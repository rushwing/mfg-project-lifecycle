# Document Index

> **Auto-generated** by `scripts/generate_doc_index.py`. Do not edit manually.
> Last updated: 2026-03-30  
> Total templates: 136

## Legend

| Symbol | Meaning |
|--------|---------|
| 🔴 Critical | Required for phase gate exit |
| 🟠 Required | Must exist before phase ends |
| 🟡 Recommended | Strong recommendation |
| 🔵 Optional | Situational use |
| 📋 plan | Planning document |
| 📐 spec | Specification |
| 📊 report | Report/analysis |
| ✅ checklist | Checklist |
| 🗃️ matrix | Matrix/table |

---

## P1 — 20 documents

### P1 CP1: Requirements Clarification and Testability Input

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `P1-CP1-DFT-003` | [DFT / DFX Requirement](p1-concept/cp1-requirements-clarity/dft-dfx-requirement-template.md) | 📐 spec | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `P1-CP1-HWS-002` | [HW Spec / System Spec (Testability Annotations)](p1-concept/cp1-requirements-clarity/hw-spec-system-spec-template.md) | 📐 spec | 🟠 required | MTE Lead | by-section · medium | template-stub |
| `P1-CP1-PMR-001` | [PRD / MRD (Manufacturing Testability Review)](p1-concept/cp1-requirements-clarity/prd-mrd-template.md) | 📐 spec | 🟠 required | MTE Lead | by-section · medium | template-stub |
| `P1-CP1-RSK-005` | [Risk List / Open Issue List](p1-concept/cp1-requirements-clarity/risk-list-open-issue-template.md) | 🔍 tracker | 🟠 required | MTE Lead | by-table · medium | template-stub |
| `P1-CP1-TSO-004` | [Test Strategy Overview](p1-concept/cp1-requirements-clarity/test-strategy-overview-template.md) | 📋 plan | 🔴 critical | MTE Lead | by-section · high | template-stub |

### P1 CP2: Test Architecture and Station Planning

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `P1-CP2-CAP-005` | [Capacity Planning Draft / UPH Estimation Draft](p1-concept/cp2-test-architecture-planning/capacity-planning-uph-draft-template.md) | 🔬 analysis | 🟡 recommended | MTE Staff | by-section · medium | template-stub |
| `P1-CP2-SFD-002` | [Station Flow Diagram / Test Flow Diagram](p1-concept/cp2-test-architecture-planning/station-flow-diagram-template.md) | 📐 spec | 🔴 critical | MTE Staff | by-section · high | template-stub |
| `P1-CP2-TAS-001` | [MFG Test Architecture Spec](p1-concept/cp2-test-architecture-planning/mfg-test-architecture-spec-template.md) | 📐 spec | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `P1-CP2-TCM-003` | [High-Level Test Coverage Matrix](p1-concept/cp2-test-architecture-planning/test-coverage-matrix-hl-template.md) | 🗃️ matrix | 🟠 required | MTE Lead | by-table · high | template-stub |
| `P1-CP2-TEL-004` | [Test Equipment List](p1-concept/cp2-test-architecture-planning/test-equipment-list-template.md) | 🔍 tracker | 🟠 required | MTE Staff | by-table · medium | template-stub |

### P1 CP3: Fixture / Equipment / Vendor Pre-Evaluation

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `P1-CP3-CAP-005` | [CAPEX Budget Draft](p1-concept/cp3-fixture-equipment-vendor/capex-budget-draft-template.md) | 📋 plan | 🟠 required | MTE Manager | by-table · medium | template-stub |
| `P1-CP3-ERS-002` | [Equipment Requirement Spec (ERS)](p1-concept/cp3-fixture-equipment-vendor/equipment-requirement-spec-template.md) | 📐 spec | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `P1-CP3-FCP-001` | [Fixture Concept Proposal](p1-concept/cp3-fixture-equipment-vendor/fixture-concept-proposal-template.md) | 📐 spec | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `P1-CP3-FFR-004` | [Fixture Feasibility Review Notes](p1-concept/cp3-fixture-equipment-vendor/fixture-feasibility-review-template.md) | 📊 report | 🟠 required | MTE Lead | by-section · medium | template-stub |
| `P1-CP3-RFQ-003` | [Vendor RFQ / Vendor Selection Criteria](p1-concept/cp3-fixture-equipment-vendor/vendor-rfq-selection-criteria-template.md) | 🔍 tracker | 🟠 required | MTE Staff | by-section · medium | template-stub |

