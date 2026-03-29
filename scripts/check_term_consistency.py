#!/usr/bin/env python3
"""
check_term_consistency.py

Semantic drift prevention tool. Checks that:
1. Every term listed in controlled_terms frontmatter fields exists in GLOSSARY.md
2. (Optional) Terms appear in document body using canonical form, not aliases

Usage:
    cd <repo_root>
    python scripts/check_term_consistency.py [--check-body] [--path PATH]

Exit codes:
    0 — All controlled_terms are defined in GLOSSARY.md
    1 — Missing terms found
"""

import argparse
import re
import sys
from pathlib import Path

import frontmatter

try:
    from rich.console import Console
    USE_RICH = True
except ImportError:
    USE_RICH = False

ROOT = Path(__file__).parent.parent
GLOSSARY_PATH = ROOT / "GLOSSARY.md"
console = Console() if USE_RICH else None


def log(msg: str, style: str = "") -> None:
    if USE_RICH and console:
        console.print(msg, style=style)
    else:
        print(msg)


def parse_glossary_terms(glossary_path: Path) -> dict[str, dict]:
    """
    Parse GLOSSARY.md and extract:
    - canonical_terms: set of canonical form strings (from ## Term headings)
    - aliases: mapping of alias -> canonical form
    """
    if not glossary_path.exists():
        log(f"[red]ERROR[/red] GLOSSARY.md not found at {glossary_path}", "red")
        sys.exit(1)

    content = glossary_path.read_text(encoding="utf-8")
    canonical_terms: set[str] = set()
    aliases_map: dict[str, str] = {}  # alias -> canonical

    current_term = None
    for line in content.splitlines():
        # Match ## Term Name headings (but not ### sub-headings)
        h2_match = re.match(r"^## (.+)$", line)
        if h2_match:
            current_term = h2_match.group(1).strip()
            canonical_terms.add(current_term)
            # Also map canonical to itself
            aliases_map[current_term.lower()] = current_term
            continue

        # Match **Aliases:** lines
        if current_term and line.startswith("**Aliases:**"):
            aliases_raw = line.replace("**Aliases:**", "").strip()
            for alias in re.split(r",|;", aliases_raw):
                alias = alias.strip().strip(".")
                if alias:
                    aliases_map[alias.lower()] = current_term

        # Match **Canonical Form:** `term` lines
        canonical_match = re.match(r"\*\*Canonical Form:\*\* `(.+?)`", line)
        if canonical_match and current_term:
            canonical_form = canonical_match.group(1).strip()
            canonical_terms.add(canonical_form)
            aliases_map[canonical_form.lower()] = canonical_form

    return {"canonical": canonical_terms, "aliases": aliases_map}


def check_template(template_path: Path, glossary_data: dict, check_body: bool = False) -> list[str]:
    """Returns list of error messages for a template file."""
    errors = []

    try:
        post = frontmatter.load(str(template_path))
    except Exception as e:
        return [f"Failed to parse: {e}"]

    controlled_terms = post.metadata.get("controlled_terms", [])
    if not controlled_terms:
        return []

    canonical_terms = glossary_data["canonical"]
    aliases_map = glossary_data["aliases"]

    for term in controlled_terms:
        if term not in canonical_terms:
            # Check if it's a known alias
            canonical = aliases_map.get(term.lower())
            if canonical:
                errors.append(
                    f"Term '{term}' is an alias for '{canonical}' — use canonical form in controlled_terms"
                )
            else:
                errors.append(
                    f"Term '{term}' not found in GLOSSARY.md — add it before using as a controlled term"
                )

    if check_body and post.content:
        # Check that canonical terms are used, not just aliases
        for term in controlled_terms:
            canonical = aliases_map.get(term.lower(), term)
            # Check each alias of this term is not used in preference to canonical
            for alias, canonical_of_alias in aliases_map.items():
                if canonical_of_alias == canonical and alias != term.lower() and alias != canonical.lower():
                    # This is a non-canonical alias for our controlled term
                    if re.search(r'\b' + re.escape(alias) + r'\b', post.content, re.IGNORECASE):
                        if not re.search(r'\b' + re.escape(canonical) + r'\b', post.content, re.IGNORECASE):
                            errors.append(
                                f"Body uses alias '{alias}' but not canonical form '{canonical}'"
                            )

    return errors


def find_templates(search_path: Path) -> list[Path]:
    results = set(search_path.rglob("*-template.md"))
    snippets_dir = ROOT / "shared" / "_snippets"
    if snippets_dir.exists():
        results |= set(snippets_dir.glob("*.md"))
    return sorted(results)


def main():
    parser = argparse.ArgumentParser(description="Check controlled_terms against GLOSSARY.md")
    parser.add_argument("--check-body", action="store_true",
                        help="Also check that canonical forms are used in document body")
    parser.add_argument("--path", default=str(ROOT), help="Root path to search for templates")
    args = parser.parse_args()

    glossary_data = parse_glossary_terms(GLOSSARY_PATH)
    log(f"\n[bold]Term Consistency Checker[/bold]")
    log(f"Glossary: {len(glossary_data['canonical'])} canonical terms loaded")

    templates = find_templates(Path(args.path))
    log(f"Templates: {len(templates)} files to check\n")

    file_errors: dict[Path, list[str]] = {}
    for t in templates:
        errs = check_template(t, glossary_data, args.check_body)
        if errs:
            file_errors[t] = errs

    if file_errors:
        log(f"[bold red]TERM CONSISTENCY ERRORS ({len(file_errors)} files):[/bold red]\n")
        for path, errs in file_errors.items():
            rel = path.relative_to(ROOT)
            log(f"[red]✗[/red] {rel}", "red")
            for e in errs:
                log(f"    • {e}")
    else:
        log(f"[green]✓ All controlled_terms are defined in GLOSSARY.md.[/green]", "green")

    log(f"\n{'=' * 60}")
    log(f"Checked: {len(templates)} templates")
    log(f"Errors:  {len(file_errors)} files with issues")

    if file_errors:
        log("\n[bold red]FAILED[/bold red]", "bold red")
        sys.exit(1)
    else:
        log("\n[bold green]PASSED[/bold green]", "bold green")
        sys.exit(0)


if __name__ == "__main__":
    main()
