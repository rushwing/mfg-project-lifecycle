---
doc_type: glossary
version: "1.0.0"
last_updated: "2026-03-29"
maintainer: "MTE Lead"
description: >
  Canonical term definitions for the MFG Project Lifecycle Knowledge Base.
  All controlled_terms declared in template frontmatter MUST have an entry here.
  The LLM document generation agent uses this file as the semantic anchor to
  prevent terminology drift across phases and product families.
rag_chunk_strategy: by-section
embedding_priority: high
---

# Manufacturing Test Engineering — Glossary

> **Purpose:** This is the single source of truth for all controlled terminology used in manufacturing test engineering document templates. All `controlled_terms` fields in template frontmatter must reference canonical forms defined here.
>
> **Usage by AI agents:** When generating or reviewing documents, always resolve ambiguous terms against this glossary before producing output. Terms listed under `Do Not Confuse With` are common sources of semantic drift.
>
> **Maintenance:** Add new terms before using them in templates. Changing a canonical form requires updating all templates that reference it.

---

## Table of Contents

1. [Lifecycle Phases](#lifecycle-phases)
2. [Test Types and Stations](#test-types-and-stations)
3. [Document and Process Terms](#document-and-process-terms)
4. [Quality and Yield Terms](#quality-and-yield-terms)
5. [Efficiency and Capacity Terms](#efficiency-and-capacity-terms)
6. [Materials and Change Control](#materials-and-change-control)
7. [Equipment and Fixture Terms](#equipment-and-fixture-terms)
8. [Software and Data Terms](#software-and-data-terms)

---

## Lifecycle Phases

### NPI
**Canonical Form:** `NPI`
**Canonical Form (zh-CN):** `新品导入`
**Canonical Form (zh-TW):** `新品導入`
**Canonical Form (vi):** *(pending)*
**Aliases:** New Product Introduction, New Product Intro
**Definition:** The end-to-end process of bringing a new product from concept through engineering validation to mass production readiness. NPI encompasses all phases from P1 through PVT exit.
**Do Not Confuse With:** MP (Mass Production), which begins after NPI exit gate.
**Phase Context:** Meta-term spanning P1, EVT, DVT, PVT.
**Example Usage:** "The NPI build plan governs engineering resource allocation from P1 through PVT."

---

### P1
**Canonical Form:** `P1`
**Canonical Form (zh-CN):** `P1阶段`
**Canonical Form (zh-TW):** `P1階段`
**Canonical Form (vi):** *(pending)*
**Aliases:** Pre-NPI, Concept Phase, Feasibility Phase
**Definition:** The first lifecycle phase covering product concept, feasibility analysis, and pre-NPI planning. Outputs include test strategy, test architecture, fixture concepts, and program mechanisms (RAID log, build plan, milestones).
**Do Not Confuse With:** EVT, which is the first hardware build phase. P1 is planning-only, no physical builds.
**Phase Context:** P1.
**Example Usage:** "DFT requirements are first captured in P1-CP1 and refined through EVT."

---

### EVT
**Canonical Form:** `EVT`
**Canonical Form (zh-CN):** `工程验证测试`
**Canonical Form (zh-TW):** `工程驗證測試`
**Canonical Form (vi):** *(pending)*
**Aliases:** Engineering Validation Test, Engineering Validation
**Definition:** The first hardware build phase. Goal: validate that the design meets engineering specifications. Test infrastructure (fixtures, frameworks, test programs) is developed and debugged on early silicon/hardware. Yield and UPH are not targets at this phase.
**Do Not Confuse With:** DVT (design is more mature, focus shifts to coverage and repeatability).
**Phase Context:** EVT.
**Example Usage:** "EVT exit requires TRP sign-off and passing EVT Exit Criteria Review."

---

### DVT
**Canonical Form:** `DVT`
**Canonical Form (zh-CN):** `设计验证测试`
**Canonical Form (zh-TW):** `設計驗證測試`
**Canonical Form (vi):** *(pending)*
**Aliases:** Design Validation Test, Design Validation
**Definition:** Second hardware build phase. Goal: validate design completeness, test coverage maturity, fixture qualification (GR&R), software releasability, and initial UPH/yield baselines. Design changes are minimal; focus is on test robustness.
**Do Not Confuse With:** EVT (earlier, infrastructure still developing); PVT (DVT is still NPI, not production-ready).
**Phase Context:** DVT.
**Example Usage:** "DVT-CP2 requires GR&R report to confirm fixture measurement repeatability."

---

### PVT
**Canonical Form:** `PVT`
**Canonical Form (zh-CN):** `生产验证测试`
**Canonical Form (zh-TW):** `生產驗證測試`
**Canonical Form (vi):** *(pending)*
**Aliases:** Production Validation Test, PVT Build
**Definition:** Third and final NPI hardware build phase. Goal: validate the complete mass production flow end-to-end including SFC, traceability, operator workflow, IQ/OQ qualification, and yield/UPH targets. PVT exit is the gate to MP.
**Do Not Confuse With:** DVT (PVT is production-flow focused, not design-focused); MP (PVT is still validation, not sustained production).
**Phase Context:** PVT.
**Example Usage:** "PVT-CP5 MP Release Recommendation is required before factory ops handover."

---

### MP
**Canonical Form:** `MP`
**Canonical Form (zh-CN):** `量产`
**Canonical Form (zh-TW):** `量產`
**Canonical Form (vi):** *(pending)*
**Aliases:** Mass Production, Volume Production, HVM (High Volume Manufacturing)
**Definition:** Sustained production phase following PVT exit. Focus shifts to daily ops, yield maintenance, change management, incoming quality control, and continuous improvement. Engineering involvement transitions to support mode.
**Do Not Confuse With:** PVT (which is the final validation phase before MP starts).
**Phase Context:** MP.
**Example Usage:** "ECO/ECN changes during MP require Change Management Log entries and golden unit re-verification."

---

### EOL
**Canonical Form:** `EOL`
**Canonical Form (zh-CN):** `生命周期终止`
**Canonical Form (zh-TW):** `生命週期終止`
**Canonical Form (vi):** *(pending)*
**Aliases:** End of Life, Product EOL, Sunset
**Definition:** The phase when a product is discontinued from active manufacturing. Triggered by product lifecycle management decisions. Requires documentation of final lessons learned, field return data handoff, and knowledge base archival.
**Do Not Confuse With:** MP (EOL is the termination of MP).
**Phase Context:** Post-MP.
**Example Usage:** "EOL DFT/DFX feedback is captured in the NPI Feedback to Design Team document."

---

## Test Types and Stations

### ICT
**Canonical Form:** `ICT`
**Canonical Form (zh-CN):** `在路测试`
**Canonical Form (zh-TW):** `在路測試`
**Canonical Form (vi):** *(pending)*
**Aliases:** In-Circuit Test, In-Circuit Testing
**Definition:** Automated test using bed-of-nails or flying probe fixture to verify correct component population, solder joint integrity, and basic circuit functionality by accessing individual nodes. Detects manufacturing defects at component level.
**Do Not Confuse With:** FCT (ICT is structural/parametric test; FCT is functional test of assembled board behavior). ICT does not test system-level functionality.
**Phase Context:** EVT through MP.
**Example Usage:** "ICT coverage gap analysis in DVT-CP1 identified 15% of nets not accessible by the current fixture."

---

### FCT
**Canonical Form:** `FCT`
**Canonical Form (zh-CN):** `功能电路测试`
**Canonical Form (zh-TW):** `功能電路測試`
**Canonical Form (vi):** *(pending)*
**Aliases:** Functional Circuit Test, Functional Check Test, Functional Test
**Definition:** Automated test that verifies the functional correctness of an assembled PCB or system by exercising it under operational conditions. Tests interfaces, communication protocols, power rails, and functional blocks.
**Do Not Confuse With:** ICT (FCT does not test individual nodes; it tests functional behavior). DIAG (FCT is typically a standalone station; DIAG may run within system context).
**Phase Context:** EVT through MP.
**Example Usage:** "FCT Test Plan must define pass/fail criteria for all PCIe, NVLink, and HBM interfaces."

---

### DIAG
**Canonical Form:** `DIAG`
**Canonical Form (zh-CN):** `诊断测试`
**Canonical Form (zh-TW):** `診斷測試`
**Canonical Form (vi):** *(pending)*
**Aliases:** Diagnostics, Manufacturing Diagnostics, MFG DIAG
**Definition:** Software-driven diagnostic tests executed on the DUT (Device Under Test) using on-board processors or embedded controllers. Includes BIST execution, memory tests, thermal ramp, and hardware-level diagnostic sequences. Distinguished from FCT by running within the DUT's own execution environment.
**Do Not Confuse With:** FCT (external tester driving the board vs. internal processor running diagnostics). Field diagnostics (DIAG in this KB refers to manufacturing diagnostics only).
**Phase Context:** EVT through MP.
**Example Usage:** "DIAG Development Plan details the NVDIAG test sequence, coverage, and pass/fail thresholds."

---

### BIST
**Canonical Form:** `BIST`
**Canonical Form (zh-CN):** `内建自测`
**Canonical Form (zh-TW):** `內建自測`
**Canonical Form (vi):** *(pending)*
**Aliases:** Built-In Self-Test, On-Chip Self-Test
**Definition:** Self-test capability embedded in hardware (typically in silicon) that can verify internal logic, memory arrays, or functional blocks without external test equipment. Invoked during manufacturing test as part of DIAG sequences.
**Do Not Confuse With:** DIAG (BIST is a hardware feature; DIAG is the software that invokes BIST and interprets results). SCAN (BIST tests functional blocks; scan tests structural logic).
**Phase Context:** EVT through MP.
**Example Usage:** "BIST coverage for HBM PHY is verified as part of the Test Coverage Matrix in EVT-CP2."

---

### Boundary Scan
**Canonical Form:** `Boundary Scan`
**Canonical Form (zh-CN):** `边界扫描`
**Canonical Form (zh-TW):** `邊界掃描`
**Canonical Form (vi):** *(pending)*
**Aliases:** BScan, JTAG Boundary Scan, IEEE 1149.1
**Definition:** IEEE 1149.1 standard-based test methodology that uses shift registers (boundary scan cells) at I/O pins to test board interconnects and component connectivity without physical probing. Used to detect open/short circuits on boards where ICT access is limited.
**Do Not Confuse With:** ICT (Boundary Scan is JTAG-based and requires JTAG support in devices; ICT uses physical probing). BIST (Boundary Scan tests interconnects; BIST tests internal logic).
**Phase Context:** P1 through MP.
**Example Usage:** "Boundary Scan test coverage for GPU-to-CPU interconnects is included in the DFT Requirement document."

---

### ATE
**Canonical Form:** `ATE`
**Canonical Form (zh-CN):** `自动测试设备`
**Canonical Form (zh-TW):** `自動測試設備`
**Canonical Form (vi):** *(pending)*
**Aliases:** Automated Test Equipment
**Definition:** General term for automated electronic test systems used in manufacturing. In the context of this KB, refers specifically to wafer-level or bare-die test systems (e.g., Teradyne, Advantest platforms) as distinct from board-level FCT stations.
**Do Not Confuse With:** FCT station (ATE typically refers to wafer/die test; board test is FCT). The term ATE is sometimes used colloquially to mean any automated test station — in this KB, use the specific station type (ICT, FCT, DIAG) unless referring generically.
**Phase Context:** Pre-EVT through MP (wafer test).
**Example Usage:** "ATE test results from wafer sort are used to calibrate expected defect rates in EVT."

---

### OBA
**Canonical Form:** `OBA`
**Canonical Form (zh-CN):** `开箱审核`
**Canonical Form (zh-TW):** `開箱稽核`
**Canonical Form (vi):** *(pending)*
**Aliases:** Out-of-Box Audit, OBA Test
**Definition:** Final audit test performed on packaged/finished products before shipment. Verifies that the product functions correctly from a customer-perspective workflow. Catches any damage or regression introduced during packaging/handling.
**Do Not Confuse With:** FCT (OBA is post-packaging functional check; FCT is pre-packaging board-level test). System Test (OBA is a sampling audit; System Test is 100% coverage).
**Phase Context:** PVT, MP.
**Example Usage:** "OBA sampling rate and test coverage are defined in the Mass Production Test Flow."

---

### HIL
**Canonical Form:** `HIL`
**Canonical Form (zh-CN):** `硬件在环测试`
**Canonical Form (zh-TW):** `硬體在環測試`
**Canonical Form (vi):** *(pending)*
**Aliases:** Hardware-in-the-Loop, HIL Testing
**Definition:** Test methodology where real hardware is connected to a simulated environment (e.g., virtual vehicle bus, simulated sensor inputs) to validate embedded software and hardware interaction. Primarily used for Automotive product validation.
**Do Not Confuse With:** FCT (HIL simulates operating environment; FCT tests hardware functionality directly). SIL (Software-in-the-Loop — no physical hardware).
**Phase Context:** EVT through DVT (Automotive products).
**Example Usage:** "For Automotive products, the Test Plan must include HIL test coverage for CAN/LIN interface validation."

---

## Document and Process Terms

### TRP
**Canonical Form:** `TRP`
**Canonical Form (zh-CN):** `测试需求计划`
**Canonical Form (zh-TW):** `測試需求計畫`
**Canonical Form (vi):** *(pending)*
**Aliases:** Test Requirement Plan, Test Readiness Plan, Test Requirements Plan
**Definition:** Master planning document that baselines all manufacturing test requirements for a product. Defines test objectives, station coverage, pass/fail philosophy, test ownership, and exit criteria for each phase. TRP is the primary gate document for EVT and DVT phase reviews.
**Do Not Confuse With:** Test Plan (TRP is higher-level requirements; Test Plan is the detailed execution spec for a specific station). PRD (TRP is manufacturing-specific; PRD is product requirements for the end customer).
**Phase Context:** EVT-CP2 creation, updated each phase through DVT.
**Example Usage:** "TRP must be signed off by MTE Lead, HW Design Lead, and PM before EVT-CP2 exit."

---

### PRD
**Canonical Form:** `PRD`
**Canonical Form (zh-CN):** `产品需求文档`
**Canonical Form (zh-TW):** `產品需求文件`
**Canonical Form (vi):** *(pending)*
**Aliases:** Product Requirements Document
**Definition:** Document specifying product features, performance requirements, and constraints from a product management perspective. MTE uses PRD as an input to derive testability requirements and test coverage goals.
**Do Not Confuse With:** MRD (PRD is engineering-focused; MRD is market/customer focused). HW Spec (PRD is feature-level; HW Spec is implementation-level).
**Phase Context:** P1-CP1 input.
**Example Usage:** "DFT requirements in P1-CP1 are derived directly from PRD functional requirements."

---

### MRD
**Canonical Form:** `MRD`
**Canonical Form (zh-CN):** `市场需求文档`
**Canonical Form (zh-TW):** `市場需求文件`
**Canonical Form (vi):** *(pending)*
**Aliases:** Market Requirements Document
**Definition:** Document specifying market and customer requirements for a product, including use cases, competitive positioning, and market segment needs. Upstream input to PRD.
**Do Not Confuse With:** PRD (MRD is customer-facing requirements; PRD translates these to engineering specs).
**Phase Context:** P1-CP1 input.
**Example Usage:** "MRD and PRD are reviewed in P1-CP1 requirements clarification to identify testability constraints."

---

### DFT
**Canonical Form:** `DFT`
**Canonical Form (zh-CN):** `可测试性设计`
**Canonical Form (zh-TW):** `可測試性設計`
**Canonical Form (vi):** *(pending)*
**Aliases:** Design for Test, Design for Testability
**Definition:** A set of design practices and requirements that ensure a product can be efficiently tested during manufacturing. Includes JTAG boundary scan, BIST, test access points, and diagnostic hooks. MTE provides DFT requirements to hardware design teams during P1.
**Do Not Confuse With:** DFX (DFT is specifically about testability; DFX is a broader term). Test Coverage (DFT enables coverage; coverage is the outcome measurement).
**Phase Context:** P1 requirement capture, enforced through EVT/DVT.
**Example Usage:** "DFT Requirement document specifies minimum JTAG chain coverage and BIST requirements for all ICs."

---

### DFX
**Canonical Form:** `DFX`
**Canonical Form (zh-CN):** `面向X的设计`
**Canonical Form (zh-TW):** `面向X的設計`
**Canonical Form (vi):** *(pending)*
**Aliases:** Design for Excellence, Design for X
**Definition:** Umbrella term for design methodologies that optimize products for a specific manufacturing attribute. Includes DFT (testability), DFM (manufacturability), DFA (assembly), DFS (serviceability). In MTE context, DFX typically refers to the combination relevant to manufacturing test and quality.
**Do Not Confuse With:** DFT (DFT is a subset of DFX focused specifically on testability).
**Phase Context:** P1 through DVT.
**Example Usage:** "DFX Feedback Report at MP-CP6 consolidates lessons learned on testability, assembly, and serviceability for the next product generation."

---

### SFC
**Canonical Form:** `SFC`
**Canonical Form (zh-CN):** `车间流程控制`
**Canonical Form (zh-TW):** `車間流程控制`
**Canonical Form (vi):** *(pending)*
**Aliases:** Shop Floor Control, MES (Manufacturing Execution System), WMS (Work Management System)
**Definition:** Software system that tracks unit serial numbers, test results, repair history, and routing decisions on the factory floor. SFC is the traceability backbone — every unit's test pass/fail at every station is recorded and linked to its serial number.
**Do Not Confuse With:** ERP (SFC is real-time shop floor; ERP is business-level planning). Traceability (SFC is the system; traceability is the outcome it enables).
**Phase Context:** EVT-CP3 interface spec, validated in PVT-CP4, sustained in MP.
**Example Usage:** "SFC Interface Requirement defines the API contract between the test station and the factory's SFC system."

---

### RAID
**Canonical Form:** `RAID`
**Canonical Form (zh-CN):** `风险行动问题决策日志`
**Canonical Form (zh-TW):** `風險行動問題決策日誌`
**Canonical Form (vi):** *(pending)*
**Aliases:** RAID Log, Risk-Action-Issue-Dependency Log
**Definition:** Program management tool that tracks four categories: Risks (potential future problems), Actions (tasks with owners and due dates), Issues (current problems being resolved), and Dependencies (external commitments or blockers). Standard NPI program management artifact.
**Do Not Confuse With:** Bug list/Defect tracker (RAID covers program-level risks and actions; defect trackers are test-result-specific). RAID storage (unrelated acronym).
**Phase Context:** P1-CP4 through MP.
**Example Usage:** "RAID Log is updated weekly and reviewed in the NPI program status meeting."

---

### CAPA
**Canonical Form:** `CAPA`
**Canonical Form (zh-CN):** `纠正及预防措施`
**Canonical Form (zh-TW):** `矯正及預防措施`
**Canonical Form (vi):** *(pending)*
**Aliases:** Corrective Action and Preventive Action, Corrective and Preventive Action
**Definition:** Formal quality management process to (1) identify root cause of a defect or process failure, (2) implement corrective action to fix the specific instance, and (3) implement preventive action to prevent recurrence. CAPA reports are required for any yield excursion or test escape.
**Do Not Confuse With:** RCA (RCA is the root cause analysis portion of CAPA; CAPA includes both corrective and preventive action). FA (FA provides technical root cause; CAPA documents the process response to that root cause).
**Phase Context:** DVT-CP5, PVT-CP3, MP.
**Example Usage:** "CAPA is required for any yield loss exceeding the DVT exit threshold of 95%."

---

### ECO
**Canonical Form:** `ECO`
**Canonical Form (zh-CN):** `工程变更通知`
**Canonical Form (zh-TW):** `工程變更通知`
**Canonical Form (vi):** *(pending)*
**Aliases:** Engineering Change Order
**Definition:** A formal document authorizing and recording a change to hardware design, firmware, or test program. ECOs are numbered, tracked, and require cross-functional approval. In manufacturing, ECOs are issued to implement design changes on production builds.
**Do Not Confuse With:** ECN (ECO is the formal order; ECN is the notification/record of change). PCN (Product Change Notice — used by suppliers to notify customers of component changes).
**Phase Context:** DVT-CP3 through MP.
**Example Usage:** "ECO/ECN Impact Assessment evaluates whether a design change requires re-qualification of test coverage."

---

### ECN
**Canonical Form:** `ECN`
**Canonical Form (zh-CN):** `工程变更通知单`
**Canonical Form (zh-TW):** `工程變更通知單`
**Canonical Form (vi):** *(pending)*
**Aliases:** Engineering Change Notice, Engineering Change Notification
**Definition:** Document that notifies stakeholders of an approved engineering change, referencing the corresponding ECO. ECN is the communication vehicle; ECO is the authorization.
**Do Not Confuse With:** ECO (ECN is the notice/record; ECO is the order/authorization). PCN (PCN comes from component suppliers; ECN is internal to the OEM/ODM).
**Phase Context:** DVT-CP3 through MP.
**Example Usage:** "All ECNs affecting test coverage must be reflected in the Configuration Control Matrix before DVT-CP3 exit."

---

### IQ
**Canonical Form:** `IQ`
**Canonical Form (zh-CN):** `安装确认`
**Canonical Form (zh-TW):** `安裝確認`
**Canonical Form (vi):** *(pending)*
**Aliases:** Installation Qualification, Tester IQ
**Definition:** Formal qualification step that verifies a test system has been installed correctly according to specifications — correct hardware configuration, software version, calibration status, and environmental conditions. IQ is the first of three validation steps (IQ → OQ → PQ).
**Do Not Confuse With:** OQ (OQ verifies operational performance after installation). PQ (PQ verifies performance under production conditions). Intelligence Quotient (unrelated).
**Phase Context:** PVT-CP2.
**Example Usage:** "Tester IQ checklist must be completed and signed before any test data collected at the new factory site is considered valid."

---

### OQ
**Canonical Form:** `OQ`
**Canonical Form (zh-CN):** `运行确认`
**Canonical Form (zh-TW):** `運行確認`
**Canonical Form (vi):** *(pending)*
**Aliases:** Operational Qualification, Tester OQ
**Definition:** Formal qualification step that verifies a test system operates within specified performance parameters when running standardized test routines. Follows IQ. Demonstrates that the system meets its operational specifications.
**Do Not Confuse With:** IQ (IQ verifies installation; OQ verifies operational performance). PQ (OQ uses standardized inputs; PQ uses actual production parts under real conditions).
**Phase Context:** PVT-CP2.
**Example Usage:** "OQ report must demonstrate measurement accuracy within ±2% of reference standard across all test channels."

---

### PQ
**Canonical Form:** `PQ`
**Canonical Form (zh-CN):** `性能确认`
**Canonical Form (zh-TW):** `性能確認`
**Canonical Form (vi):** *(pending)*
**Aliases:** Performance Qualification, Production Qualification
**Definition:** Formal qualification step that verifies a test system produces consistent, acceptable results when testing actual production units under real manufacturing conditions. Follows OQ. Includes process capability studies.
**Do Not Confuse With:** OQ (PQ is with real production parts; OQ is with standardized reference inputs). GR&R (GR&R quantifies measurement variation specifically; PQ is a broader production process validation).
**Phase Context:** PVT-CP2 (less commonly used term in semiconductor manufacturing; IQ/OQ are more prevalent).
**Example Usage:** "PQ data from the first 200 production units confirms Cpk > 1.33 for all critical test parameters."

---

### GR&R
**Canonical Form:** `GR&R`
**Canonical Form (zh-CN):** `量具重复性与再现性`
**Canonical Form (zh-TW):** `量具重複性與再現性`
**Canonical Form (vi):** *(pending)*
**Aliases:** Gauge R&R, Gauge Repeatability and Reproducibility, Gage R&R
**Definition:** Statistical study that quantifies the total measurement system variation attributable to (1) repeatability (same operator, same unit, repeated measures) and (2) reproducibility (different operators or stations measuring the same unit). Expressed as %GR&R relative to total process variation or tolerance. In MTE, GR&R validates that fixture + tester measurement variation is acceptable before committing to production tooling.
**Do Not Confuse With:** Cpk (GR&R measures measurement system; Cpk measures process capability). False Fail rate (GR&R is a characterization study; false fail is a production metric).
**Phase Context:** DVT-CP2.
**Example Usage:** "GR&R Report must show %GR&R < 10% for all critical parametric measurements before fixture acceptance."

---

## Quality and Yield Terms

### Test Escape
**Canonical Form:** `Test Escape`
**Canonical Form (zh-CN):** `测试逃逸`
**Canonical Form (zh-TW):** `測試逃逸`
**Canonical Form (vi):** *(pending)*
**Aliases:** Escape, Quality Escape, Leakage (in some contexts)
**Definition:** A defective unit that passes all manufacturing tests and is shipped to the customer, where it subsequently fails. Test escapes represent the most critical quality failure mode — the test process failed to catch a real defect. Measured as DPPM (Defective Parts Per Million shipped).
**Do Not Confuse With:** False Fail (False Fail is a good unit incorrectly rejected; Test Escape is a bad unit incorrectly accepted — opposite failure modes). Leakage (Leakage is a synonym for Test Escape in some vocabularies, but in this KB use Test Escape as the canonical form to avoid ambiguity with electrical leakage current).
**Phase Context:** DVT-CP5, PVT-CP3, MP.
**Example Usage:** "Escape/Leakage Analysis identifies test gaps that allowed defective units to pass FCT."

---

### False Fail
**Canonical Form:** `False Fail`
**Canonical Form (zh-CN):** `误判失效`
**Canonical Form (zh-TW):** `誤判失效`
**Canonical Form (vi):** *(pending)*
**Aliases:** False Reject, False Negative, Nuisance Fail, Pseudo Fail
**Definition:** A non-defective (good) unit that fails manufacturing test incorrectly, due to test noise, measurement instability, marginal test limits, or fixture contact issues. False fails reduce effective yield and increase retest/repair burden without improving quality.
**Do Not Confuse With:** True Fail (True Fail is a genuinely defective unit correctly identified by test). Marginal Fail (Marginal Fail may be a real defect near the spec limit; False Fail is a good unit incorrectly failed).
**Phase Context:** DVT-CP5, PVT-CP3, MP.
**Example Usage:** "False Fail Retest Reduction Report identifies the top 5 test items with >2% retest rate for limit optimization."

---

### True Fail
**Canonical Form:** `True Fail`
**Canonical Form (zh-CN):** `真实失效`
**Canonical Form (zh-TW):** `真實失效`
**Canonical Form (vi):** *(pending)*
**Aliases:** Real Fail, Genuine Fail
**Definition:** A defective unit that fails manufacturing test correctly — the test has identified a real defect. True fails are the intended output of the test process and indicate manufacturing quality issues that need investigation.
**Do Not Confuse With:** False Fail (True Fail is a real defect correctly caught; False Fail is a good unit incorrectly rejected).
**Phase Context:** All phases.
**Example Usage:** "Pareto Report categorizes all True Fails by failure mode to prioritize yield improvement actions."

---

### Marginal Fail
**Canonical Form:** `Marginal Fail`
**Canonical Form (zh-CN):** `边界失效`
**Canonical Form (zh-TW):** `邊界失效`
**Canonical Form (vi):** *(pending)*
**Aliases:** Marginal, Near-Spec Fail, Borderline Fail
**Definition:** A unit that fails test with a measured value close to the pass/fail limit. May indicate a real defect at the tolerance boundary, measurement system variation, or a unit that is at risk of early field failure. Requires careful analysis to distinguish from False Fail.
**Do Not Confuse With:** False Fail (Marginal Fail may have a real defect near spec; False Fail is definitively a good unit). True Fail (Marginal Fail is borderline; True Fail is clearly defective).
**Phase Context:** DVT-CP5, PVT-CP3, MP.
**Example Usage:** "Retest Analysis Report must classify each retest unit as True Fail, False Fail, or Marginal Fail."

---

### Retest
**Canonical Form:** `Retest`
**Canonical Form (zh-CN):** `复测`
**Canonical Form (zh-TW):** `複測`
**Canonical Form (vi):** *(pending)*
**Aliases:** Re-test, Rescreen
**Definition:** The act of running a test on a unit that previously failed, to determine if the failure was repeatable (True Fail) or non-repeatable (False Fail / Marginal Fail). Retest policy (who can authorize, how many times, what disposition follows) must be defined in the Test Plan.
**Do Not Confuse With:** Repair (Retest is re-running test without physical intervention; Repair involves physical rework before retesting). Regression test (Retest is on a failed unit; regression test is validating that a software change didn't break existing passing tests).
**Phase Context:** EVT through MP.
**Example Usage:** "Retest is permitted up to 2 times per unit; a third failure requires FA escalation per the Test Plan."

---

### Golden Unit
**Canonical Form:** `Golden Unit`
**Canonical Form (zh-CN):** `黄金样机`
**Canonical Form (zh-TW):** `黃金樣機`
**Canonical Form (vi):** *(pending)*
**Aliases:** Golden Sample, Reference Unit, Standard Unit, Known-Good Unit
**Definition:** A characterized unit with known-good behavior used as a reference for calibrating test stations, establishing baseline measurements, and verifying test system health. Golden Units must be periodically re-verified to ensure they remain in specification.
**Do Not Confuse With:** Production unit (Golden Units are reference standards, not production parts). Engineering sample (Engineering samples are early silicon; Golden Units are characterized reference units for test use).
**Phase Context:** EVT-CP1 definition, used through MP.
**Example Usage:** "Golden Unit Maintenance Record tracks calibration history, usage, and periodic re-verification results."

---

### FA
**Canonical Form:** `FA`
**Canonical Form (zh-CN):** `失效分析`
**Canonical Form (zh-TW):** `失效分析`
**Canonical Form (vi):** *(pending)*
**Aliases:** Failure Analysis
**Definition:** Technical investigation to determine the physical/electrical root cause of a component or unit failure. FA may involve destructive analysis (cross-section, SEM), electrical probing, and comparison to Golden Unit. FA produces a root cause finding that feeds CAPA.
**Do Not Confuse With:** RCA (RCA is the process/system analysis; FA is the physical/technical analysis of a specific failed unit). Debug (Debug is an informal troubleshooting activity; FA is a formal documented investigation).
**Phase Context:** DVT-CP5, PVT, MP.
**Example Usage:** "FA Request is submitted when a True Fail cannot be diagnosed through standard tester logging alone."

---

### RCA
**Canonical Form:** `RCA`
**Canonical Form (zh-CN):** `根因分析`
**Canonical Form (zh-TW):** `根因分析`
**Canonical Form (vi):** *(pending)*
**Aliases:** Root Cause Analysis
**Definition:** Systematic process to identify the underlying process, design, or system cause of a quality problem or yield excursion. RCA typically follows FA (which provides the physical/technical root cause) and precedes CAPA (which documents the corrective and preventive actions).
**Do Not Confuse With:** FA (FA investigates the specific failed unit; RCA investigates the broader process/system cause). CAPA (CAPA is the action plan derived from RCA).
**Phase Context:** EVT-CP5, DVT-CP5, PVT, MP.
**Example Usage:** "Root Cause Analysis Report must be completed within 5 business days of any yield excursion exceeding the action limit."

---

### Yield
**Canonical Form:** `Yield`
**Canonical Form (zh-CN):** `良率`
**Canonical Form (zh-TW):** `良率`
**Canonical Form (vi):** *(pending)*
**Aliases:** Test Yield, First Pass Yield (FPY), Pass Rate
**Definition:** The percentage of units that pass all manufacturing tests on the first attempt, without retest or repair. `Yield = (Units passing first test) / (Units entering test) × 100%`. Distinct from final yield which includes retest.
**Do Not Confuse With:** First Pass Yield (FPY is a synonym for Yield as defined here). Final Yield (includes retested units — higher than Yield by definition). Uptime/Availability (equipment metric, not product quality metric).
**Phase Context:** DVT-CP4 baseline, PVT-CP3 target, MP sustained.
**Example Usage:** "PVT exit requires First Pass Yield ≥ 92% sustained over 3 consecutive production days."

---

### Coverage Hole
**Canonical Form:** `Coverage Hole`
**Canonical Form (zh-CN):** `测试覆盖漏洞`
**Canonical Form (zh-TW):** `測試覆蓋漏洞`
**Canonical Form (vi):** *(pending)*
**Aliases:** Test Gap, Coverage Gap
**Definition:** A functional block, signal path, or failure mode that is not covered by any manufacturing test. Coverage holes are potential escape vectors. Identified through Test Gap Analysis and must be dispositioned (add test, accept risk with justification, or redesign DFT).
**Do Not Confuse With:** Test Gap (synonym — in this KB use Coverage Hole as the canonical form when describing a specific untested area, and Test Gap Analysis as the document/process name). False Fail (False Fail is a test that fires incorrectly; Coverage Hole is a test that doesn't exist).
**Phase Context:** EVT-CP2 identification, DVT-CP1 resolution.
**Example Usage:** "Test Gap Analysis identified a Coverage Hole in NVLink PHY PRBS testing at EVT."

---

### DPM
**Canonical Form:** `DPM`
**Canonical Form (zh-CN):** `百万缺陷率`
**Canonical Form (zh-TW):** `百萬缺陷率`
**Canonical Form (vi):** *(pending)*
**Aliases:** Defects Per Million, DPPM (Defective Parts Per Million)
**Definition:** Quality metric measuring defect rate. `DPM = (Defective units / Total units tested) × 1,000,000`. Used to set yield targets and measure test escape rates. DPPM specifically refers to defective parts (units) per million shipped.
**Do Not Confuse With:** PPM (Parts Per Million — a general concentration term); DPM in MTE always refers to quality/defect rate context.
**Phase Context:** MP quality targets.
**Example Usage:** "MP quality target: Test Escape rate < 50 DPPM."

---

### PFMEA
**Canonical Form:** `PFMEA`
**Canonical Form (zh-CN):** `制程失效模式与影响分析`
**Canonical Form (zh-TW):** `製程失效模式與影響分析`
**Canonical Form (vi):** *(pending)*
**Aliases:** Process FMEA, Manufacturing FMEA
**Definition:** Process Failure Mode and Effects Analysis. A structured risk analysis of each manufacturing process step, identifying potential failure modes, their effects on the product, potential causes, current controls, and a Risk Priority Number (RPN = Severity × Occurrence × Detection) used to prioritize corrective actions. PFMEA is the upstream input to the Control Plan.
**Do Not Confuse With:** DFMEA (Design FMEA — conducted by the design team on the product design, not the manufacturing process). PFMEA focuses on process steps and workmanship defects; DFMEA focuses on design-induced failure modes.
**Phase Context:** Created in P1/EVT when the manufacturing process is first defined; updated through DVT/PVT as the process matures. Mandatory for Automotive product families.
**Example Usage:** "The PFMEA for the FCT station identified insufficient pogo-pin pressure as a high-occurrence failure mode (RPN = 144); fixture redesign was triggered."

---

### RPN
**Canonical Form:** `RPN`
**Canonical Form (zh-CN):** `风险优先数`
**Canonical Form (zh-TW):** `風險優先數`
**Canonical Form (vi):** *(pending)*
**Aliases:** Risk Priority Number
**Definition:** Risk Priority Number. A composite risk score in FMEA: RPN = Severity (1–10) × Occurrence (1–10) × Detection (1–10). Range: 1–1000. Items with RPN ≥ 100 or Severity ≥ 8 require documented corrective actions. After actions are implemented, RPN is recalculated to confirm risk reduction.
**Do Not Confuse With:** Risk score in RAID log (qualitative High/Medium/Low); RPN is a quantitative FMEA-specific metric.
**Phase Context:** Used in PFMEA and DFMEA throughout EVT–PVT.
**Example Usage:** "Initial RPN for the open-solder failure mode was 210; post-reflow profile optimization reduced it to 48."

---

### SPC
**Canonical Form:** `SPC`
**Canonical Form (zh-CN):** `统计过程控制`
**Canonical Form (zh-TW):** `統計製程管制`
**Canonical Form (vi):** *(pending)*
**Aliases:** Statistical Process Control
**Definition:** Statistical Process Control. The use of control charts and statistical methods to monitor manufacturing process variables in real time, distinguishing normal process variation (common cause) from signals requiring intervention (special cause). Common chart types: X-bar/R for continuous variables, P-chart for proportion defective, np-chart for defect counts.
**Do Not Confuse With:** Process Capability (Cpk — a static capability metric computed from a data set); SPC is a real-time dynamic monitoring system. A process can be in statistical control but still have poor capability, and vice versa.
**Phase Context:** Baselines established during PVT; operated continuously in MP.
**Example Usage:** "FCT yield SPC chart triggered a Western Electric Rule 2 violation on Day 7 of MP ramp; root cause was a firmware version mismatch."

---

### Control Chart
**Canonical Form:** `Control Chart`
**Canonical Form (zh-CN):** `控制图`
**Canonical Form (zh-TW):** `管制圖`
**Canonical Form (vi):** *(pending)*
**Aliases:** Shewhart Chart, Process Control Chart
**Definition:** A time-series chart used in SPC with a center line (process mean), Upper Control Limit (UCL), and Lower Control Limit (LCL) set at ±3σ from the mean. Points outside control limits or patterns matching the Western Electric Rules indicate a special cause requiring investigation.
**Do Not Confuse With:** Specification limits (USL/LSL — engineering tolerances set by product requirements, wider than control limits); control limits are derived from process variation, not product tolerances.
**Phase Context:** MP daily operations and continuous improvement.
**Example Usage:** "The X-bar control chart for ICT test time showed the process drifting toward UCL over 3 shifts, indicating fixture wear."

---

### Cpk
**Canonical Form:** `Cpk`
**Canonical Form (zh-CN):** `过程能力指数`
**Canonical Form (zh-TW):** `製程能力指標`
**Canonical Form (vi):** *(pending)*
**Aliases:** Process Capability Index, Cp, Pp, Ppk
**Definition:** Process Capability Index. Measures how well a process output fits within specification limits relative to natural process variation. Cpk = min(USL − μ, μ − LSL) / (3σ). Thresholds: Cpk < 1.00 = incapable; 1.00–1.33 = marginal; ≥ 1.33 = capable; ≥ 1.67 = highly capable (Automotive target). Cp measures potential capability (ignoring mean offset); Cpk measures actual capability. Pp/Ppk use overall σ from a study; Cp/Cpk use within-subgroup σ from ongoing SPC charts.
**Do Not Confuse With:** Yield (a yield of 99% does not imply Cpk ≥ 1.33; a bimodal process can have high yield but poor Cpk and latent risk). Cpk should only be computed after the process is in statistical control.
**Phase Context:** Computed at DVT/PVT to qualify the manufacturing process; monitored in MP continuous improvement.
**Example Usage:** "GR&R passed (< 10% study variation), but Cpk for the RF power measurement was 0.91 — recalibration raised it to 1.45."

---

### 8D
**Canonical Form:** `8D`
**Canonical Form (zh-CN):** `八步骤问题解决法`
**Canonical Form (zh-TW):** `八步驟問題解決法`
**Canonical Form (vi):** *(pending)*
**Aliases:** Eight Disciplines, 8D Report, G8D, Global 8D
**Definition:** Eight Disciplines Problem Solving. A structured 8-step methodology for resolving significant quality problems: D1 (form the team), D2 (describe the problem), D3 (interim containment), D4 (root cause identification), D5 (permanent corrective actions), D6 (implement and validate), D7 (systemic preventive actions), D8 (recognize the team). Required by automotive customers (IATF 16949) for significant field or production quality escapes.
**Do Not Confuse With:** CAPA (a broader quality system requirement; 8D is a specific structured format often used to fulfill a CAPA). RCA (D4 is the RCA step within 8D; standalone RCA does not include containment, validation, or systemic prevention).
**Phase Context:** Triggered during EVT–MP when a high-severity defect or Test Escape is identified; mandatory for customer-facing field escapes.
**Example Usage:** "A field return cluster triggered a G8D; D4 identified a marginal solder joint on the power rail; D7 updated the PFMEA and tightened the paste volume spec in the SOP."

---

## Efficiency and Capacity Terms

### UPH
**Canonical Form:** `UPH`
**Canonical Form (zh-CN):** `每小时产出`
**Canonical Form (zh-TW):** `每小時產出`
**Canonical Form (vi):** *(pending)*
**Aliases:** Units Per Hour, Throughput Rate
**Definition:** Production throughput metric measuring how many units a test station or production line processes per hour. UPH is a primary capacity planning input. `UPH = 3600 / Cycle Time (seconds)`.
**Do Not Confuse With:** Cycle Time (Cycle Time is the inverse metric — seconds per unit). Takt Time (Takt Time is the rate demanded by customer; UPH is the rate supplied by the line).
**Phase Context:** P1-CP2 estimation, DVT-CP4 study, PVT-CP3 validation, MP monitoring.
**Example Usage:** "UPH Study Report in DVT-CP4 must demonstrate ≥ 45 UPH at FCT station to support MP ramp plan."

---

### Cycle Time
**Canonical Form:** `Cycle Time`
**Canonical Form (zh-CN):** `节拍时间`
**Canonical Form (zh-TW):** `節拍時間`
**Canonical Form (vi):** *(pending)*
**Aliases:** CT, Test Cycle Time, Station Cycle Time
**Definition:** The total elapsed time for a unit to complete one pass through a test station, from unit-in to unit-out. Includes test execution time, handler time, connection time, and any station overhead. `Cycle Time (s) = 3600 / UPH`.
**Do Not Confuse With:** UPH (UPH is throughput; Cycle Time is the duration metric). Takt Time (Takt Time is demand-driven; Cycle Time is supply-driven).
**Phase Context:** DVT-CP4, PVT-CP3.
**Example Usage:** "Cycle Time Breakdown documents each component of station cycle time to identify optimization opportunities."

---

### Takt Time
**Canonical Form:** `Takt Time`
**Canonical Form (zh-CN):** `生产节拍`
**Canonical Form (zh-TW):** `生產節拍`
**Canonical Form (vi):** *(pending)*
**Aliases:** Takt, Customer Takt
**Definition:** The rate at which products must be produced to meet customer demand. `Takt Time = Available production time / Customer demand rate`. If Cycle Time > Takt Time, the station is a bottleneck.
**Do Not Confuse With:** Cycle Time (Takt Time is the demand target; Cycle Time is the actual production rate). UPH (UPH is actual throughput; Takt Time is required throughput).
**Phase Context:** DVT-CP4, PVT-CP3.
**Example Usage:** "Station Loading Analysis compares Cycle Time to Takt Time to identify line balance issues."

---

### WIP
**Canonical Form:** `WIP`
**Canonical Form (zh-CN):** `在制品`
**Canonical Form (zh-TW):** `在製品`
**Canonical Form (vi):** *(pending)*
**Aliases:** Work in Progress, Work in Process
**Definition:** Units that are currently in the manufacturing process — between the start of production and final test pass. High WIP indicates bottlenecks or flow problems. WIP level is a key daily operations metric.
**Do Not Confuse With:** Input/Output (I/O Report tracks WIP flow). Buffer stock (managed WIP between stations for flow balancing).
**Phase Context:** MP-CP1 monitoring.
**Example Usage:** "WIP/IO Report tracks daily WIP levels by station to identify emerging bottlenecks."

---

### OEE
**Canonical Form:** `OEE`
**Canonical Form (zh-CN):** `设备综合效率`
**Canonical Form (zh-TW):** `設備綜合效率`
**Canonical Form (vi):** *(pending)*
**Aliases:** Overall Equipment Effectiveness
**Definition:** Composite metric measuring manufacturing productivity: `OEE = Availability × Performance × Quality`. Availability = uptime ratio; Performance = actual vs. theoretical speed; Quality = good parts ratio. OEE < 85% typically indicates a significant improvement opportunity.
**Do Not Confuse With:** UPH (UPH is a throughput count; OEE is a composite efficiency ratio). Yield (Yield is the Quality component of OEE, not OEE itself).
**Phase Context:** PVT-CP3, MP.
**Example Usage:** "Downtime Report feeds the Availability component of OEE calculation."

---

### Bottleneck
**Canonical Form:** `Bottleneck`
**Canonical Form (zh-CN):** `瓶颈站点`
**Canonical Form (zh-TW):** `瓶頸站點`
**Canonical Form (vi):** *(pending)*
**Aliases:** Constraint, Rate-Limiting Station
**Definition:** The production station with the lowest throughput capacity (highest cycle time relative to Takt Time), which limits the overall line output rate. The bottleneck determines the maximum throughput of the entire line regardless of other station capacities.
**Do Not Confuse With:** Downtime (Downtime is unplanned unavailability; Bottleneck is a structural capacity constraint). Station Loading (Station Loading analysis identifies the bottleneck).
**Phase Context:** DVT-CP4, PVT-CP3, MP.
**Example Usage:** "Bottleneck Analysis Report identified DIAG station as the constraint at 38 UPH vs. required 45 UPH."

---

## Materials and Change Control

### BOM
**Canonical Form:** `BOM`
**Canonical Form (zh-CN):** `物料清单`
**Canonical Form (zh-TW):** `物料清單`
**Canonical Form (vi):** *(pending)*
**Aliases:** Bill of Materials
**Definition:** Structured list of all components, subassemblies, and materials required to build a product or fixture. In MTE context, Fixture BOM lists all mechanical and electrical components of the test fixture.
**Do Not Confuse With:** AVL (Approved Vendor List — lists approved suppliers for BOM components). Assembly drawing (graphical representation vs. BOM tabular list).
**Phase Context:** EVT-CP4 (Fixture BOM), all phases for design BOM tracking.
**Example Usage:** "Fixture BOM must be controlled under version management and updated for every ECO affecting fixture hardware."

---

### IQC
**Canonical Form:** `IQC`
**Canonical Form (zh-CN):** `来料品质控制`
**Canonical Form (zh-TW):** `來料品質控制`
**Canonical Form (vi):** *(pending)*
**Aliases:** Incoming Quality Control, Incoming Inspection, Receiving Inspection
**Definition:** Quality inspection and verification process performed on components and materials when they arrive at the factory before use in production. IQC verifies supplier quality and prevents defective incoming materials from entering the production flow.
**Do Not Confuse With:** In-process quality (IQC is at receiving; in-process quality is on the production line). Supplier qualification (IQC is routine receiving inspection; supplier qualification is a one-time approval process).
**Phase Context:** MP-CP3.
**Example Usage:** "IQC Report documents daily incoming material acceptance/rejection results by supplier and part number."

---

### NCR
**Canonical Form:** `NCR`
**Canonical Form (zh-CN):** `不合格品报告`
**Canonical Form (zh-TW):** `不合格品報告`
**Canonical Form (vi):** *(pending)*
**Aliases:** Non-Conformance Report, Nonconformance Report
**Definition:** Formal document recording that a material, component, or process has failed to meet its specified requirements. NCR initiates the disposition process (use as-is, rework, reject, return to supplier) through MRB.
**Do Not Confuse With:** MRB (NCR documents the non-conformance; MRB is the board that reviews and dispositions NCRs). CAPA (NCR identifies the non-conformance event; CAPA addresses the systematic root cause).
**Phase Context:** MP-CP3.
**Example Usage:** "NCR is issued for any incoming material that fails IQC inspection; MRB disposition is required within 48 hours."

---

### MRB
**Canonical Form:** `MRB`
**Canonical Form (zh-CN):** `物料审查委员会`
**Canonical Form (zh-TW):** `物料審查委員會`
**Canonical Form (vi):** *(pending)*
**Aliases:** Material Review Board
**Definition:** Cross-functional team (typically including Quality, Engineering, and Operations) that reviews and dispositions NCRs for non-conforming materials or components. MRB decisions include: Use-As-Is, Rework, Conditional Use, Reject/Return to Supplier.
**Do Not Confuse With:** NCR (NCR is the document; MRB is the board that reviews it). FA (FA provides technical analysis; MRB makes the use/reject decision).
**Phase Context:** MP-CP3.
**Example Usage:** "NCR/MRB Report tracks open non-conformances and MRB disposition status for supplier accountability."

---

### RMA
**Canonical Form:** `RMA`
**Canonical Form (zh-CN):** `退货授权`
**Canonical Form (zh-TW):** `退貨授權`
**Canonical Form (vi):** *(pending)*
**Aliases:** Return Merchandise Authorization, Field Return
**Definition:** Authorization and process for returning defective products from customers or field deployments to the factory for failure analysis and quality tracking. RMA data is a critical input for post-MP quality assessment and next-generation DFT improvement.
**Do Not Confuse With:** NCR (NCR is for incoming materials; RMA is for shipped products returned from customers). Repair (Repair may occur during RMA processing, but RMA is the return/tracking process).
**Phase Context:** MP-CP6 analysis.
**Example Usage:** "Field Return/RMA Analysis Summary identifies field failure modes to feed DFT/DFX improvements for next-gen products."

---

### CAPEX
**Canonical Form:** `CAPEX`
**Canonical Form (zh-CN):** `资本性支出`
**Canonical Form (zh-TW):** `資本支出`
**Canonical Form (vi):** *(pending)*
**Aliases:** Capital Expenditure, Capital Investment
**Definition:** Expenditure to acquire, upgrade, or maintain physical assets such as test equipment, fixtures, and production machinery. In MTE, CAPEX covers test station purchases, fixture tooling, and lab equipment. Distinguished from OPEX (operational expenditure for ongoing costs like labor and consumables).
**Do Not Confuse With:** OPEX (ongoing operational costs vs. one-time capital investments). Budget (CAPEX is a specific accounting category within the budget).
**Phase Context:** P1-CP3 estimation.
**Example Usage:** "CAPEX Budget Draft in P1-CP3 estimates fixture and test equipment investment for EVT through MP."

---

## Equipment and Fixture Terms

### Fixture
**Canonical Form:** `Fixture`
**Canonical Form (zh-CN):** `测试夹具`
**Canonical Form (zh-TW):** `測試治具`
**Canonical Form (vi):** *(pending)*
**Aliases:** Test Fixture, MFG Fixture, Tooling
**Definition:** Custom mechanical/electrical interface device that connects a DUT (Device Under Test) to a test station. Fixtures include mechanical alignment, electrical contacts (pogo pins, edge connectors), and signal routing from DUT interfaces to tester resources. Fixture design is a critical NPI deliverable with long lead times.
**Do Not Confuse With:** Test station/tester (the fixture is the DUT interface; the tester is the instrument system). Jig (a jig positions parts for assembly; a fixture positions parts for testing — the terms are sometimes used interchangeably but Fixture is the canonical form in this KB).
**Phase Context:** P1-CP3 concept, EVT-CP4 prototype, DVT-CP2 qualification, PVT-MP sustained.
**Example Usage:** "Fixture Debug Report documents all hardware and contact issues encountered during EVT fixture bring-up."

---

### ERS
**Canonical Form:** `ERS`
**Canonical Form (zh-CN):** `设备需求规格`
**Canonical Form (zh-TW):** `設備需求規格`
**Canonical Form (vi):** *(pending)*
**Aliases:** Equipment Requirement Spec, Equipment Requirement Specification
**Definition:** Document specifying the functional, performance, interface, and environmental requirements for test equipment to be procured or developed. Used as the basis for vendor RFQ and equipment evaluation.
**Do Not Confuse With:** Test Plan (ERS defines what the equipment must do; Test Plan defines how tests are executed). RFQ (ERS is the internal spec; RFQ is the external request to vendors based on ERS).
**Phase Context:** P1-CP3.
**Example Usage:** "Equipment Requirement Spec defines channel count, measurement accuracy, and interface requirements for the FCT station."

---

### RFQ
**Canonical Form:** `RFQ`
**Canonical Form (zh-CN):** `询价单`
**Canonical Form (zh-TW):** `詢價單`
**Canonical Form (vi):** *(pending)*
**Aliases:** Request for Quotation
**Definition:** Formal request sent to vendors/suppliers to obtain pricing and technical proposals for equipment, fixtures, or services. RFQ responses are evaluated against vendor selection criteria to choose suppliers.
**Do Not Confuse With:** RFP (Request for Proposal — more open-ended; RFQ requests specific pricing). PO (Purchase Order — issued after RFQ evaluation and vendor selection).
**Phase Context:** P1-CP3.
**Example Usage:** "Vendor RFQ includes ERS as an attachment and requests fixture unit price, lead time, and technical approach."

---

## Software and Data Terms

### SOP
**Canonical Form:** `SOP`
**Canonical Form (zh-CN):** `标准作业程序`
**Canonical Form (zh-TW):** `標準作業程序`
**Canonical Form (vi):** *(pending)*
**Aliases:** Standard Operating Procedure
**Definition:** Detailed, step-by-step written procedure for executing a recurring task. In MTE, SOPs cover station setup, unit loading, test execution, failure handling, and shift handover. SOPs are required for all production operations.
**Do Not Confuse With:** WI (Work Instruction — WI is typically more detailed and task-specific than SOP, though the terms are sometimes used interchangeably). Test Plan (Test Plan defines what to test; SOP defines how to operate the station).
**Phase Context:** PVT-CP1, MP.
**Example Usage:** "SOP/WI documents are part of the PVT operator training package and must be in local language for factory operators."

---

### WI
**Canonical Form:** `WI`
**Canonical Form (zh-CN):** `工作指导书`
**Canonical Form (zh-TW):** `工作指導書`
**Canonical Form (vi):** *(pending)*
**Aliases:** Work Instruction
**Definition:** Detailed task-level instructions for specific manufacturing operations, typically more granular than SOPs. WIs are step-by-step guides for individual tasks (e.g., loading a DUT into a fixture, interpreting a test result screen).
**Do Not Confuse With:** SOP (SOP is process-level; WI is task-level step-by-step). Test Plan (WI is operational; Test Plan is technical specification).
**Phase Context:** PVT-CP1, MP.
**Example Usage:** "WI for FCT station loading specifies ESD handling requirements, fixture engagement sequence, and operator safety checklist."

---

### BOD / EOD
**Canonical Form:** `BOD / EOD`
**Canonical Form (zh-CN):** `班前/班后会议`
**Canonical Form (zh-TW):** `班前/班後會議`
**Canonical Form (vi):** *(pending)*
**Aliases:** Beginning of Day Report / End of Day Report, Start of Shift / End of Shift
**Definition:** Shift-level status reporting documents. BOD summarizes planned targets, open issues from previous shift, and equipment status at shift start. EOD summarizes actual production results, yield, downtime, issues encountered, and handover items.
**Do Not Confuse With:** Daily Production Report (BOD/EOD are shift-level; Daily Production Report aggregates across all shifts for management visibility).
**Phase Context:** P1-CP4 template definition, MP-CP1 daily use.
**Example Usage:** "BOD/EOD template is defined in P1-CP4 and instantiated as the BOD/EOD Report in MP daily operations."

---

### Traceability
**Canonical Form:** `Traceability`
**Canonical Form (zh-CN):** `可追溯性`
**Canonical Form (zh-TW):** `可追溯性`
**Canonical Form (vi):** *(pending)*
**Aliases:** Unit Traceability, Serial Number Traceability, Manufacturing Traceability
**Definition:** The ability to track a specific unit's complete manufacturing history — including all test results, repair events, component lots, and operator records — using its serial number as the key. Required for failure analysis, field return investigation, and regulatory compliance.
**Do Not Confuse With:** SFC (SFC is the system that enables traceability; traceability is the capability/outcome). Genealogy (genealogy tracks component provenance within a unit; traceability tracks the unit's process history).
**Phase Context:** EVT-CP3 spec, PVT-CP4 validation, MP sustained.
**Example Usage:** "Traceability Mapping Document defines the data fields, recording points, and retention policy for unit traceability."