### P1 CP4: Program Mechanics Establishment

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `P1-CP4-BOD-002` | [BOD / EOD Template](p1-concept/cp4-program-mechanics/bod-eod-template.md) | 📋 plan | 🟠 required | MTE Staff | by-section · medium | template-stub |
| `P1-CP4-NBP-001` | [NPI Build Plan (Initial)](p1-concept/cp4-program-mechanics/npi-build-plan-template.md) | 📋 plan | 🔴 critical | NPI PM | by-section · high | template-stub |
| `P1-CP4-PMT-005` | [Program Milestone Tracker](p1-concept/cp4-program-mechanics/program-milestone-tracker-template.md) | 🔍 tracker | 🟠 required | NPI PM | by-table · medium | template-stub |
| `P1-CP4-RAI-003` | [RAID Log (Risk / Action / Issue / Dependency)](p1-concept/cp4-program-mechanics/raid-log-template.md) | 🔍 tracker | 🔴 critical | MTE Lead | by-table · high | template-stub |
| `P1-CP4-VCP-004` | [Version Control Plan (HW / SW / Test)](p1-concept/cp4-program-mechanics/version-control-plan-template.md) | 📋 plan | 🟠 required | MTE Lead | by-section · medium | template-stub |

## EVT — 25 documents

### EVT CP1: Sample Receipt and Basic Bring-Up

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `EVT-CP1-BBC-002` | [Board Bring-Up Checklist](evt-engineering-validation/cp1-bringup-test-readiness/board-bringup-checklist-template.md) | ✅ checklist | 🔴 critical | MTE Staff | by-section · high | template-stub |
| `EVT-CP1-EBP-001` | [EVT Build Plan](evt-engineering-validation/cp1-bringup-test-readiness/evt-build-plan-template.md) | 📋 plan | 🔴 critical | NPI PM | by-section · high | template-stub |
| `EVT-CP1-GSD-004` | [Golden Sample Definition](evt-engineering-validation/cp1-bringup-test-readiness/golden-sample-definition-template.md) | 📐 spec | 🟠 required | MTE Lead | by-section · high | template-stub |
| `EVT-CP1-TRC-003` | [Test Readiness Checklist](evt-engineering-validation/cp1-bringup-test-readiness/test-readiness-checklist-template.md) | ✅ checklist | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `EVT-CP1-VXM-005` | [HW / SW / FW Version Matrix](evt-engineering-validation/cp1-bringup-test-readiness/hw-sw-fw-version-matrix-template.md) | 🔍 tracker | 🟠 required | MTE Staff | by-table · medium | template-stub |

### EVT CP2: Test Requirements Freeze and Plan Elaboration

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `EVT-CP2-FCP-004` | [Failure Criteria / Pass-Fail Criteria](evt-engineering-validation/cp2-test-requirements-freeze/failure-criteria-pass-fail-template.md) | 📐 spec | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `EVT-CP2-TCL-005` | [Test Case List / Test Item Spec](evt-engineering-validation/cp2-test-requirements-freeze/test-case-list-item-spec-template.md) | 📐 spec | 🟠 required | MTE Staff | by-table · high | template-stub |
| `EVT-CP2-TCM-003` | [Test Coverage Matrix (Detailed)](evt-engineering-validation/cp2-test-requirements-freeze/test-coverage-matrix-detailed-template.md) | 🗃️ matrix | 🔴 critical | MTE Staff | by-table · high | template-stub |
| `EVT-CP2-TCP-002` | [Test Plan (ICT / FCT / DIAG)](evt-engineering-validation/cp2-test-requirements-freeze/test-plan-ict-fct-diag-template.md) | 📋 plan | 🔴 critical | MTE Staff | by-section · high | template-stub |
| `EVT-CP2-TRP-001` | [TRP (Test Requirement Plan / Test Readiness Plan)](evt-engineering-validation/cp2-test-requirements-freeze/trp-test-readiness-plan-template.md) | 📋 plan | 🔴 critical | MTE Lead | by-section · high | template-stub |

