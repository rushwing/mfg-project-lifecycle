# KB Feature Backlog

Quality methods gap analysis against manufacturing community best practices.
Phase 1 is complete (merged). Phases 2–4 are tracked here.

---

## Phase 1 — Quality Methods Skeleton ✅ Done

| Template | Location | Status |
|----------|----------|--------|
| Process FMEA (PFMEA) — P1-CP2-PFM-006 | p1-concept/cp2 | ✅ Merged |
| SPC Control Chart — MP-CP1-SPC-006 | mp-mass-production/cp1 | ✅ Merged |
| 8D Problem Solving Report — MP-CP3-8DR-006 | mp-mass-production/cp3 | ✅ Merged |
| Process Capability Report (Cpk) — MP-CP4-CPK-006 | mp-mass-production/cp4 | ✅ Merged |

GLOSSARY additions: PFMEA, RPN, SPC, Control Chart, Cpk, 8D

---

## Phase 2 — Test Station Coverage Gaps

### AOI / AXI / 3D SPI (SMT Inspection Stations)

**Why:** GPU/DC-L6 SMT density is high; AOI coverage rate is a standard DVT exit criterion.
These stations are completely absent from `test_stations` enum and no templates exist.

**Tasks:**
- [ ] Add `AOI`, `AXI`, `3D-SPI` to `test_stations` enum in `schemas/template_frontmatter.schema.json` and `schemas/checkpoint_index.schema.json`
- [ ] Add corresponding entries to `production_stages` mapping in `bootstrap_templates.py` (AOI/AXI/3D-SPI → SMT)
- [ ] Add GLOSSARY terms: AOI, AXI, 3D SPI
- [ ] New templates:
  - `EVT-CP2-AOI-006` — AOI / AXI Coverage Plan (EVT-CP2, spec)
  - `DVT-CP2-AOI-007` — AOI / AXI Qualification Report (DVT-CP2, report)

### HALT / HASS (Reliability Testing)

**Why:** Highly Accelerated Life Testing and Stress Screening are standard in DVT/PVT for DC and Automotive. Currently BURN-IN is in the enum but HALT is a distinct methodology.

**Tasks:**
- [ ] Add `HALT`, `HASS` to `test_stations` enum (or handle as a sub-type under SYSTEM)
- [ ] Add GLOSSARY terms: HALT, HASS
- [ ] New templates:
  - `DVT-CP2-HLT-006` — HALT Test Protocol (DVT-CP2, procedure)
  - `PVT-CP3-HSS-006` — HASS Screening Procedure (PVT-CP3, procedure)

---

## Phase 3 — Quality Closure Gaps

### SCAR (Supplier Corrective Action Request)

**Why:** Current MP-CP3 has NCR/MRB (internal) but no SCAR (external, sent to supplier requiring root-cause response). These are distinct documents in supplier quality management.

**Tasks:**
- [ ] Add GLOSSARY term: SCAR
- [ ] New template: `MP-CP3-SCR-007` — SCAR (Supplier Corrective Action Request) (MP-CP3, report)

### Requirements Traceability Matrix (RTM)

**Why:** No formal bidirectional traceability from PRD/MRD requirements → test cases → test results. The test coverage matrices exist but are coverage-by-station, not requirement-by-test-case.

**Tasks:**
- [ ] Add GLOSSARY term: RTM
- [ ] New template: `EVT-CP2-RTM-007` — Requirements Traceability Matrix (EVT-CP2, matrix)
- [ ] Consider `related_docs` links: PRD/MRD → RTM → Test Coverage Matrix

### Yield Learning Curve

**Why:** PVT has yield reports but no formal yield ramp baseline vs. actual comparison. Manufacturing community standard is to define a yield learning curve target (Wright's Law or empirical model) at PVT entry and track against it.

**Tasks:**
- [ ] New template: `PVT-CP1-YLC-006` — Yield Learning Curve Plan (PVT-CP1, plan)

### Component Qualification Plan

**Why:** Critical components (GPU die, HBM, custom ASICs) require supplier qualification plans at EVT-CP1 that are distinct from IQC reports. Currently absent.

**Tasks:**
- [ ] New template: `EVT-CP1-CQP-006` — Component Qualification Plan (EVT-CP1, plan)

---

## Phase 4 — Compliance and Advanced Features

### PPAP / APQP (Automotive)

**Why:** `product_families` includes `Automotive`. PPAP (Production Part Approval Process) is mandatory for automotive customers (IATF 16949). Should be gated on `product_families: [Automotive]`.

**Tasks:**
- [ ] Add GLOSSARY terms: PPAP, APQP, IATF 16949
- [ ] New template: `PVT-CP5-PPA-006` — PPAP Checklist (PVT-CP5, checklist) — Automotive only
- [ ] Consider schema conditional: `if product_families contains Automotive then priority = critical` for PPAP

### MRL Assessment (Manufacturing Readiness Level)

**Why:** MRL (1–10 scale) provides a more structured gate framework than the current checklist-based exit reviews. Increasingly used in high-reliability and DC manufacturing beyond defense.

**Tasks:**
- [ ] Add GLOSSARY term: MRL
- [ ] New template: `PVT-CP5-MRL-007` — Manufacturing Readiness Level Assessment (PVT-CP5, checklist)

### KPI Parameterization Framework

**Why:** Phase gate exit criteria are currently stated as text conditions. A KPI framework would parameterize targets by product family (e.g., DVT exit: yield ≥ 85%, coverage ≥ 92%, GR&R < 10%) stored in `_manifest.yaml` or a dedicated KPI file, enabling automated gate checking by the RAG agent.

**Tasks:**
- [ ] Design KPI schema (phase → checkpoint → metric → target by product_family)
- [ ] Add KPI targets to `{phase}/_manifest.yaml` files
- [ ] Update exit criteria templates to reference KPI targets

### Field Failure → DFT Feedback Closure

**Why:** MP-CP6 has `test-escape-summary` and `npi-feedback-to-design`, but there is no structured mechanism to ensure field escape root causes flow back into the next program's P1 DFT/DFX requirements. The chain breaks at the human handoff.

**Tasks:**
- [ ] Design structured `field_escape_action` frontmatter field (optional) linking a Test Escape to a P1 DFT requirement
- [ ] Update `npi-feedback-to-design-template.md` with structured DFT feedback sections
- [ ] Consider `related_docs` from MP-CP6-TES-003 → P1-CP1-DFT-003 in next program

---

## Structural / Tooling Backlog

| Item | Priority | Notes |
|------|----------|-------|
| `playbook` doc_type has 0 templates outside MP-CP5 | Low | Add playbook templates for HALT operation, fixture maintenance, 8D facilitation |
| `scripts/validate_structure.py`: check PFMEA → Control Plan `related_docs` chain | Low | Enforce the upstream dependency at CI level |
| `docs/agentic-rag-inference.md`: add PFMEA table chunking guidance | Low | PFMEA tables are large; `by-table` strategy may need row-level chunking |
| Vietnamese (vi) support | Low | Replace all `(pending)` stubs in GLOSSARY.md and i18n/ files |
