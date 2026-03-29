---
doc_id: "SHARED-SNIP-DFT-005"
title: "DFT Coverage Table Template"
slug: "dft-coverage-table-template"
doc_type: "matrix"
phase: "Universal"
checkpoint: "Universal"
checkpoint_name: "Shared Snippet"
version: "1.0.0"
status: "approved"
product_families: [GPU, DC-L6, Automotive, Embedded]
test_stations: [ICT, FCT, DIAG, Universal]
owner_role: "MTE Lead"
created_date: "2026-03-29"
last_updated: "2026-03-29"
rag_chunk_strategy: "by-table"
embedding_priority: "high"
controlled_terms: [DFT, BIST, "Boundary Scan", ICT, FCT, DIAG, "Coverage Hole"]
required_sections: []
---

# DFT Coverage Table — Standard Template

> **Type:** Shared Snippet — use in Test Coverage Matrix documents.
>
> **RAG note:** This table structure is the canonical format for coverage matrices in this KB.
> Chunk this content at the table level.

## Coverage Matrix Format

| Functional Block | ICT | BScan | FCT | DIAG/BIST | ATE | Coverage % | Coverage Hole? | DFT Hook Required |
|-----------------|-----|-------|-----|-----------|-----|-----------|---------------|------------------|
| Power Delivery | ✓ | — | ✓ | ✓ | — | 95% | No | — |
| PCIe Interface | — | ✓ | ✓ | ✓ | — | 85% | Partial | LTSSM BIST |
| HBM Stack | — | — | — | ✓ | ✓ | 90% | No | HBM BIST |
| NVLink | — | ✓ | ✓ | ✓ | — | 80% | Yes | Add PRBS test |
| Thermal / Fan | — | — | ✓ | ✓ | — | 70% | Partial | Temp sensor access |
| VBIOS / FW | — | — | ✓ | ✓ | — | 95% | No | — |

**Legend:**
- ✓ = Covered
- Partial = Partial coverage (document gap)
- — = Not tested at this station

## Instructions for Use

1. List all functional blocks in the first column
2. Mark each station with ✓ if that block is tested at that station
3. Estimate coverage % based on test items vs. total fault universe for that block
4. Flag Coverage Holes with "Yes" — each must be dispositioned in Test Gap Analysis
5. Note required DFT hooks for uncovered areas — feed to DFT Requirements doc

## Coverage Targets by Phase

| Phase | Minimum Coverage Target |
|-------|------------------------|
| EVT | ≥ 80% documented |
| DVT | ≥ 90% achieved |
| PVT/MP | ≥ 92% with all holes dispositioned |