### EVT CP3: Test Framework Integration and Initial Program Development

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `EVT-CP3-DDP-003` | [DIAG Development Plan](evt-engineering-validation/cp3-framework-sw-development/diag-development-plan-template.md) | 📋 plan | 🔴 critical | MTE Staff | by-section · high | template-stub |
| `EVT-CP3-LTS-004` | [Logging and Traceability Spec](evt-engineering-validation/cp3-framework-sw-development/logging-traceability-spec-template.md) | 📐 spec | 🟠 required | MTE Staff | by-section · high | template-stub |
| `EVT-CP3-SFR-005` | [SFC Interface Requirement](evt-engineering-validation/cp3-framework-sw-development/sfc-interface-requirement-template.md) | 📐 spec | 🟠 required | MTE Lead | by-section · high | template-stub |
| `EVT-CP3-SWA-002` | [SW Architecture for MFG Test](evt-engineering-validation/cp3-framework-sw-development/sw-architecture-mfg-test-template.md) | 📐 spec | 🟠 required | MTE Staff | by-section · high | template-stub |
| `EVT-CP3-TFI-001` | [Test Framework Integration Plan](evt-engineering-validation/cp3-framework-sw-development/test-framework-integration-plan-template.md) | 📋 plan | 🔴 critical | MTE Staff | by-section · high | template-stub |

### EVT CP4: Fixture Prototype and Equipment Bring-Up

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `EVT-CP4-ESI-004` | [Equipment Setup Instruction](evt-engineering-validation/cp4-fixture-equipment-debug/equipment-setup-instruction-template.md) | 📖 procedure | 🟠 required | MTE Staff | by-section · medium | template-stub |
| `EVT-CP4-FBM-002` | [Fixture BOM](evt-engineering-validation/cp4-fixture-equipment-debug/fixture-bom-template.md) | 🔍 tracker | 🟠 required | MTE Staff | by-table · medium | template-stub |
| `EVT-CP4-FDR-003` | [Fixture Debug Report](evt-engineering-validation/cp4-fixture-equipment-debug/fixture-debug-report-template.md) | 📊 report | 🔴 critical | MTE Staff | by-section · high | template-stub |
| `EVT-CP4-FDS-001` | [Fixture Design Spec](evt-engineering-validation/cp4-fixture-equipment-debug/fixture-design-spec-template.md) | 📐 spec | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `EVT-CP4-VAT-005` | [Vendor Action Tracker](evt-engineering-validation/cp4-fixture-equipment-debug/vendor-action-tracker-template.md) | 🔍 tracker | 🟠 required | MTE Lead | by-table · medium | template-stub |

### EVT CP5: Issue Management and Phase Summary

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `EVT-CP5-DBR-001` | [EVT Daily Build Report](evt-engineering-validation/cp5-issue-mgmt-phase-summary/evt-daily-build-report-template.md) | 📊 report | 🟠 required | MTE Staff | by-section · medium | template-stub |
| `EVT-CP5-DTL-002` | [Defect Tracking List / Bug List](evt-engineering-validation/cp5-issue-mgmt-phase-summary/defect-tracking-list-template.md) | 🔍 tracker | 🔴 critical | MTE Staff | by-table · high | template-stub |
| `EVT-CP5-ECR-004` | [EVT Exit Criteria Review](evt-engineering-validation/cp5-issue-mgmt-phase-summary/evt-exit-criteria-review-template.md) | ✅ checklist | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `EVT-CP5-EPR-005` | [EVT Phase Summary Report](evt-engineering-validation/cp5-issue-mgmt-phase-summary/evt-phase-summary-report-template.md) | 📊 report | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `EVT-CP5-RCA-003` | [Root Cause Analysis Report (Initial)](evt-engineering-validation/cp5-issue-mgmt-phase-summary/root-cause-analysis-report-template.md) | 📊 report | 🟠 required | MTE Lead | by-section · high | template-stub |

## DVT — 29 documents

### DVT CP1: Test Completeness Improvement

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `DVT-CP1-DBP-001` | [DVT Build Plan](dvt-design-validation/cp1-test-completeness/dvt-build-plan-template.md) | 📋 plan | 🔴 critical | NPI PM | by-section · high | template-stub |
| `DVT-CP1-DCR-003` | [Detailed Coverage Report](dvt-design-validation/cp1-test-completeness/detailed-coverage-report-template.md) | 📊 report | 🔴 critical | MTE Staff | by-table · high | template-stub |
| `DVT-CP1-DEP-005` | [Diagnostic Enhancement Plan](dvt-design-validation/cp1-test-completeness/diagnostic-enhancement-plan-template.md) | 📋 plan | 🟠 required | MTE Staff | by-section · high | template-stub |
| `DVT-CP1-TGA-004` | [Test Gap Analysis](dvt-design-validation/cp1-test-completeness/test-gap-analysis-template.md) | 🔬 analysis | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `DVT-CP1-TRP-002` | [Updated TRP / Test Plan](dvt-design-validation/cp1-test-completeness/updated-trp-test-plan-template.md) | 📋 plan | 🔴 critical | MTE Lead | by-section · high | template-stub |

