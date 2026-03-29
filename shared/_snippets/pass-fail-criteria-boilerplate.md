---
doc_id: "SHARED-SNIP-PFC-001"
title: "Pass/Fail Criteria Boilerplate"
slug: "pass-fail-criteria-boilerplate"
doc_type: "spec"
phase: "Universal"
checkpoint: "Universal"
checkpoint_name: "Shared Snippet"
version: "1.0.0"
status: "approved"
product_families: [GPU, DC-L6, Automotive, Embedded]
test_stations: [ICT, FCT, DIAG, Universal]
production_stages: [All]
owner_role: "MTE Lead"
created_date: "2026-03-29"
last_updated: "2026-03-29"
rag_chunk_strategy: "by-section"
embedding_priority: "high"
controlled_terms: ["False Fail", "True Fail", "Marginal Fail", Retest, "Test Escape"]
required_sections: []
---

# Pass/Fail Criteria — Standard Boilerplate

> **Type:** Shared Snippet — include in Test Plan and Failure Criteria documents.

## Pass Criteria

A unit **PASSES** a test item when the measured parameter is within the defined specification limits for all test conditions.

## Fail Criteria

A unit **FAILS** a test item when any measured parameter is outside the defined specification limits. Failure must be reproducible on retest to be classified as a **True Fail**.

## Marginal Fail Policy

A unit where the measured parameter falls within ±[X]% of the specification limit is classified as a **Marginal Fail**. Marginal Fails are:
1. Retested once to confirm repeatability
2. Submitted for failure analysis if the failure is repeatable
3. Accepted with engineering disposition if approved by MTE Lead

## False Fail Handling

A unit that fails test but passes on all retests (up to the maximum retest count) is classified as a **False Fail**. The test item responsible for the False Fail must be investigated. If the False Fail rate for any test item exceeds **2%**, a Retest Analysis Report must be initiated.

## Retest Policy

| Condition | Maximum Retests Allowed |
|-----------|------------------------|
| First failure at station | 1 retest |
| Second failure at same item | Escalate to MTE Lead |
| Maximum retests per unit per shift | 2 |

After exhausting retests, units are dispositioned as **True Fail** and routed to repair or FA as appropriate.

## Test Escape Prevention

Any failure mode with known potential to escape to field must be documented in the Escape/Leakage Analysis. Yield targets assume the pass/fail limits defined here. Do not loosen limits to improve yield without MTE Lead and Quality Engineer approval.
