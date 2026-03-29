#!/usr/bin/env python3
"""
generate_doc_index.py

Walks all *-template.md files, reads frontmatter, and generates
DOC_INDEX.md — a human-readable + RAG-queryable document registry.

Usage:
    cd <repo_root>
    python scripts/generate_doc_index.py [--output PATH]

The output file is DOC_INDEX.md at repo root by default.
"""

import argparse
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

import frontmatter

try:
    from rich.console import Console
    USE_RICH = True
except ImportError:
    USE_RICH = False

ROOT = Path(__file__).parent.parent
DEFAULT_OUTPUT = ROOT / "DOC_INDEX.md"
PHASE_ORDER = ["P1", "EVT", "DVT", "PVT", "MP", "Universal"]
console = Console() if USE_RICH else None


def log(msg: str, style: str = "") -> None:
    if USE_RICH and console:
        console.print(msg, style=style)
    else:
        print(msg)


def find_templates() -> list[Path]:
    results = set(ROOT.rglob("*-template.md"))
    snippets_dir = ROOT / "shared" / "_snippets"
    if snippets_dir.exists():
        results |= set(snippets_dir.glob("*.md"))
    return sorted(results)


def load_template_metadata(templates: list[Path]) -> list[dict]:
    """Load frontmatter from all templates, add file path info."""
    docs = []
    for t in templates:
        try:
            post = frontmatter.load(str(t))
            meta = dict(post.metadata)
            meta["_file"] = str(t.relative_to(ROOT))
            docs.append(meta)
        except Exception as e:
            log(f"[yellow]WARN[/yellow] Could not parse {t.relative_to(ROOT)}: {e}")
    return docs


def group_docs(docs: list[dict]) -> dict:
    """Group documents by phase → checkpoint."""
    grouped = defaultdict(lambda: defaultdict(list))
    for doc in docs:
        phase = doc.get("phase", "UNKNOWN")
        checkpoint = doc.get("checkpoint", "UNKNOWN")
        checkpoint_name = doc.get("checkpoint_name", "")
        grouped[phase][(checkpoint, checkpoint_name)].append(doc)
    return grouped


def doc_type_badge(doc_type: str) -> str:
    badges = {
        "plan": "📋",
        "spec": "📐",
        "report": "📊",
        "checklist": "✅",
        "tracker": "🔍",
        "matrix": "🗃️",
        "log": "📝",
        "analysis": "🔬",
        "procedure": "📖",
        "playbook": "🎯",
    }
    return badges.get(doc_type, "📄")


def priority_badge(priority: str) -> str:
    badges = {
        "critical": "🔴",
        "required": "🟠",
        "recommended": "🟡",
        "optional": "🔵",
    }
    return badges.get(priority or "", "⚪")


def generate_markdown(grouped: dict, total: int) -> str:
    lines = [
        "# Document Index",
        "",
        "> **Auto-generated** by `scripts/generate_doc_index.py`. Do not edit manually.",
        f"> Last updated: {date.today().isoformat()}  ",
        f"> Total templates: {total}",
        "",
        "## Legend",
        "",
        "| Symbol | Meaning |",
        "|--------|---------|",
        "| 🔴 Critical | Required for phase gate exit |",
        "| 🟠 Required | Must exist before phase ends |",
        "| 🟡 Recommended | Strong recommendation |",
        "| 🔵 Optional | Situational use |",
        "| 📋 plan | Planning document |",
        "| 📐 spec | Specification |",
        "| 📊 report | Report/analysis |",
        "| ✅ checklist | Checklist |",
        "| 🗃️ matrix | Matrix/table |",
        "",
        "---",
        "",
    ]

    for phase in PHASE_ORDER:
        if phase not in grouped:
            continue

        phase_docs = grouped[phase]
        phase_total = sum(len(docs) for docs in phase_docs.values())
        phase_label = "Shared Snippets" if phase == "Universal" else phase
        lines.append(f"## {phase_label} — {phase_total} documents")
        lines.append("")

        for (checkpoint, checkpoint_name), docs in sorted(phase_docs.items()):
            if phase == "Universal":
                lines.append(f"### {checkpoint_name}")
            else:
                lines.append(f"### {phase} {checkpoint}: {checkpoint_name}")
            lines.append("")
            lines.append("| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |")
            lines.append("|--------|-------|------|----------|-------|-------------|--------|")

            for doc in sorted(docs, key=lambda d: d.get("doc_id", "")):
                doc_id = doc.get("doc_id", "—")
                title = doc.get("title", "—")
                doc_type = doc.get("doc_type", "—")
                priority = doc.get("priority", doc.get("embedding_priority", "—"))
                owner = doc.get("owner_role", "—")
                rag = doc.get("rag_chunk_strategy", "—")
                status = doc.get("status", "—")
                file_path = doc.get("_file", "")

                type_icon = doc_type_badge(doc_type)
                priority_icon = priority_badge(priority)

                title_link = f"[{title}]({file_path})" if file_path else title
                lines.append(
                    f"| `{doc_id}` | {title_link} | {type_icon} {doc_type} | "
                    f"{priority_icon} {priority} | {owner} | {rag} | {status} |"
                )

            lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate DOC_INDEX.md from template frontmatter")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output file path")
    args = parser.parse_args()

    log("\n[bold]Doc Index Generator[/bold]")

    templates = find_templates()
    log(f"Found {len(templates)} template files")

    docs = load_template_metadata(templates)
    log(f"Loaded {len(docs)} document metadata records")

    grouped = group_docs(docs)
    markdown = generate_markdown(grouped, len(docs))

    output_path = Path(args.output)
    output_path.write_text(markdown, encoding="utf-8")
    try:
        display_path = output_path.relative_to(ROOT)
    except ValueError:
        display_path = output_path
    log(f"\n[green]✓ DOC_INDEX.md written to {display_path}[/green]")
    log(f"  Total documents indexed: {len(docs)}")


if __name__ == "__main__":
    main()