### DVT CP2: Fixture Qualification and Repeatability Verification

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `DVT-CP2-ECP-004` | [Equipment Calibration Plan](dvt-design-validation/cp2-fixture-qualification/equipment-calibration-plan-template.md) | 📋 plan | 🟠 required | MTE Staff | by-table · medium | template-stub |
| `DVT-CP2-FAR-003` | [Fixture Acceptance Report](dvt-design-validation/cp2-fixture-qualification/fixture-acceptance-report-template.md) | 📊 report | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `DVT-CP2-FQP-001` | [Fixture Qualification Plan](dvt-design-validation/cp2-fixture-qualification/fixture-qualification-plan-template.md) | 📋 plan | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `DVT-CP2-GRR-002` | [GR&R Report (Gauge R&R)](dvt-design-validation/cp2-fixture-qualification/grr-report-template.md) | 📊 report | 🔴 critical | Quality Engineer | by-section · high | template-stub |
| `DVT-CP2-PMP-005` | [Preventive Maintenance Plan](dvt-design-validation/cp2-fixture-qualification/preventive-maintenance-plan-template.md) | 📋 plan | 🟠 required | MTE Staff | by-table · medium | template-stub |

### DVT CP3: Software Version Management and Releasability

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `DVT-CP3-CCM-003` | [Configuration Control Matrix](dvt-design-validation/cp3-sw-version-releasability/configuration-control-matrix-template.md) | 🗃️ matrix | 🟠 required | MTE Staff | by-table · medium | template-stub |
| `DVT-CP3-EIA-005` | [ECO / ECN Impact Assessment](dvt-design-validation/cp3-sw-version-releasability/eco-ecn-impact-assessment-template.md) | 🔬 analysis | 🟠 required | MTE Lead | by-section · high | template-stub |
| `DVT-CP3-RNT-001` | [Release Note (Test SW / FW / DIAG)](dvt-design-validation/cp3-sw-version-releasability/release-note-test-sw-fw-diag-template.md) | 📝 log | 🔴 critical | MTE Staff | by-section · high | template-stub |
| `DVT-CP3-SCL-004` | [Software Change Log](dvt-design-validation/cp3-sw-version-releasability/software-change-log-template.md) | 📝 log | 🟠 required | MTE Staff | by-table · medium | template-stub |
| `DVT-CP3-VRP-002` | [Version Release Plan](dvt-design-validation/cp3-sw-version-releasability/version-release-plan-template.md) | 📋 plan | 🟠 required | MTE Lead | by-section · high | template-stub |

### DVT CP4: UPH and Capacity Assessment

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `DVT-CP4-BOT-005` | [Bottleneck Analysis Report](dvt-design-validation/cp4-uph-capacity/bottleneck-analysis-report-template.md) | 📊 report | 🟠 required | MTE Lead | by-section · high | template-stub |
| `DVT-CP4-CTB-002` | [Cycle Time Breakdown](dvt-design-validation/cp4-uph-capacity/cycle-time-breakdown-template.md) | 🔬 analysis | 🔴 critical | MTE Staff | by-table · high | template-stub |
| `DVT-CP4-HMP-004` | [Headcount / Machine Planning Sheet](dvt-design-validation/cp4-uph-capacity/headcount-machine-planning-template.md) | 📋 plan | 🟠 required | MTE Manager | by-table · medium | template-stub |
| `DVT-CP4-SLA-003` | [Station Loading Analysis](dvt-design-validation/cp4-uph-capacity/station-loading-analysis-template.md) | 🔬 analysis | 🟠 required | MTE Lead | by-section · high | template-stub |
| `DVT-CP4-UPH-001` | [UPH Study Report](dvt-design-validation/cp4-uph-capacity/uph-study-report-template.md) | 📊 report | 🔴 critical | MTE Staff | by-section · high | template-stub |

