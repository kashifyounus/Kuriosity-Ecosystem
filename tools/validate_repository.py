#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "governance/releases/KE-REL-004-v2.0.0-release-manifest.md"
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

errors = []
if not MANIFEST.exists():
    errors.append(f"missing manifest: {MANIFEST.relative_to(ROOT)}")
else:
    text = MANIFEST.read_text(encoding="utf-8")
    rows = re.findall(r"^\| (KE-[A-Z0-9-]+) \| ([^|]+?) \| \`([^\`]+)\` \|$", text, re.MULTILINE)
    if not rows:
        errors.append("manifest contains no normative inventory rows")
    for identifier, version, relpath in rows:
        path = ROOT / relpath
        if not path.is_file():
            errors.append(f"{identifier}: missing canonical path {relpath}")
            continue
        content = path.read_text(encoding="utf-8")
        fields = dict(re.findall(r"^\| ([^|]+?) \| ([^|]+?) \|$", content, re.MULTILINE))
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
if "KE v2.0.0" not in readme:
    errors.append("README does not identify KE v2.0.0")

for relpath in ("CODEOWNERS", ".github/workflows/ke-repository-validation.yml"):
    if not (ROOT / relpath).is_file():
        errors.append(f"missing repository control: {relpath}")

if errors:
    print("KE repository validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"KE repository validation passed for {len(rows)} normative artifacts.")
