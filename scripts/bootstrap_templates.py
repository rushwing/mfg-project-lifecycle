#!/usr/bin/env python3
"""
bootstrap_templates.py

Reads all _index.yaml files in the repository and generates missing
*-template.md stub files. Safe to re-run: NEVER overwrites existing files.

Usage:
    cd <repo_root>
    python scripts/bootstrap_templates.py [--dry-run] [--phase EVT]

Options:
    --dry-run       Show what would be created without writing files
    --phase PHASE   Only process checkpoints for the specified phase (P1/EVT/DVT/PVT/MP)
    --force         Overwrite existing files (use with caution)
"""

import argparse
import sys
from datetime import date
from pathlib import Path

import yaml

try:
    from rich.console import Console
    from rich.table import Table
    USE_RICH = True
except ImportError:
    USE_RICH = False

ROOT = Path(__file__).parent.parent
REPO_DATE = date.today().isoformat()
console = Console() if USE_RICH else None


def log(msg: str, style: str = "") -> None:
    if USE_RICH and console:
        console.print(msg, style=style)
    else:
        print(msg)


def find_index_files(phase_filter: str | None = None) -> list[Path]:
    """Find all _index.yaml files, optionally filtered by phase directory prefix."""
    pattern = "*/_index.yaml" if phase_filter is None else f"*{phase_filter.lower()}*/**/_index.yaml"
    found = []
    for phase_dir in sorted(ROOT.iterdir()):
        if not phase_dir.is_dir() or phase_dir.name.startswith(".") or phase_dir.name in ("scripts", "schemas", "shared"):
            continue
        if phase_filter and phase_filter.lower() not in phase_dir.name.lower():
            continue
        for index_file in sorted(phase_dir.rglob("_index.yaml")):
            found.append(index_file)
    return found


_STATION_TO_STAGE: dict[str, str | None] = {
    "ICT": "SMT",
    "FCT": "FATP",
    "DIAG": "FATP",
    "BURN-IN": "FATP",
    "ATE": "FATP",
    "SYSTEM": "FATP",
    "OBA": "PACK",
    "SFC": None,       # spans all stages
    "Universal": None, # stage-agnostic
}


def derive_production_stages(test_stations: list[str]) -> list[str]:
    """Map test_stations to production stages. SFC and Universal → All."""
    if not test_stations or any(s in test_stations for s in ("Universal", "SFC")):
        return ["All"]
    seen: list[str] = []
    for stage in ("SMT", "FATP", "PACK"):
        if any(_STATION_TO_STAGE.get(s) == stage for s in test_stations):
            seen.append(stage)
    return seen if seen else ["All"]


def build_frontmatter(doc: dict, checkpoint_id: str, phase: str, checkpoint_name: str) -> str:
    """Build YAML frontmatter string from a document entry in _index.yaml."""
    product_families = doc.get("product_families", ["GPU", "DC-L6", "Automotive", "Embedded"])
    test_stations = doc.get("test_stations", ["Universal"])
    controlled_terms = doc.get("controlled_terms", [])
    required_sections = doc.get("required_sections", [
        "1. Purpose and Scope",
        "2. References",
        "3. Main Content",
        "4. Revision History"
    ])

    fm = {
        "doc_id": doc["doc_id"],
        "title": doc["title"],
        "slug": doc["slug"],
        "version": "0.1.0",
        "phase": phase,
        "checkpoint": checkpoint_id.split("-")[1],  # CP1, CP2, etc.
        "checkpoint_name": checkpoint_name,
        "doc_type": doc.get("doc_type", "plan"),
        "priority": doc.get("priority", "required"),
        "product_families": product_families,
        "test_stations": test_stations,
        "production_stages": doc.get("production_stages", derive_production_stages(test_stations)),
        "owner_role": doc.get("owner_role", "MTE Staff"),
        "status": "template-stub",
        "created_date": REPO_DATE,
        "last_updated": REPO_DATE,
        "rag_chunk_strategy": doc.get("rag_chunk_strategy", "by-section"),
        "embedding_priority": doc.get("embedding_priority", "medium"),
        "controlled_terms": controlled_terms,
        "related_docs": doc.get("related_docs", []),
        "required_sections": required_sections,
        "supersedes": None,
    }
    return yaml.dump(fm, allow_unicode=True, sort_keys=False, default_flow_style=False)


