#!/usr/bin/env python3
from pathlib import Path
from urllib.parse import unquote
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
NORMATIVE_ROOTS = (
    "governance/constitution", "governance/charter", "governance/operating-model",
    "governance/authority", "governance/platforms", "governance/engineering",
    "governance/repository", "governance/change", "standards",
)


def version_key(path):
    match = re.search(r"-v(\d+)\.(\d+)\.(\d+)-release-manifest\.md$", path.name)
    return tuple(map(int, match.groups())) if match else None


def fields_from(text):
    return dict(re.findall(r"^\| ([^|]+?) \| ([^|]+?) \|$", text, re.MULTILINE))


def local_link_targets(path, text):
    for raw in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = raw.strip().split(" ", 1)[0]
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = unquote(target.split("#", 1)[0])
        if target:
            yield (path.parent / target).resolve()


errors = []
warnings = []
manifests = [(version_key(path), path) for path in RELEASE_DIR.glob("KE-REL-*-v*-release-manifest.md")]
manifests = [(version, path) for version, path in manifests if version is not None]

if not manifests:
    errors.append("missing versioned release manifest")
    manifest_version = None
    manifest = None
    rows = []
else:
    manifest_version, manifest = max(manifests, key=lambda item: item[0])
    text = manifest.read_text(encoding="utf-8")
    rows = re.findall(r"^\| (KE-[A-Z0-9-]+) \| ([^|]+?) \| `([^`]+)` \|$", text, re.MULTILINE)
    if not rows:
        errors.append(f"{manifest.name}: contains no normative inventory rows")
    manifest_fields = fields_from(text)
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
        fields = fields_from(artifact)
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

    register_path = ROOT / "reference/registers/KE-REG-001-authoritative-artifact-register.md"
    if not register_path.is_file():
        errors.append("missing authoritative artifact register")
    else:
        register = register_path.read_text(encoding="utf-8")
        for identifier, version, relpath in rows:
            candidates = [line for line in register.splitlines() if line.startswith(f"| {identifier} |")]
            aligned = any(
                version.strip() in [cell.strip() for cell in line.strip("|").split("|")]
                and f"`{relpath}`" in line
                for line in candidates
            )
            if not aligned:
                errors.append(f"{identifier}: release manifest and authoritative register are not aligned")

    manifest_ids = {identifier for identifier, _, _ in rows}
    discovered = {}
    for root_name in NORMATIVE_ROOTS:
        for path in (ROOT / root_name).glob("*.md"):
            fields = fields_from(path.read_text(encoding="utf-8"))
            identifier = fields.get("Identifier")
            if not identifier:
                errors.append(f"{path.relative_to(ROOT)}: normative artifact has no Identifier")
                continue
            if identifier in discovered:
                errors.append(f"{identifier}: duplicate normative source at {discovered[identifier]} and {path.relative_to(ROOT)}")
            discovered[identifier] = path.relative_to(ROOT)
    for identifier in sorted(set(discovered) - manifest_ids):
        errors.append(f"{identifier}: normative artifact is absent from the current release manifest")
    for identifier in sorted(manifest_ids - set(discovered)):
        errors.append(f"{identifier}: manifest entry is outside the governed normative roots")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
if manifest_version is not None:
    release_label = f"KE v{'.'.join(map(str, manifest_version))}"
    if release_label not in readme:
        errors.append(f"README does not identify {release_label}")

portfolio_path = ROOT / "governance/platforms/KE-004-platform-portfolio-and-responsibility-map.md"
platform_register_path = ROOT / "reference/registers/KE-REG-002-platform-portfolio-register.md"
if not portfolio_path.is_file() or not platform_register_path.is_file():
    errors.append("missing platform portfolio authority or register")
else:
    portfolio = portfolio_path.read_text(encoding="utf-8")
    platform_register = platform_register_path.read_text(encoding="utf-8")
    platform_rows = re.findall(r"^\| (K[A-Z]{2}) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \| `([^`]+)` \|$", portfolio, re.MULTILINE)
    portfolio_ids = set()
    coordinates = set()
    for identifier, _, _, _, relpath in platform_rows:
        portfolio_ids.add(identifier)
        coordinates.add(relpath.rstrip("/"))
        if not (ROOT / relpath).is_dir():
            errors.append(f"{identifier}: missing canonical platform coordinate {relpath}")
        if not re.search(rf"^\| {identifier} \|.*`{re.escape(relpath)}`.*\|$", platform_register, re.MULTILINE):
            errors.append(f"{identifier}: platform map and register are not aligned")
    if len(portfolio_ids) != len(platform_rows):
        errors.append("platform portfolio contains duplicate identifiers")
    actual_coordinates = {str(path.relative_to(ROOT)) for path in (ROOT / "platforms").iterdir() if path.is_dir()}
    for relpath in sorted(actual_coordinates - coordinates):
        errors.append(f"{relpath}: platform directory is absent from KE-004")

link_files = [ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "SECURITY.md"]
link_files += [ROOT / relpath for _, _, relpath in rows]
link_files += list((ROOT / "templates").glob("*.md"))
link_files += list((ROOT / "platforms").glob("*/*.md"))
for path in link_files:
    if not path.is_file():
        continue
    for target in local_link_targets(path, path.read_text(encoding="utf-8")):
        try:
            target.relative_to(ROOT)
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: local link escapes the repository")
            continue
        if not target.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken local link to {target.relative_to(ROOT)}")

for relpath in ("CODEOWNERS", ".github/workflows/ke-repository-validation.yml", "SECURITY.md", "CONTRIBUTING.md"):
    if not (ROOT / relpath).is_file():
        errors.append(f"missing repository control: {relpath}")

for relpath in ("templates", "methodologies", "patterns"):
    files = [path for path in (ROOT / relpath).rglob("*") if path.is_file() and path.name != ".gitkeep"]
    if not files:
        warnings.append(f"{relpath}: placeholder-only capability area")
if not (ROOT / "LICENSE").is_file():
    warnings.append("LICENSE: public-repository licensing decision remains unresolved")

if warnings:
    print("KE repository validation warnings:")
    for warning in warnings:
        print(f"- {warning}")

if errors:
    print("KE repository validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"KE repository validation passed for {len(rows)} normative artifacts using {manifest.name}.")
