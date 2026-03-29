---
doc_id: "SHARED-SNIP-GRR-004"
title: "GR&R Acceptance Criteria Reference"
slug: "grr-acceptance-criteria"
doc_type: "spec"
phase: "Universal"
checkpoint: "Universal"
checkpoint_name: "Shared Snippet"
version: "1.0.0"
status: "approved"
product_families: [GPU, DC-L6, Automotive, Embedded]
test_stations: [ICT, FCT]
owner_role: "Quality Engineer"
created_date: "2026-03-29"
last_updated: "2026-03-29"
rag_chunk_strategy: "by-section"
embedding_priority: "high"
controlled_terms: [GR&R, "False Fail", Fixture, "Golden Unit"]
required_sections: []
---

# GR&R Acceptance Criteria — Reference

> **Type:** Shared Snippet — include in GR&R Report and Fixture Qualification Plan.

## Standard Acceptance Thresholds

| %GR&R | Interpretation | Disposition |
|-------|---------------|-------------|
| **< 10%** | Excellent | Measurement system **ACCEPTED** |
| **10% – 30%** | Marginal | May be acceptable depending on application; MTE Lead review required |
| **> 30%** | Unacceptable | Measurement system **REJECTED** — fixture/tester rework required |

> **Default acceptance criterion for NVIDIA GPU/DC-L6/Automotive/Embedded: %GR&R < 10%**

## Study Design (Standard)

| Parameter | Minimum Requirement |
|-----------|-------------------|
| Number of operators | 2 |
| Number of parts (units) | 10 (covering spec range) |
| Number of replications | 2 per operator per part |
| Golden Units included | Yes — min 1 Golden Unit per study |

## Calculation Reference

```
%GR&R = (GR&R Variation / Total Variation) × 100%

where:
  GR&R Variation = √(Repeatability² + Reproducibility²)
  Total Variation = √(GR&R Variation² + Part Variation²)
```

Use ANOVA method (preferred) or X-bar/R method. Document which method was used.

## False Fail Correlation

High %GR&R directly increases False Fail rate. A measurement system with >10% GR&R will cause units near the specification limit to fail inconsistently. Always address GR&R issues before investigating False Fail root causes.

## Corrective Actions for Failed GR&R

Priority order of corrective actions:
1. **Improve fixture contact reliability** (most common root cause)
2. **Reduce measurement noise** (cable routing, grounding, shielding)
3. **Improve operator training/method** (if reproducibility >> repeatability)
4. **Widen specification limits** (requires MTE Lead + Quality Engineer approval and Test Escape risk assessment)
