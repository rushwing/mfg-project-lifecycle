MTE 生命周期（NPI → MP）

├── P1（Concept / Feasibility / Pre-NPI）
│   ├── Checkpoint 1：需求澄清与可测试性输入
│   │   ├── PRD / MRD（产品/市场需求文档）
│   │   ├── HW Spec / System Spec（硬件/系统规格书）
│   │   ├── DFT Requirement / DFX Requirement
│   │   ├── Test Strategy Overview
│   │   └── Risk List / Open Issue List
│   │
│   ├── Checkpoint 2：测试架构与站位规划
│   │   ├── MFG Test Architecture Spec
│   │   ├── Station Flow Diagram / Test Flow Diagram
│   │   ├── High-Level Test Coverage Matrix
│   │   ├── Test Equipment List
│   │   └── Capacity Planning Draft / UPH Estimation Draft
│   │
│   ├── Checkpoint 3：夹具/设备/供应商前期评估
│   │   ├── Fixture Concept Proposal
│   │   ├── Equipment Requirement Spec（ERS）
│   │   ├── Vendor RFQ / Vendor Selection Criteria
│   │   ├── Fixture Feasibility Review Notes
│   │   └── CAPEX Budget Draft
│   │
│   └── Checkpoint 4：项目机制建立
│       ├── NPI Build Plan（初版）
│       ├── BOD / EOD Template
│       ├── RAID Log（Risk/Action/Issue/Dependency）
│       ├── Version Control Plan（HW/SW/Test）
│       └── Program Milestone Tracker
│
├── EVT（Engineering Validation Test）
│   ├── Checkpoint 1：样机回片与基础 bring-up
│   │   ├── EVT Build Plan
│   │   ├── Board Bring-up Checklist
│   │   ├── Test Readiness Checklist
│   │   ├── Golden Sample Definition
│   │   └── HW/SW/FW Version Matrix
│   │
│   ├── Checkpoint 2：测试需求冻结与方案细化
│   │   ├── TRP（Test Requirement Plan / Test Readiness Plan，依公司叫法）
│   │   ├── Test Plan（ICT/FCT/DIAG）
│   │   ├── Test Coverage Matrix（详细版）
│   │   ├── Failure Criteria / Pass-Fail Criteria
│   │   └── Test Case List / Test Item Spec
│   │
│   ├── Checkpoint 3：测试框架导入与初版程序开发
│   │   ├── Test Framework Integration Plan
│   │   ├── SW Architecture for MFG Test
│   │   ├── DIAG Development Plan
│   │   ├── Logging & Traceability Spec
│   │   └── SFC Interface Requirement
│   │
│   ├── Checkpoint 4：夹具打样与设备联调
│   │   ├── Fixture Design Spec
│   │   ├── Fixture BOM
│   │   ├── Fixture Debug Report
│   │   ├── Equipment Setup Instruction
│   │   └── Vendor Action Tracker
│   │
│   └── Checkpoint 5：问题管理与阶段总结
│       ├── EVT Daily Build Report
│       ├── Defect Tracking List / Bug List
│       ├── Root Cause Analysis Report（初版）
│       ├── EVT Exit Criteria Review
│       └── EVT Phase Summary Report
│
├── DVT（Design Validation Test）
│   ├── Checkpoint 1：测试完整性提升
│   │   ├── DVT Build Plan
│   │   ├── Updated TRP / Test Plan
│   │   ├── Detailed Coverage Report
│   │   ├── Test Gap Analysis
│   │   └── Diagnostic Enhancement Plan
│   │
│   ├── Checkpoint 2：治具/设备定版与重复性验证
│   │   ├── Fixture Qualification Plan
│   │   ├── GR&R Report（Gauge R&R）
│   │   ├── Fixture Acceptance Report
│   │   ├── Equipment Calibration Plan
│   │   └── Preventive Maintenance Plan
│   │
│   ├── Checkpoint 3：软件版本管理与可发布性
│   │   ├── Release Note（Test SW / FW / DIAG）
│   │   ├── Version Release Plan
│   │   ├── Configuration Control Matrix
│   │   ├── Software Change Log
│   │   └── ECO/ECN Impact Assessment
│   │
│   ├── Checkpoint 4：UPH 与产能评估
│   │   ├── UPH Study Report
│   │   ├── Cycle Time Breakdown
│   │   ├── Station Loading Analysis
│   │   ├── Headcount / Machine Planning Sheet
│   │   └── Bottleneck Analysis Report
│   │
│   ├── Checkpoint 5：失效分析与良率改善
│   │   ├── FA Request / FA Report
│   │   ├── Pareto Report
│   │   ├── Yield Trend Report
│   │   ├── Retest Analysis Report
│   │   └── Corrective Action Plan（CAPA）
│   │
│   └── Checkpoint 6：阶段退出评审
│       ├── DVT Exit Criteria Checklist
│       ├── Open Issue Closure Plan
│       ├── DVT Summary Report
│       └── PVT Readiness Review Deck
│
├── PVT（Production Validation Test）
│   ├── Checkpoint 1：量产流程验证
│   │   ├── PVT Build Plan
│   │   ├── Mass Production Test Flow
│   │   ├── SOP / WI（作业指导书）
│   │   ├── Operator Training Material
│   │   └── Line Qualification Plan
│   │
│   ├── Checkpoint 2：工厂导入与站位验证
│   │   ├── Line Bring-up Checklist
│   │   ├── Site Readiness Checklist
│   │   ├── Tester Installation Qualification（IQ）
│   │   ├── Operational Qualification（OQ）
│   │   └── Production Sign-off Checklist
│   │
│   ├── Checkpoint 3：良率/效率/稳定性验证
│   │   ├── PVT Yield Report
│   │   ├── UPH Validation Report
│   │   ├── Downtime Report
│   │   ├── Escape / Leakage Analysis
│   │   └── False Fail / Retest Reduction Report
│   │
│   ├── Checkpoint 4：SFC / Traceability / 数据闭环
│   │   ├── SFC Validation Report
│   │   ├── Traceability Mapping Document
│   │   ├── Data Upload Validation Report
│   │   ├── Serial Number Control Plan
│   │   └── Repair / Rework Flow Spec
│   │
│   ├── Checkpoint 5：量产签核
│   │   ├── PVT Exit Report
│   │   ├── MP Release Recommendation
│   │   ├── Control Plan
│   │   ├── Contingency Plan / Escalation Plan
│   │   └── Handover Package to Factory Ops
│   │
│   └── Checkpoint 6：阶段复盘
│       ├── PVT Lessons Learned
│       ├── Open Issues for MP Tracker
│       └── Phase Retrospective Notes
│
└── MP（Mass Production）
    ├── Checkpoint 1：量产日常运营
    │   ├── Daily Production Report
    │   ├── BOD / EOD Report
    │   ├── WIP / Input-Output Report
    │   ├── Yield Dashboard
    │   └── Downtime / Escalation Log
    │
    ├── Checkpoint 2：版本与变更管理
    │   ├── MP Release Note
    │   ├── Change Management Log
    │   ├── ECO/ECN Implementation Tracker
    │   ├── Test Program Revision History
    │   └── Golden Unit Maintenance Record
    │
    ├── Checkpoint 3：来料与异常管理
    │   ├── Incoming Quality Report / IQC Report
    │   ├── Supplier Issue Tracker
    │   ├── NCR / MRB Report
    │   ├── Component Risk Assessment
    │   └── Containment Action Report
    │
    ├── Checkpoint 4：持续改善
    │   ├── Yield Improvement Plan
    │   ├── Cost Reduction Plan
    │   ├── Test Time Optimization Report
    │   ├── Station Consolidation Proposal
    │   └── Preventive Action Plan
    │
    ├── Checkpoint 5：项目收尾与知识沉淀
    │   ├── MP Phase Summary Report
    │   ├── Final Lessons Learned
    │   ├── Best Practice / Playbook
    │   ├── Knowledge Base Update
    │   └── Project Closure Report
    │
    └── Checkpoint 6：下一代产品反馈
        ├── DFT/DFX Feedback Report
        ├── Field Return / RMA Analysis Summary
        ├── Test Escape Summary
        └── NPI Feedback to Design Team
