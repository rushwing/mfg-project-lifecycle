---
doc_id: "SHARED-SNIP-UPH-003"
title: "UPH Calculation Method"
slug: "uph-calculation-method"
doc_type: "spec"
phase: "Universal"
checkpoint: "Universal"
checkpoint_name: "Shared Snippet"
version: "1.0.0"
status: "approved"
product_families: [GPU, DC-L6, Automotive, Embedded]
test_stations: [Universal]
owner_role: "MTE Staff"
created_date: "2026-03-29"
last_updated: "2026-03-29"
rag_chunk_strategy: "by-section"
embedding_priority: "medium"
controlled_terms: [UPH, "Cycle Time", "Takt Time", Bottleneck, OEE]
required_sections: []
---

# UPH Calculation Method — Reference

> **Type:** Shared Snippet — include in UPH Study Report and Capacity Planning documents.

## Core Formula

```
UPH = 3600 / Cycle Time (seconds)
Cycle Time (s) = 3600 / UPH
```

## Cycle Time Components

| Component | Description |
|-----------|-------------|
| **Load time** | Time to load DUT into fixture and make contact |
| **Test execution time** | Pure test execution (ICT/FCT/DIAG program runtime) |
| **Unload time** | Time to break contact and unload DUT |
| **Handler/conveyor time** | Transport between stations (if automated) |
| **Station overhead** | SFC upload, log write, station initialization |

**Cycle Time = Load + Test Execution + Unload + Handler + Overhead**

## UPH Measurement Protocol

1. Use a characterized Golden Unit or production unit
2. Run minimum 30 consecutive cycles at steady state (exclude warm-up)
3. Record each cycle time; report mean, min, max, and σ
4. Calculate UPH from mean cycle time
5. Correct for yield: `Effective UPH = UPH × First Pass Yield`

## Takt Time vs. Cycle Time

| Term | Formula | Meaning |
|------|---------|---------|
| **Takt Time** | Available time / Demand | Required rate to meet customer demand |
| **Cycle Time** | Measured per station | Actual rate the station produces |
| **Condition** | Cycle Time ≤ Takt Time | Station is not a bottleneck |
| **Condition** | Cycle Time > Takt Time | Station is the **Bottleneck** |

## OEE Impact on Effective UPH

```
OEE = Availability × Performance × Quality
Effective UPH = Theoretical UPH × OEE
```

Target OEE ≥ 85% for production stations.
