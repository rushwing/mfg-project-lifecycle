#!/usr/bin/env python3
"""
validate_frontmatter.py

Validates YAML frontmatter in all *-template.md files against
schemas/template_frontmatter.schema.json.

Also checks global doc_id uniqueness across the repository.

Usage:
    cd <repo_root>
    python scripts/validate_frontmatter.py [--path PATH] [--strict]

Exit codes:
    0 — All validations passed
    1 — One or more validation errors found
"""

import argparse
import json
import sys
from pathlib import Path

import frontmatter
import jsonschema
import yaml

try:
    from rich.console import Console
    from rich.table import Table
    USE_RICH = True
except ImportError:
    USE_RICH = False

ROOT = Path(__file__).parent.parent
SCHEMA_PATH = ROOT / "schemas" / "template_frontmatter.schema.json"
console = Console() if USE_RICH else None


def log(msg: str, style: str = "") -> None:
    if USE_RICH and console:
        console.print(msg, style=style)
    else:
        print(msg)


def find_templates(search_path: Path) -> list[Path]:
    """Find all *-template.md files under search_path, plus shared snippets."""
    results = set(search_path.rglob("*-template.md"))
    snippets_dir = ROOT / "shared" / "_snippets"
    if snippets_dir.exists():
        results |= set(snippets_dir.glob("*.md"))
    return sorted(results)


def load_schema() -> dict:
    if not SCHEMA_PATH.exists():
        log(f"[red]ERROR[/red] Schema not found: {SCHEMA_PATH}", "red")
        sys.exit(1)
    with open(SCHEMA_PATH) as f:
        return json.load(f)


def validate_file(template_path: Path, schema: dict) -> list[str]:
    """Validate a single template file. Returns list of error messages."""
    errors = []

    try:
        post = frontmatter.load(str(template_path))
    except Exception as e:
        return [f"Failed to parse frontmatter: {e}"]

    metadata = dict(post.metadata)
    if not metadata:
        return ["No frontmatter found (file may be missing --- delimiters)"]

    validator = jsonschema.Draft7Validator(schema)
    for error in sorted(validator.iter_errors(metadata), key=lambda e: e.path):
        path = ".".join(str(p) for p in error.path) or "(root)"
        errors.append(f"Field '{path}': {error.message}")

    return errors


def check_doc_id_uniqueness(templates: list[Path]) -> list[tuple[str, list[Path]]]:
    """Returns list of (doc_id, [files]) tuples where doc_id appears more than once."""
    id_map: dict[str, list[Path]] = {}
    for t in templates:
        try:
            post = frontmatter.load(str(t))
            doc_id = post.metadata.get("doc_id")
            if doc_id:
                id_map.setdefault(doc_id, []).append(t)
        except Exception:
            pass
    return [(doc_id, paths) for doc_id, paths in id_map.items() if len(paths) > 1]


def main():
    parser = argparse.ArgumentParser(description="Validate template frontmatter against JSON Schema")
    parser.add_argument("--path", default=str(ROOT), help="Root path to search for templates")
    parser.add_argument("--strict", action="store_true", help="Fail on warnings as well as errors")
    args = parser.parse_args()

    schema = load_schema()
    search_path = Path(args.path)
    templates = find_templates(search_path)

    if not templates:
        log("[yellow]No *-template.md files found.[/yellow]", "yellow")
        sys.exit(0)

    log(f"\n[bold]Frontmatter Validator[/bold]")
    log(f"Schema:    {SCHEMA_PATH.relative_to(ROOT)}")
    log(f"Templates: {len(templates)} files found\n")

    file_errors: dict[Path, list[str]] = {}
    for t in templates:
        errs = validate_file(t, schema)
        if errs:
            file_errors[t] = errs

    # Report per-file errors
    if file_errors:
        log(f"[bold red]VALIDATION ERRORS ({len(file_errors)} files):[/bold red]\n")
        for path, errs in file_errors.items():
            rel = path.relative_to(ROOT)
            log(f"[red]✗[/red] {rel}", "red")
            for e in errs:
                log(f"    • {e}")
    else:
        log(f"[green]✓ All {len(templates)} templates passed schema validation.[/green]", "green")

    # Check doc_id uniqueness
    duplicates = check_doc_id_uniqueness(templates)
    if duplicates:
        log(f"\n[bold red]DUPLICATE doc_id ({len(duplicates)} conflicts):[/bold red]")
        for doc_id, paths in duplicates:
            log(f"  [red]{doc_id}[/red] appears in:")
            for p in paths:
                log(f"    - {p.relative_to(ROOT)}")
    else:
        log(f"[green]✓ All doc_ids are unique.[/green]", "green")

    # Summary
    total_errors = len(file_errors) + len(duplicates)
    log(f"\n{'=' * 60}")
    log(f"Checked: {len(templates)} templates")
    log(f"Errors:  {total_errors}")

    if total_errors > 0:
        log("\n[bold red]FAILED[/bold red]", "bold red")
        sys.exit(1)
    else:
        log("\n[bold green]PASSED[/bold green]", "bold green")
        sys.exit(0)


if __name__ == "__main__":
    main()
