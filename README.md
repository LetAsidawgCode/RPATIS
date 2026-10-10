# Web-Based Real Property Tax Pre-Assessment and Assessment Support Portal

**Enhancing Transaction Efficiency and Public Service Delivery for the Municipal Assessor's Office of San Fernando**

A Capstone Project Study submitted to the Faculty of the School of Computer and Information Sciences, **University of Nueva Caceres**, in partial fulfillment of the requirements for the degree of **Bachelor of Science in Information Technology (BSIT)**.

---

## 👥 Project Proponents
- **Rizalina A. Ortega**
- **John Kenneth P. Calubad**
- **Christian Louise O. Asido**

**Research Duration:** July 2026 – November 2026  
**Target Agency / Partner:** Municipal Assessor's Office of San Fernando, Camarines Sur, Philippines  

---

## 📋 Project Overview

The Municipal Assessor's Office of San Fernando currently relies on manual ledger entries, physical record books, and paper-based tracking for:
- Real Property Tax (RPT) pre-assessments
- Tax declaration requests
- Ownership transfer verifications
- Assessment clearance generations

This legacy manual workflow causes severe administrative friction, long queues at assessment service windows, prolonged waiting times for citizens, and operational bottlenecks for assessors cross-checking physical tax maps and assessment rolls.

### Proposed Technical Intervention ("The Proposed System")
A secure, responsive 3-tier web portal designed to digitize, streamline, and accelerate real property tax transactions:
1. **Online RPT Pre-Assessment Request Module:** Allows taxpayers and property owners to submit initial transaction requirements remotely, minimizing physical counter congestion.
2. **Automated Assessment Billing Estimator:** Computes real property tax dues automatically based on declared property classifications and statutory assessment levels.
3. **Centralized Document Status & Verification Dashboard:** Provides real-time request tracking for taxpayers and office personnel.
4. **Administrative Workflow Panel:** Streamlines verification, document reviews, and processing for municipal assessors.

---

## 🏗️ System Architecture

- **Tier 1 (Presentation):** Responsive React & Tailwind CSS web interface.
- **Tier 2 (Application / Logic):** Secure backend handling business logic, pre-assessment validation rules, and automated tax computation formulas.
- **Tier 3 (Data / Database):** Centralized relational database (PostgreSQL) with Role-Based Access Control (RBAC) and data encryption compliant with Republic Act No. 10173 (Data Privacy Act of 2012).

---

## 🎯 Objectives & Evaluation

- **General Objective:** Determine the operational and technical feasibility of designing, developing, and evaluating the portal to enhance transaction efficiency and public service delivery.
- **Methodological Framework:** Input-Process-Output (IPO) Model developed through Agile iterative sprints.
- **Evaluation Standards:**
  - **ISO/IEC 25010 Software Quality Standards:** Functional Suitability, Performance Efficiency, Usability, Security, and Maintainability.
  - **Quantitative Benchmarks:** Processing time efficiency (analyzed via Paired t-test) and billing calculation accuracy (%).

---

## 🤖 AI Agent Research Framework (`.agents/`)

This repository includes a standardized configuration for academic research agents:
- **`rules/context.md`:** Active research profile, architectural parameters, and study boundaries.
- **`rules/mandatory-primary-source-reading.md`:** Rigorous primary-source reading and zero-hallucination protocols.
- **`rules/vault-entry-format.md`:** Obsidian vault and ACM citation formatting standards.
- **`skills/`:** Reusable academic skills for drafting Chapter 1 (Background, Objectives, Scope, Terms, IPO Model) and Chapter 2 (RRL, RSS, Related Systems, Synthesis).
- **`workflows/`:** Step-by-step literature sourcing and annotation workflows.