### DVT CP5: Failure Analysis and Yield Improvement

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `DVT-CP5-CAP-005` | [CAPA (Corrective Action and Preventive Action)](dvt-design-validation/cp5-failure-analysis-yield/capa-corrective-action-plan-template.md) | 📊 report | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `DVT-CP5-FAR-001` | [FA Request / FA Report](dvt-design-validation/cp5-failure-analysis-yield/fa-request-report-template.md) | 📊 report | 🔴 critical | MTE Staff | by-section · high | template-stub |
| `DVT-CP5-PAR-002` | [Pareto Report](dvt-design-validation/cp5-failure-analysis-yield/pareto-report-template.md) | 📊 report | 🔴 critical | MTE Staff | by-section · high | template-stub |
| `DVT-CP5-RTA-004` | [Retest Analysis Report](dvt-design-validation/cp5-failure-analysis-yield/retest-analysis-report-template.md) | 📊 report | 🟠 required | MTE Staff | by-section · high | template-stub |
| `DVT-CP5-YTR-003` | [Yield Trend Report](dvt-design-validation/cp5-failure-analysis-yield/yield-trend-report-template.md) | 📊 report | 🔴 critical | MTE Staff | by-table · high | template-stub |

### DVT CP6: Phase Exit Review

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `DVT-CP6-DEC-001` | [DVT Exit Criteria Checklist](dvt-design-validation/cp6-exit-review/dvt-exit-criteria-checklist-template.md) | ✅ checklist | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `DVT-CP6-DSR-003` | [DVT Summary Report](dvt-design-validation/cp6-exit-review/dvt-summary-report-template.md) | 📊 report | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `DVT-CP6-OIC-002` | [Open Issue Closure Plan](dvt-design-validation/cp6-exit-review/open-issue-closure-plan-template.md) | 🔍 tracker | 🔴 critical | MTE Lead | by-table · high | template-stub |
| `DVT-CP6-PRD-004` | [PVT Readiness Review Deck](dvt-design-validation/cp6-exit-review/pvt-readiness-review-deck-template.md) | 📊 report | 🔴 critical | MTE Lead | by-section · high | template-stub |

## PVT — 28 documents

### PVT CP1: Mass Production Flow Validation

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `PVT-CP1-LQP-005` | [Line Qualification Plan](pvt-production-validation/cp1-mp-process-validation/line-qualification-plan-template.md) | 📋 plan | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `PVT-CP1-MTF-002` | [Mass Production Test Flow](pvt-production-validation/cp1-mp-process-validation/mp-test-flow-template.md) | 📐 spec | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `PVT-CP1-OTM-004` | [Operator Training Material](pvt-production-validation/cp1-mp-process-validation/operator-training-material-template.md) | 📖 procedure | 🟠 required | MTE Staff | by-section · medium | template-stub |
| `PVT-CP1-PBP-001` | [PVT Build Plan](pvt-production-validation/cp1-mp-process-validation/pvt-build-plan-template.md) | 📋 plan | 🔴 critical | NPI PM | by-section · high | template-stub |
| `PVT-CP1-SOP-003` | [SOP / WI (Work Instruction)](pvt-production-validation/cp1-mp-process-validation/sop-wi-work-instruction-template.md) | 📖 procedure | 🔴 critical | MTE Staff | by-section · high | template-stub |

### PVT CP2: Factory Line Bring-Up and Station Qualification

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `PVT-CP2-LBC-001` | [Line Bring-Up Checklist](pvt-production-validation/cp2-factory-bringup-station/line-bringup-checklist-template.md) | ✅ checklist | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `PVT-CP2-PSC-005` | [Production Sign-Off Checklist](pvt-production-validation/cp2-factory-bringup-station/production-sign-off-checklist-template.md) | ✅ checklist | 🔴 critical | MTE Manager | by-section · high | template-stub |
| `PVT-CP2-SRC-002` | [Site Readiness Checklist](pvt-production-validation/cp2-factory-bringup-station/site-readiness-checklist-template.md) | ✅ checklist | 🔴 critical | Factory Ops | by-section · high | template-stub |
| `PVT-CP2-TIQ-003` | [Tester Installation Qualification (IQ)](pvt-production-validation/cp2-factory-bringup-station/tester-iq-installation-qualification-template.md) | ✅ checklist | 🔴 critical | MTE Staff | by-section · high | template-stub |
| `PVT-CP2-TOQ-004` | [Tester Operational Qualification (OQ)](pvt-production-validation/cp2-factory-bringup-station/tester-oq-operational-qualification-template.md) | 📊 report | 🔴 critical | MTE Staff | by-section · high | template-stub |

