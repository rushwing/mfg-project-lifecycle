#!/usr/bin/env python3
"""
validate_i18n.py

Validates i18n/ translation data:
1. YAML files parse without error
2. doc_titles.yaml covers every doc_id declared in _index.yaml files and
   shared/_snippets/*.md frontmatter
3. Every doc_titles.yaml entry has an "en" key
4. section_titles.yaml entries each have at least one non-English key

Usage:
    cd <repo_root>
    python scripts/validate_i18n.py

Exit codes:
    0 — All checks passed
    1 — One or more errors found
"""

import sys
from pathlib import Path

import frontmatter
import yaml

try:
    from rich.console import Console
    USE_RICH = True
except ImportError:
    USE_RICH = False

ROOT = Path(__file__).parent.parent
I18N_DIR = ROOT / "i18n"
DOC_TITLES_PATH = I18N_DIR / "doc_titles.yaml"
SECTION_TITLES_PATH = I18N_DIR / "section_titles.yaml"
console = Console() if USE_RICH else None


def log(msg: str, style: str = "") -> None:
    if USE_RICH and console:
        console.print(msg, style=style)
    else:
        print(msg)


def load_yaml(path: Path) -> tuple[dict | None, str | None]:
    """Load and parse a YAML file. Returns (data, error_message)."""
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        return data, None
    except yaml.YAMLError as e:
        return None, str(e)


def collect_all_doc_ids() -> list[str]:
    """Collect all doc_ids from _index.yaml files and shared snippet frontmatter."""
    doc_ids = []

    # Lifecycle doc_ids from _index.yaml
    for index_file in sorted(ROOT.rglob("_index.yaml")):
        try:
            data = yaml.safe_load(index_file.read_text(encoding="utf-8"))
            for doc in data.get("documents", []):
                if "doc_id" in doc:
                    doc_ids.append(doc["doc_id"])
        except Exception as e:
            log(f"[yellow]WARN[/yellow] Could not parse {index_file.relative_to(ROOT)}: {e}")

    # Shared snippet doc_ids from frontmatter
    snippets_dir = ROOT / "shared" / "_snippets"
    if snippets_dir.exists():
        for f in sorted(snippets_dir.glob("*.md")):
            try:
                post = frontmatter.load(str(f))
                doc_id = post.metadata.get("doc_id")
                if doc_id:
                    doc_ids.append(doc_id)
            except Exception as e:
                log(f"[yellow]WARN[/yellow] Could not parse {f.relative_to(ROOT)}: {e}")

    return doc_ids


def main() -> None:
    errors: list[str] = []

    log("\n[bold]i18n Validator[/bold]")

    # ── 1. YAML parse checks ──────────────────────────────────────────────────

    for path in (DOC_TITLES_PATH, SECTION_TITLES_PATH):
        if not path.exists():
            errors.append(f"Missing file: {path.relative_to(ROOT)}")
            continue
        data, err = load_yaml(path)
        if err:
            errors.append(f"{path.relative_to(ROOT)}: YAML parse error — {err}")
        elif not isinstance(data, dict):
            errors.append(f"{path.relative_to(ROOT)}: expected a YAML mapping at top level")

    if any("YAML parse error" in e or "Missing file" in e for e in errors):
        # Can't proceed with content checks if files are broken
        for e in errors:
            log(f"[red]✗[/red] {e}")
        log("\n[bold red]FAILED[/bold red]", "bold red")
        sys.exit(1)

    doc_titles, _ = load_yaml(DOC_TITLES_PATH)
    section_titles, _ = load_yaml(SECTION_TITLES_PATH)

    log(f"doc_titles.yaml:    {len(doc_titles)} entries")
    log(f"section_titles.yaml: {len(section_titles)} entries")

    # ── 2. doc_titles.yaml coverage ──────────────────────────────────────────

    all_doc_ids = collect_all_doc_ids()
    log(f"doc_ids in KB:      {len(all_doc_ids)}")

    missing_ids = [doc_id for doc_id in all_doc_ids if doc_id not in doc_titles]
    if missing_ids:
        for doc_id in sorted(missing_ids):
            errors.append(f"doc_titles.yaml: missing entry for doc_id '{doc_id}'")

    extra_ids = set(doc_titles.keys()) - set(all_doc_ids)
    if extra_ids:
        for doc_id in sorted(extra_ids):
            errors.append(f"doc_titles.yaml: stale entry '{doc_id}' (not found in any _index.yaml or snippet)")

    # ── 3. doc_titles.yaml entries must have "en" key ────────────────────────

    for doc_id, entry in doc_titles.items():
        if not isinstance(entry, dict):
            errors.append(f"doc_titles.yaml[{doc_id}]: expected a mapping, got {type(entry).__name__}")
            continue
        if "en" not in entry:
            errors.append(f"doc_titles.yaml[{doc_id}]: missing required 'en' key")

    # ── 4. section_titles.yaml entries must have at least one non-en key ─────

    for heading, entry in section_titles.items():
        if not isinstance(entry, dict):
            errors.append(f"section_titles.yaml['{heading}']: expected a mapping, got {type(entry).__name__}")
            continue
        non_en_keys = [k for k in entry if k != "en"]
        if not non_en_keys:
            errors.append(f"section_titles.yaml['{heading}']: no non-English translation keys")

    # ── Report ────────────────────────────────────────────────────────────────

    log(f"\n{'=' * 60}")

    if errors:
        log(f"\n[bold red]ERRORS ({len(errors)}):[/bold red]\n")
        for e in errors:
            log(f"  [red]✗[/red] {e}")
        log(f"\n[bold red]FAILED[/bold red]", "bold red")
        sys.exit(1)
    else:
        log(f"\n[bold green]✓ All i18n checks passed.[/bold green]", "bold green")
        log(f"  doc_titles.yaml: {len(doc_titles)}/{len(all_doc_ids)} doc_ids covered")
        log(f"  section_titles.yaml: {len(section_titles)} headings valid")
        log("\n[bold green]PASSED[/bold green]", "bold green")


if __name__ == "__main__":
    main()
