#!/usr/bin/env python3
"""
bump_version.py

KB version management utility. Bumps the version in pyproject.toml and
prepares CHANGELOG.md for a new release.

Usage:
    uv run python scripts/bump_version.py patch    # 0.1.0 → 0.1.1
    uv run python scripts/bump_version.py minor    # 0.1.0 → 0.2.0
    uv run python scripts/bump_version.py major    # 0.1.0 → 1.0.0
    uv run python scripts/bump_version.py --dry-run minor

Version Semantics:
    MAJOR  Breaking schema changes (new required frontmatter fields, renamed enums)
    MINOR  New phases/checkpoints/templates, new GLOSSARY terms, new scripts
    PATCH  Template content fixes, script bugfixes, GLOSSARY clarifications

After running this script:
    1. Review CHANGELOG.md [Unreleased] section — fill in your changes
    2. git add pyproject.toml CHANGELOG.md
    3. git commit -m "chore: release vX.Y.Z"
    4. git tag vX.Y.Z
    5. git push && git push --tags
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

try:
    from rich.console import Console
    USE_RICH = True
except ImportError:
    USE_RICH = False

ROOT = Path(__file__).parent.parent
PYPROJECT = ROOT / "pyproject.toml"
CHANGELOG = ROOT / "CHANGELOG.md"
console = Console() if USE_RICH else None


def log(msg: str, style: str = "") -> None:
    if USE_RICH and console:
        console.print(msg, style=style)
    else:
        print(msg)


def get_current_version() -> str:
    """Read current version from pyproject.toml."""
    content = PYPROJECT.read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', content, re.MULTILINE)
    if not match:
        log("[red]ERROR[/red] Could not find version in pyproject.toml")
        sys.exit(1)
    return match.group(1)


def bump(version: str, bump_type: str) -> str:
    """Calculate the next version string."""
    parts = version.split(".")
    if len(parts) != 3:
        log(f"[red]ERROR[/red] Version '{version}' is not valid semver (X.Y.Z)")
        sys.exit(1)
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
    if bump_type == "major":
        return f"{major + 1}.0.0"
    elif bump_type == "minor":
        return f"{major}.{minor + 1}.0"
    elif bump_type == "patch":
        return f"{major}.{minor}.{patch + 1}"
    else:
        log(f"[red]ERROR[/red] Unknown bump type: {bump_type}")
        sys.exit(1)


def update_pyproject(old_version: str, new_version: str) -> None:
    """Update version in pyproject.toml."""
    content = PYPROJECT.read_text(encoding="utf-8")
    updated = re.sub(
        r'^(version\s*=\s*)"[^"]+"',
        f'\\1"{new_version}"',
        content,
        count=1,
        flags=re.MULTILINE,
    )
    PYPROJECT.write_text(updated, encoding="utf-8")


def update_changelog(old_version: str, new_version: str, release_date: str) -> None:
    """
    Move [Unreleased] content into a new versioned section.
    Leaves a fresh empty [Unreleased] section at the top.
    """
    content = CHANGELOG.read_text(encoding="utf-8")

    # Find the [Unreleased] section
    unreleased_match = re.search(
        r"(## \[Unreleased\]\n)(.*?)(\n---\n\n## \[)",
        content,
        re.DOTALL,
    )
    if not unreleased_match:
        log("[yellow]WARN[/yellow] Could not locate [Unreleased] section in CHANGELOG.md. Skipping changelog update.")
        return

    unreleased_body = unreleased_match.group(2).strip()

    # Build the new version section
    new_section = f"## [{new_version}] — {release_date}\n\n"
    if unreleased_body and unreleased_body != "- (list changes not yet released)":
        new_section += unreleased_body + "\n"
    else:
        new_section += f"### Changed\n- KB version bumped from {old_version} to {new_version}\n"

    # Replace: [Unreleased] section → fresh empty + new version section
    fresh_unreleased = (
        "## [Unreleased]\n\n"
        "### Added\n- (list changes not yet released)\n\n"
        "---\n\n"
    )
    updated = content.replace(
        unreleased_match.group(0),
        fresh_unreleased + new_section + "\n---\n\n## [",
    )

    # Update comparison links at bottom
    repo_url_match = re.search(r"(https://github\.com/[^/]+/[^/]+)", updated)
    if repo_url_match:
        repo = repo_url_match.group(1)
        # Update [Unreleased] link
        updated = re.sub(
            r"\[Unreleased\]: .*",
            f"[Unreleased]: {repo}/compare/v{new_version}...HEAD",
            updated,
        )
        # Add new version link (after [Unreleased] link)
        old_link_pattern = f"[{old_version}]:"
        new_link = f"[{new_version}]: {repo}/compare/v{old_version}...v{new_version}"
        if old_link_pattern in updated:
            updated = updated.replace(
                old_link_pattern,
                f"{new_link}\n{old_link_pattern}",
            )

    CHANGELOG.write_text(updated, encoding="utf-8")


def count_templates() -> int:
    """Count current template files for release notes."""
    results = set(ROOT.rglob("*-template.md"))
    snippets_dir = ROOT / "shared" / "_snippets"
    if snippets_dir.exists():
        results |= set(snippets_dir.glob("*.md"))
    return len(results)


def count_glossary_terms() -> int:
    """Count ## headings in GLOSSARY.md."""
    glossary = ROOT / "GLOSSARY.md"
    if not glossary.exists():
        return 0
    content = glossary.read_text(encoding="utf-8")
    return len(re.findall(r"^### ", content, re.MULTILINE))


def main():
    parser = argparse.ArgumentParser(
        description="Bump KB version in pyproject.toml and update CHANGELOG.md",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "bump_type",
        choices=["major", "minor", "patch"],
        help="Version component to bump",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing files",
    )
    args = parser.parse_args()

    current = get_current_version()
    new = bump(current, args.bump_type)
    today = date.today().isoformat()
    templates = count_templates()
    terms = count_glossary_terms()

    log(f"\n[bold]KB Version Bump[/bold]")
    log(f"  {current}  →  [bold green]{new}[/bold green]  ({args.bump_type})")
    log(f"  Release date : {today}")
    log(f"  Templates    : {templates}")
    log(f"  GLOSSARY     : {terms} terms")

    if args.dry_run:
        log("\n[cyan]DRY RUN — no files written.[/cyan]")
        return

    update_pyproject(current, new)
    log(f"\n[green]✓[/green] pyproject.toml updated  version = \"{new}\"")

    update_changelog(current, new, today)
    log(f"[green]✓[/green] CHANGELOG.md updated  [{new}] — {today}")

    log(f"""
[bold]Next steps:[/bold]
  1. Edit [bold]CHANGELOG.md[/bold] → fill in [Unreleased] section with your changes
  2. [dim]git add pyproject.toml CHANGELOG.md[/dim]
  3. [dim]git commit -m "chore: release v{new}"[/dim]
  4. [dim]git tag v{new}[/dim]
  5. [dim]git push && git push --tags[/dim]
""")


if __name__ == "__main__":
    main()