### PVT CP3: Yield / Efficiency / Stability Validation

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `PVT-CP3-DTR-003` | [Downtime Report](pvt-production-validation/cp3-yield-efficiency-stability/downtime-report-template.md) | 📊 report | 🟠 required | MTE Staff | by-section · medium | template-stub |
| `PVT-CP3-ELA-004` | [Escape / Leakage Analysis](pvt-production-validation/cp3-yield-efficiency-stability/escape-leakage-analysis-template.md) | 🔬 analysis | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `PVT-CP3-FFR-005` | [False Fail / Retest Reduction Report](pvt-production-validation/cp3-yield-efficiency-stability/false-fail-retest-reduction-report-template.md) | 📊 report | 🟠 required | MTE Staff | by-section · high | template-stub |
| `PVT-CP3-PYR-001` | [PVT Yield Report](pvt-production-validation/cp3-yield-efficiency-stability/pvt-yield-report-template.md) | 📊 report | 🔴 critical | MTE Staff | by-section · high | template-stub |
| `PVT-CP3-UPH-002` | [UPH Validation Report](pvt-production-validation/cp3-yield-efficiency-stability/uph-validation-report-template.md) | 📊 report | 🔴 critical | MTE Staff | by-section · high | template-stub |

### PVT CP4: SFC / Traceability / Data Closure

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `PVT-CP4-DUV-003` | [Data Upload Validation Report](pvt-production-validation/cp4-sfc-traceability-data/data-upload-validation-report-template.md) | 📊 report | 🟠 required | MTE Staff | by-section · medium | template-stub |
| `PVT-CP4-RWF-005` | [Repair / Rework Flow Spec](pvt-production-validation/cp4-sfc-traceability-data/repair-rework-flow-spec-template.md) | 📐 spec | 🟠 required | MTE Lead | by-section · high | template-stub |
| `PVT-CP4-SNC-004` | [Serial Number Control Plan](pvt-production-validation/cp4-sfc-traceability-data/serial-number-control-plan-template.md) | 📋 plan | 🟠 required | Factory Ops | by-section · medium | template-stub |
| `PVT-CP4-SVR-001` | [SFC Validation Report](pvt-production-validation/cp4-sfc-traceability-data/sfc-validation-report-template.md) | 📊 report | 🔴 critical | MTE Staff | by-section · high | template-stub |
| `PVT-CP4-TMD-002` | [Traceability Mapping Document](pvt-production-validation/cp4-sfc-traceability-data/traceability-mapping-document-template.md) | 📐 spec | 🔴 critical | MTE Lead | by-section · high | template-stub |

### PVT CP5: Mass Production Sign-Off

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `PVT-CP5-CEP-004` | [Contingency / Escalation Plan](pvt-production-validation/cp5-mp-sign-off/contingency-escalation-plan-template.md) | 📋 plan | 🟠 required | MTE Manager | by-section · medium | template-stub |
| `PVT-CP5-CTP-003` | [Control Plan](pvt-production-validation/cp5-mp-sign-off/control-plan-template.md) | 📋 plan | 🔴 critical | Quality Engineer | by-table · high | template-stub |
| `PVT-CP5-HPF-005` | [Handover Package to Factory Ops](pvt-production-validation/cp5-mp-sign-off/handover-package-factory-ops-template.md) | 📋 plan | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `PVT-CP5-MPR-002` | [MP Release Recommendation](pvt-production-validation/cp5-mp-sign-off/mp-release-recommendation-template.md) | 📋 plan | 🔴 critical | MTE Manager | by-section · high | template-stub |
| `PVT-CP5-PER-001` | [PVT Exit Report](pvt-production-validation/cp5-mp-sign-off/pvt-exit-report-template.md) | 📊 report | 🔴 critical | MTE Lead | by-section · high | template-stub |

### PVT CP6: Phase Retrospective

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `PVT-CP6-OIT-002` | [Open Issues for MP Tracker](pvt-production-validation/cp6-retrospective/open-issues-mp-tracker-template.md) | 🔍 tracker | 🟠 required | MTE Lead | by-table · medium | template-stub |
| `PVT-CP6-PLL-001` | [PVT Lessons Learned](pvt-production-validation/cp6-retrospective/pvt-lessons-learned-template.md) | 📊 report | 🟠 required | MTE Lead | by-section · high | template-stub |
| `PVT-CP6-PRN-003` | [Phase Retrospective Notes](pvt-production-validation/cp6-retrospective/phase-retrospective-notes-template.md) | 📝 log | 🟡 recommended | NPI PM | by-section · medium | template-stub |

