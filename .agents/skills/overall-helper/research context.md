# Active Research Context: Real Property Assessment Tracking and Inter-Office Synchronization System

## 1. Project Title & Identity

**Needs Assessment for a Real Property Assessment Tracking and Inter-Office Synchronization System: Resolving Disconnected Records and Workflow Delays in Municipal Assessor and Treasurer Offices in Pasacao**

A Capstone Project Study  
Presented to the Faculty of the School of Computer and Information Sciences  
University of Nueva Caceres  

In Partial Fulfillment of the Requirements for the Degree of  
**BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY**

**Proponents:**
- Rizalina A. Ortega
- John Kenneth P. Calubad
- Christian Louise O. Asido

**Research Period:** July 2026 – December 2026

---

## 2. Problem Domain & Operational Urgency

- **Partner Agencies / Sites:** Municipal Assessor's and Treasurer's Offices in the municipalities of Canaman, Magarao, and San Fernando, with the community of Pasacao as the primary benchmark and interview site for comparative evaluation.
- **Problem Domain:** Inter-office data synchronization, municipal real property assessment tracking, and local e-governance workflow automation.
- **Operational Reality & Bottlenecks:**
  - LGUs in Camarines Sur operate entirely on disconnected workflows between the Municipal Assessor's Office and the Municipal Treasurer's Office — tracking tax payments and cross-checking assessment rolls requires tedious manual effort.
  - Decades-old legacy records (dating back to 1949) remain in physical form, creating major migration and reconciliation overhead.
  - Even in Pasacao — which already uses a localized eRPT system — a Transfer of Assessment still takes over 7 days to fully process due to disconnected workflow steps.
  - In Canaman, assessing a new building requires days of preparation followed by 7–14 days of waiting for physical, paper-based approvals to be routed to the Provincial Capitol in Pili.
  - Manual cross-checking bottlenecks cause document processing latency, record reconciliation delays, and inter-office communication lags.
- **Institutional Alignment:**
  - UN SDG 9 (Industry, Innovation and Infrastructure) & SDG 16 (Peace, Justice, and Strong Institutions).
  - UNC Institutional Research Agenda on Digital Innovation and Public Systems Modernization.
  - Data Privacy Act of 2012 (RA 10173).

---

## 3. The Proposed System Architecture & Features

- **Standard Referent:** **"the proposed system"**
- **System Name (Product):** Real Property Assessment Tracking and Inter-Office Synchronization System
- **3-Tier Web Architecture:**
  - *Presentation Tier (Frontend):* Web browser interfaces for Assessor evaluation screens, Treasurer tax payment validation views, and document tracking monitors.
  - *Application Tier (Backend):* Handles assessment data routing, user access permissions, and departmental data integration logic linking property valuations to tax collection records.
  - *Data Tier (Database):* Centralized relational database storing synchronized property records, active assessment statuses, and transaction logs.
- **Core Modules:**
  1. *Needs Assessment & Comparative Evaluation Module:* Documents operational frictions and system requirements across Pasacao, Canaman, Magarao, and San Fernando.
  2. *Assessment Request Routing & Document Tracking Module:* Bridges municipal-treasury data silos and automates assessment document routing with real-time status monitoring.
  3. *Tax Payment Synchronization Module:* Eliminates manual cross-checking between the Assessor's and Treasurer's offices by synchronizing property assessment records with tax collection data.
  4. *Administrative Workflow Panel:* Allows personnel to monitor assessment statuses in real-time and manage inter-office data synchronization views.

---

## 4. Objectives of the Study

- **General Objective:** Determine the operational and technical feasibility of designing and developing a system that addresses the disconnected inter-office workflows and manual record-keeping bottlenecks in the Municipal Assessor's and Treasurer's Offices.
- **Specific Objectives:**
  1. Conduct a needs assessment and comparative evaluation of local municipal workflows between Pasacao, Canaman, Magarao, and San Fernando to document specific operational frictions and system requirements.
  2. Develop a web-based Real Property Assessment Tracking and Inter-Office Synchronization System to bridge municipal-treasury data silos and automate assessment document routing.
  3. Conceptualize and specify an integrated inter-office web portal framework that facilitates end-to-end document tracking, allowing personnel to monitor assessment statuses in real-time and eliminating the need for manual cross-checking between departments.

---

## 5. Methodology & Evaluation Framework

- **Research Design:** Mixed-Methods Comparative Evaluation Design combining quantitative workflow time-motion metrics with qualitative survey evaluations.
- **Conceptual Framework:** Input-Process-Output (IPO) Model.
- **Theoretical Foundation:** ISO/IEC 25010 Software Quality Standard.
- **Development Model:** Agile Development Methodology (iterative two-week sprints).
- **Experimental & Statistical Design:**
  - *Independent Variable:* Implementation of the Real Property Assessment Tracking and Inter-Office Synchronization System (replacing fragmented manual ledgers and disconnected departmental files).
  - *Quantitative Dependent Variables:*
    - Document Processing Latency: Average time (in days or hours) to process assessment transactions (e.g., Transfer of Assessment).
    - Record Reconciliation Time: Time required to cross-check tax payments and verify assessment rolls between both offices.
    - ISO/IEC 25010 Software Quality Scores: Functional Suitability, Performance Efficiency, Usability, Security, and Reliability (5-point Likert scale, Weighted Mean).
  - *Statistical Methods:* Frequency Count and Percentage (demographic profiling), Weighted Mean (ISO survey scores), Comparative Mean Analysis (processing time reduction).
  - *Qualitative Parameters:* Staff feedback on inter-office workflow ease, document tracking visibility, and operational acceptability.

---

## 6. Scope & Delimitations

- **Scope:** Comparative evaluation across Pasacao (primary benchmark), Canaman, Magarao, and San Fernando; covers inter-office assessment tracking, document routing, tax payment synchronization, and administrative workflow management; involves pilot deployment with staff from both Municipal Assessor's and Treasurer's Offices.
- **Delimitations:** Restricted to assessment tracking and inter-office synchronization (excludes electronic payment collection or fund gateway processing); RA 10173 compliance maintained using mock/masked dummy data during development and encrypted RBAC-controlled data during field deployment; parallel run phase ensures data safety and service continuity during evaluation.

---

## 7. Baseline Vault Source Index

| File / Source | Citation Key | Category | Core Contribution / Findings |
|---|---|---|---|
| Mendoza (2025) | Mendoza, 2025 | Related Study local | Demonstrates that computer-assisted assessment significantly improves processing efficiency, calculation accuracy, transparency, and accountability compared to legacy manual methods. DOI: 10.47119/IJRP1001731520257969 |
| Santos & Reyes (2024) | Santos & Reyes, 2024 | Related Study local | Highlights that administrative friction, valuation delays, and fragmented record-keeping severely hinder local treasury operations, and that digital tracking tools are essential to resolve processing backlogs. |
