---
doc_id: "SHARED-SNIP-ELD-002"
title: "Escape / Leakage Definition Reference"
slug: "escape-leakage-definition"
doc_type: "spec"
phase: "Universal"
checkpoint: "Universal"
checkpoint_name: "Shared Snippet"
version: "1.0.0"
status: "approved"
product_families: [GPU, DC-L6, Automotive, Embedded]
test_stations: [Universal]
owner_role: "MTE Lead"
created_date: "2026-03-29"
last_updated: "2026-03-29"
rag_chunk_strategy: "by-section"
embedding_priority: "high"
controlled_terms: ["Test Escape", "False Fail", "Coverage Hole", DPM, CAPA]
required_sections: []
---

# Test Escape and Leakage — Reference Definition

> **Type:** Shared Snippet — include in Escape/Leakage Analysis and Test Plan documents.

## Definition

A **Test Escape** (also called **Leakage**) is a defective unit that passes all manufacturing test stations and is shipped to a customer, where it subsequently fails or exhibits abnormal behavior.

Test Escapes are the most critical quality failure mode in manufacturing test. They represent a failure of the test process to fulfill its primary function: preventing defective units from reaching customers.

**Note:** In this KB, "Leakage" is a synonym for Test Escape. Use **Test Escape** as the canonical term in documents.

## Distinction from False Fail

| Term | Unit Condition | Test Result | Outcome |
|------|---------------|-------------|---------|
| **True Fail** | Defective | FAIL | Correctly caught — sent to repair/FA |
| **False Fail** | Non-defective | FAIL | Incorrectly rejected — yield loss |
| **Test Escape** | Defective | PASS | Missed — shipped to customer |

## Measurement

Test Escape rate is measured in **DPPM** (Defective Parts Per Million shipped):

```
DPPM = (Field Returns confirmed as manufacturing defect / Units shipped) × 1,000,000
```

## Root Cause Categories

1. **Coverage Hole** — The defect type has no test coverage at any station
2. **Marginal Coverage** — The defect is tested but the test limit is too loose to catch marginal cases
3. **Test Noise** — High measurement variation causes defective units to sometimes pass
4. **Equipment Malfunction** — Test station hardware failure during test execution
5. **SFC/Flow Error** — Unit bypassed a required test station due to routing error

## Response Requirements

Any confirmed Test Escape must trigger:
- FA to identify the defect mechanism
- CAPA to address the root cause
- Coverage improvement action (tighten limits, add test, or fix DFT)
- Risk assessment of units in field (containment/recall evaluation)