## MP — 29 documents

### MP CP1: Daily Production Operations

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `MP-CP1-BOD-002` | [BOD / EOD Report](mp-mass-production/cp1-daily-operations/bod-eod-report-template.md) | 📊 report | 🟠 required | MTE Staff | by-section · medium | template-stub |
| `MP-CP1-DEL-005` | [Downtime / Escalation Log](mp-mass-production/cp1-daily-operations/downtime-escalation-log-template.md) | 📝 log | 🟠 required | Factory Ops | by-table · medium | template-stub |
| `MP-CP1-DPR-001` | [Daily Production Report](mp-mass-production/cp1-daily-operations/daily-production-report-template.md) | 📊 report | 🔴 critical | Factory Ops | by-section · medium | template-stub |
| `MP-CP1-WIO-003` | [WIP / Input-Output Report](mp-mass-production/cp1-daily-operations/wip-io-report-template.md) | 📊 report | 🟠 required | Factory Ops | by-table · medium | template-stub |
| `MP-CP1-YDB-004` | [Yield Dashboard](mp-mass-production/cp1-daily-operations/yield-dashboard-template.md) | 📊 report | 🟠 required | MTE Staff | by-table · high | template-stub |

### MP CP2: Version and Change Management

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `MP-CP2-CML-002` | [Change Management Log](mp-mass-production/cp2-version-change-mgmt/change-management-log-template.md) | 📝 log | 🔴 critical | MTE Lead | by-table · high | template-stub |
| `MP-CP2-EIT-003` | [ECO / ECN Implementation Tracker](mp-mass-production/cp2-version-change-mgmt/eco-ecn-implementation-tracker-template.md) | 🔍 tracker | 🟠 required | MTE Lead | by-table · medium | template-stub |
| `MP-CP2-GUM-005` | [Golden Unit Maintenance Record](mp-mass-production/cp2-version-change-mgmt/golden-unit-maintenance-record-template.md) | 📝 log | 🟠 required | MTE Staff | by-table · medium | template-stub |
| `MP-CP2-MRN-001` | [MP Release Note](mp-mass-production/cp2-version-change-mgmt/mp-release-note-template.md) | 📝 log | 🔴 critical | MTE Staff | by-section · high | template-stub |
| `MP-CP2-TPR-004` | [Test Program Revision History](mp-mass-production/cp2-version-change-mgmt/test-program-revision-history-template.md) | 📝 log | 🟠 required | MTE Staff | by-table · medium | template-stub |

### MP CP3: Incoming Quality and Anomaly Management

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `MP-CP3-CAR-005` | [Containment Action Report](mp-mass-production/cp3-incoming-quality-anomaly/containment-action-report-template.md) | 📊 report | 🟠 required | Quality Engineer | by-section · medium | template-stub |
| `MP-CP3-CRA-004` | [Component Risk Assessment](mp-mass-production/cp3-incoming-quality-anomaly/component-risk-assessment-template.md) | 🔬 analysis | 🟠 required | MTE Lead | by-section · medium | template-stub |
| `MP-CP3-IQR-001` | [Incoming Quality Report / IQC Report](mp-mass-production/cp3-incoming-quality-anomaly/iqc-incoming-quality-report-template.md) | 📊 report | 🔴 critical | Quality Engineer | by-section · medium | template-stub |
| `MP-CP3-NMR-003` | [NCR / MRB Report](mp-mass-production/cp3-incoming-quality-anomaly/ncr-mrb-report-template.md) | 📊 report | 🔴 critical | Quality Engineer | by-section · high | template-stub |
| `MP-CP3-SIT-002` | [Supplier Issue Tracker](mp-mass-production/cp3-incoming-quality-anomaly/supplier-issue-tracker-template.md) | 🔍 tracker | 🟠 required | Quality Engineer | by-table · medium | template-stub |