def build_stub_body(doc: dict) -> str:
    """Build the markdown body of a stub template."""
    title = doc["title"]
    doc_id = doc["doc_id"]
    required_sections = doc.get("required_sections", [
        "1. Purpose and Scope",
        "2. References",
        "3. Main Content",
        "4. Revision History"
    ])

    lines = [
        f"# {title}",
        "",
        f"> **Doc ID:** `{doc_id}`  ",
        f"> **Status:** `template-stub` — Content to be filled by MTE author.  ",
        f"> **Priority:** `{doc.get('priority', 'required')}`",
        "",
        "---",
        "",
    ]

    for section in required_sections:
        lines.append(f"## {section}")
        lines.append("")
        lines.append("<!-- TODO: Fill in content -->")
        lines.append("")

    return "\n".join(lines)


def create_stub(template_path: Path, doc: dict, checkpoint_id: str, phase: str,
                checkpoint_name: str, dry_run: bool = False, force: bool = False) -> str:
    """
    Create a stub template file. Returns 'created', 'skipped', or 'would_create'.
    """
    if template_path.exists() and not force:
        return "skipped"

    if dry_run:
        return "would_create"

    frontmatter_str = build_frontmatter(doc, checkpoint_id, phase, checkpoint_name)
    body_str = build_stub_body(doc)
    content = f"---\n{frontmatter_str}---\n\n{body_str}"

    template_path.parent.mkdir(parents=True, exist_ok=True)
    template_path.write_text(content, encoding="utf-8")
    return "created"


def process_index(index_path: Path, dry_run: bool = False, force: bool = False) -> dict:
    """Process a single _index.yaml file and create stubs for all declared documents."""
    results = {"created": 0, "skipped": 0, "would_create": 0, "errors": 0}

    with open(index_path, encoding="utf-8") as f:
        index = yaml.safe_load(f)

    if not index:
        log(f"  [yellow]WARN[/yellow] Empty or invalid index: {index_path}", "yellow")
        return results

    checkpoint_id = index.get("checkpoint_id", "UNKNOWN")
    phase = index.get("phase", "UNKNOWN")
    checkpoint_name = index.get("checkpoint_name", "")
    documents = index.get("documents", [])

    checkpoint_dir = index_path.parent

    for doc in documents:
        slug = doc.get("slug")
        if not slug:
            log(f"  [red]ERROR[/red] Missing slug in {checkpoint_id} document: {doc.get('doc_id', '?')}", "red")
            results["errors"] += 1
            continue

        template_path = checkpoint_dir / f"{slug}-template.md"
        status = create_stub(template_path, doc, checkpoint_id, phase, checkpoint_name, dry_run, force)
        results[status] += 1

        prefix = "[dim]DRY-RUN[/dim]" if dry_run else ""
        if status == "created":
            log(f"  [green]CREATED[/green] {prefix} {template_path.relative_to(ROOT)}", "green")
        elif status == "would_create":
            log(f"  [cyan]WOULD CREATE[/cyan] {template_path.relative_to(ROOT)}", "cyan")
        # Silently skip existing files unless verbose

    return results


def main():
    parser = argparse.ArgumentParser(description="Bootstrap template stubs from _index.yaml files")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be created without writing")
    parser.add_argument("--phase", help="Filter to specific phase (P1/EVT/DVT/PVT/MP)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing stubs")
    args = parser.parse_args()

    if args.force and not args.dry_run:
        log("[bold red]WARNING: --force will overwrite existing template files![/bold red]", "bold red")
        confirm = input("Type 'yes' to confirm: ")
        if confirm.strip().lower() != "yes":
            log("Aborted.", "yellow")
            sys.exit(0)

    index_files = find_index_files(args.phase)
    if not index_files:
        log(f"[yellow]No _index.yaml files found{' for phase ' + args.phase if args.phase else ''}.[/yellow]")
        sys.exit(0)

    log(f"\n[bold]Bootstrap Templates[/bold] — {'DRY RUN' if args.dry_run else 'LIVE RUN'}")
    log(f"Found {len(index_files)} checkpoint index file(s)\n")

    totals = {"created": 0, "skipped": 0, "would_create": 0, "errors": 0}

    for index_path in index_files:
        checkpoint_rel = index_path.parent.relative_to(ROOT)
        log(f"\n[bold]{checkpoint_rel}[/bold]")
        results = process_index(index_path, args.dry_run, args.force)
        for k, v in results.items():
            totals[k] += v

    log("\n" + "=" * 60)
    if args.dry_run:
        log(f"[cyan]Would create:[/cyan] {totals['would_create']} files")
    else:
        log(f"[green]Created:[/green]      {totals['created']} files")
        log(f"[dim]Skipped:[/dim]      {totals['skipped']} files (already exist)")
    if totals["errors"]:
        log(f"[red]Errors:[/red]       {totals['errors']} entries")
        sys.exit(1)

    log("\n[bold green]Done.[/bold green]" if not args.dry_run else "\n[bold cyan]Dry run complete.[/bold cyan]")


if __name__ == "__main__":
    main()
