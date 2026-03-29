#!/usr/bin/env python3
"""
validate_structure.py

Checks structural integrity of the knowledge base:
1. All documents declared in _index.yaml have corresponding *-template.md files
2. All related_docs references in template frontmatter resolve to existing doc_ids
3. _index.yaml files conform to checkpoint_index.schema.json

Usage:
    cd <repo_root>
    python scripts/validate_structure.py

Exit codes:
    0 — Structure is complete and consistent
    1 — Missing files or broken references found
"""

import json
import sys
from pathlib import Path

import frontmatter
import jsonschema
import yaml

try:
    from rich.console import Console
    USE_RICH = True
except ImportError:
    USE_RICH = False

ROOT = Path(__file__).parent.parent
INDEX_SCHEMA_PATH = ROOT / "schemas" / "checkpoint_index.schema.json"
console = Console() if USE_RICH else None


def log(msg: str, style: str = "") -> None:
    if USE_RICH and console:
        console.print(msg, style=style)
    else:
        print(msg)


def find_index_files() -> list[Path]:
    index_files = []
    for phase_dir in sorted(ROOT.iterdir()):
        if not phase_dir.is_dir() or phase_dir.name.startswith((".", "_")) or phase_dir.name in ("scripts", "schemas", "shared"):
            continue
        for f in sorted(phase_dir.rglob("_index.yaml")):
            index_files.append(f)
    return index_files


def build_doc_id_registry(index_files: list[Path]) -> dict[str, Path]:
    """Build a global mapping of doc_id -> expected template path."""
    registry: dict[str, Path] = {}
    for index_path in index_files:
        with open(index_path, encoding="utf-8") as f:
            index = yaml.safe_load(f)
        if not index:
            continue
        checkpoint_dir = index_path.parent
        for doc in index.get("documents", []):
            doc_id = doc.get("doc_id")
            slug = doc.get("slug")
            if doc_id and slug:
                registry[doc_id] = checkpoint_dir / f"{slug}-template.md"
    return registry


def check_missing_stubs(registry: dict[str, Path]) -> list[tuple[str, Path]]:
    """Return (doc_id, expected_path) for declared docs without files."""
    return [(doc_id, path) for doc_id, path in registry.items() if not path.exists()]


def check_broken_related_docs(registry: dict[str, Path]) -> list[tuple[Path, str]]:
    """Return (template_path, broken_ref_doc_id) for broken related_docs references."""
    broken = []
    known_ids = set(registry.keys())
    for template_path in sorted(ROOT.rglob("*-template.md")):
        try:
            post = frontmatter.load(str(template_path))
            related = post.metadata.get("related_docs", [])
            for ref_id in related:
                if ref_id and ref_id not in known_ids:
                    broken.append((template_path, ref_id))
        except Exception:
            pass
    return broken


def validate_index_schemas(index_files: list[Path], schema: dict) -> dict[Path, list[str]]:
    """Validate each _index.yaml against checkpoint_index.schema.json."""
    errors: dict[Path, list[str]] = {}
    validator = jsonschema.Draft7Validator(schema)
    for index_path in index_files:
        with open(index_path, encoding="utf-8") as f:
            index = yaml.safe_load(f)
        if not index:
            errors[index_path] = ["Empty or unparseable YAML"]
            continue
        errs = [
            f"Field '{'.'.join(str(p) for p in e.path) or '(root)'}': {e.message}"
            for e in sorted(validator.iter_errors(index), key=lambda x: x.path)
        ]
        if errs:
            errors[index_path] = errs
    return errors


def main():
    log(f"\n[bold]Structure Validator[/bold]")

    index_files = find_index_files()
    log(f"Found {len(index_files)} _index.yaml files")

    # Load schema
    if INDEX_SCHEMA_PATH.exists():
        with open(INDEX_SCHEMA_PATH) as f:
            index_schema = json.load(f)
        schema_errors = validate_index_schemas(index_files, index_schema)
    else:
        log(f"[yellow]WARN[/yellow] Index schema not found, skipping schema validation")
        schema_errors = {}

    # Build registry
    registry = build_doc_id_registry(index_files)
    log(f"Declared documents: {len(registry)}\n")

    total_errors = 0

    # 1. Index schema errors
    if schema_errors:
        log(f"[bold red]INDEX SCHEMA ERRORS ({len(schema_errors)} files):[/bold red]")
        for path, errs in schema_errors.items():
            log(f"  [red]✗[/red] {path.relative_to(ROOT)}")
            for e in errs:
                log(f"      • {e}")
        total_errors += len(schema_errors)
    else:
        log(f"[green]✓ All _index.yaml files pass schema validation.[/green]")

    # 2. Missing stub files
    missing = check_missing_stubs(registry)
    if missing:
        log(f"\n[bold yellow]MISSING TEMPLATE STUBS ({len(missing)} files):[/bold yellow]")
        log(f"  Run 'python scripts/bootstrap_templates.py' to generate them.")
        for doc_id, path in sorted(missing):
            log(f"  [yellow]![/yellow] {doc_id} → {path.relative_to(ROOT)}")
        total_errors += len(missing)
    else:
        log(f"[green]✓ All declared documents have template files.[/green]")

    # 3. Broken related_docs references
    broken = check_broken_related_docs(registry)
    if broken:
        log(f"\n[bold red]BROKEN related_docs REFERENCES ({len(broken)}):[/bold red]")
        for path, ref_id in sorted(broken):
            log(f"  [red]✗[/red] {path.relative_to(ROOT)}: references unknown doc_id '{ref_id}'")
        total_errors += len(broken)
    else:
        log(f"[green]✓ All related_docs references resolve correctly.[/green]")

    log(f"\n{'=' * 60}")
    log(f"Total issues: {total_errors}")

    if total_errors > 0:
        log("\n[bold red]FAILED[/bold red]", "bold red")
        sys.exit(1)
    else:
        log("\n[bold green]PASSED[/bold green]", "bold green")
        sys.exit(0)


if __name__ == "__main__":
    main()