### MP CP4: Continuous Improvement

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `MP-CP4-CRP-002` | [Cost Reduction Plan](mp-mass-production/cp4-continuous-improvement/cost-reduction-plan-template.md) | 📋 plan | 🟡 recommended | MTE Manager | by-section · medium | template-stub |
| `MP-CP4-PAP-005` | [Preventive Action Plan](mp-mass-production/cp4-continuous-improvement/preventive-action-plan-template.md) | 📋 plan | 🟡 recommended | Quality Engineer | by-section · medium | template-stub |
| `MP-CP4-SCP-004` | [Station Consolidation Proposal](mp-mass-production/cp4-continuous-improvement/station-consolidation-proposal-template.md) | 📋 plan | 🔵 optional | MTE Lead | by-section · medium | template-stub |
| `MP-CP4-TTO-003` | [Test Time Optimization Report](mp-mass-production/cp4-continuous-improvement/test-time-optimization-report-template.md) | 📊 report | 🟡 recommended | MTE Staff | by-section · medium | template-stub |
| `MP-CP4-YIP-001` | [Yield Improvement Plan](mp-mass-production/cp4-continuous-improvement/yield-improvement-plan-template.md) | 📋 plan | 🟠 required | MTE Lead | by-section · high | template-stub |

### MP CP5: Project Closure and Knowledge Archival

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `MP-CP5-BPP-003` | [Best Practice / Playbook](mp-mass-production/cp5-closure-knowledge/best-practice-playbook-template.md) | 🎯 playbook | 🟠 required | MTE Lead | by-section · high | template-stub |
| `MP-CP5-FLL-002` | [Final Lessons Learned](mp-mass-production/cp5-closure-knowledge/final-lessons-learned-template.md) | 📊 report | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `MP-CP5-KBU-004` | [Knowledge Base Update](mp-mass-production/cp5-closure-knowledge/knowledge-base-update-template.md) | 📝 log | 🟠 required | MTE Lead | by-section · high | template-stub |
| `MP-CP5-MSR-001` | [MP Phase Summary Report](mp-mass-production/cp5-closure-knowledge/mp-phase-summary-report-template.md) | 📊 report | 🔴 critical | MTE Manager | by-section · high | template-stub |
| `MP-CP5-PCR-005` | [Project Closure Report](mp-mass-production/cp5-closure-knowledge/project-closure-report-template.md) | 📊 report | 🟠 required | NPI PM | by-section · medium | template-stub |

### MP CP6: Next-Generation Product Feedback

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `MP-CP6-DFF-001` | [DFT / DFX Feedback Report](mp-mass-production/cp6-next-gen-feedback/dft-dfx-feedback-report-template.md) | 📊 report | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `MP-CP6-FRA-002` | [Field Return / RMA Analysis Summary](mp-mass-production/cp6-next-gen-feedback/field-return-rma-analysis-template.md) | 📊 report | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `MP-CP6-NFD-004` | [NPI Feedback to Design Team](mp-mass-production/cp6-next-gen-feedback/npi-feedback-to-design-template.md) | 📊 report | 🔴 critical | MTE Lead | by-section · high | template-stub |
| `MP-CP6-TES-003` | [Test Escape Summary](mp-mass-production/cp6-next-gen-feedback/test-escape-summary-template.md) | 📊 report | 🔴 critical | MTE Lead | by-section · high | template-stub |

## Shared Snippets — 5 documents

### Shared Snippet

| Doc ID | Title | Type | Priority | Owner | RAG Strategy | Status |
|--------|-------|------|----------|-------|-------------|--------|
| `SHARED-SNIP-DFT-005` | [DFT Coverage Table Template](shared/_snippets/dft-coverage-table-template.md) | 🗃️ matrix | ⚪ — | MTE Lead | by-table · high | approved |
| `SHARED-SNIP-ELD-002` | [Escape / Leakage Definition Reference](shared/_snippets/escape-leakage-definition.md) | 📐 spec | ⚪ — | MTE Lead | by-section · high | approved |
| `SHARED-SNIP-GRR-004` | [GR&R Acceptance Criteria Reference](shared/_snippets/grr-acceptance-criteria.md) | 📐 spec | ⚪ — | Quality Engineer | by-section · high | approved |
| `SHARED-SNIP-PFC-001` | [Pass/Fail Criteria Boilerplate](shared/_snippets/pass-fail-criteria-boilerplate.md) | 📐 spec | ⚪ — | MTE Lead | by-section · high | approved |
| `SHARED-SNIP-UPH-003` | [UPH Calculation Method](shared/_snippets/uph-calculation-method.md) | 📐 spec | ⚪ — | MTE Staff | by-section · medium | approved |
