#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
RELEASE_DIR = ROOT / "governance/releases"
REQUIRED_FIELDS = (
    "Identifier", "Title", "Artifact Type", "Version", "Lifecycle Status",
    "Approval Status", "Verification Status", "Authority", "Owner",
    "Effective Date", "Scope", "Amendment Path", "Supersession State",
)
ALLOWED_LIFECYCLE = {
    "Draft", "Proposed", "Review Required", "Effective", "Deprecated",
    "Superseded", "Retired", "Archived",
}
ALLOWED_APPROVAL = {"Pending", "Approved", "Ratified", "Rejected", "Not Applicable"}
ALLOWED_VERIFICATION = {
    "Not Reviewed", "Pass", "Pass with Conditions", "Fail", "Blocked", "Not Applicable",
}


def version_key(path):
    match = re.search(r"-v(\d+)\.(\d+)\.(\d+)-release-manifest\.md$", path.name)
    return tuple(map(int, match.groups())) if match else None


manifests = [(version_key(path), path) for path in RELEASE_DIR.glob("KE-REL-*-v*-release-manifest.md")]
manifests = [(version, path) for version, path in manifests if version is not None]
errors = []

if not manifests:
    errors.append("missing versioned release manifest")
    manifest_version = None
    manifest = None
    rows = []
else:
    manifest_version, manifest = max(manifests, key=lambda item: item[0])
    text = manifest.read_text(encoding="utf-8")
    rows = re.findall(r"^\| (KE-[A-Z0-9-]+) \| ([^|]+?) \| \x60([^\x60]+)\x60 \|$", text, re.MULTILINE)
    if not rows:
        errors.append(f"{manifest.name}: contains no normative inventory rows")
    manifest_fields = dict(re.findall(r"^\| ([^|]+?) \| ([^|]+?) \|$", text, re.MULTILINE))
    expected_release = ".".join(map(str, manifest_version))
    if manifest_fields.get("Artifact Type") != "Release Manifest":
        errors.append(f"{manifest.name}: invalid artifact type")
    if manifest_fields.get("Version") != expected_release:
        errors.append(f"{manifest.name}: version metadata mismatch")

    identifiers = [identifier for identifier, _, _ in rows]
    if len(identifiers) != len(set(identifiers)):
        errors.append(f"{manifest.name}: duplicate normative identifier")

    for identifier, version, relpath in rows:
        path = ROOT / relpath
        if not path.is_file():
            errors.append(f"{identifier}: missing canonical path {relpath}")
            continue
        artifact = path.read_text(encoding="utf-8")
        fields = dict(re.findall(r"^\| ([^|]+?) \| ([^|]+?) \|$", artifact, re.MULTILINE))
        for field in REQUIRED_FIELDS:
            if field not in fields:
                errors.append(f"{identifier}: missing metadata field {field}")
        if fields.get("Identifier") != identifier:
            errors.append(f"{identifier}: identifier metadata mismatch")
        if fields.get("Version") != version.strip():
            errors.append(f"{identifier}: version metadata mismatch")
        if fields.get("Lifecycle Status") not in ALLOWED_LIFECYCLE:
            errors.append(f"{identifier}: invalid lifecycle status")
        if fields.get("Approval Status") not in ALLOWED_APPROVAL:
            errors.append(f"{identifier}: invalid approval status")
        if fields.get("Verification Status") not in ALLOWED_VERIFICATION:
            errors.append(f"{identifier}: invalid verification status")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
if manifest_version is not None:
    release_label = f"KE v{'.'.join(map(str, manifest_version))}"
    if release_label not in readme:
        errors.append(f"README does not identify {release_label}")

for relpath in ("CODEOWNERS", ".github/workflows/ke-repository-validation.yml"):
    if not (ROOT / relpath).is_file():
        errors.append(f"missing repository control: {relpath}")

if errors:
    print("KE repository validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"KE repository validation passed for {len(rows)} normative artifacts using {manifest.name}.")
