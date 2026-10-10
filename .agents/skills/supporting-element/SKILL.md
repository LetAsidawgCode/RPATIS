---
name: supporting-element
description: >-
  Extracts four standardized contextual building blocks (Empirical Evidence / Problem Anchor,
  Technical & Architectural Precedent, Implementation Limitation / Operational Barrier,
  and a 2-Sentence Chapter 1 Synthesis Snippet) from any research publication, empirical study,
  or system to ground Chapter 1 and Chapter 2 for any capstone or thesis project.
---

# Extracting Chapter 1 & 2 Supporting Elements

## Purpose

This skill guides the agent to act as an academic research adviser specializing in applied computing, software engineering, and systems research. It ingests any cited literature, empirical study, or existing system and extracts four standardized contextual building blocks aligned to the active project defined in `.agents/rules/context.md`.

---

## Step 0: Active Project Grounding

Before analyzing the source, read the active project configuration in:
- `.agents/rules/context.md`

Identify:
- **Project Title & Domain:** What domain is the active project investigating?
- **Target Institution / Locale / Community:** Where is the problem situated?
- **Core Technological Stack:** What hardware, backend, ML model, or interface tier is proposed?
- **Evaluation Criteria:** What metrics or software quality standards (e.g., ISO/IEC 25010) are measured?

---

## Step 1: Extraction Protocol

Analyze the source text provided and extract the four building blocks using this exact format:

### 1. Concrete Empirical Evidence / Problem Anchor (For Background & Problem Statement):
- What specific quantitative metrics, real-world baseline failure rates, operational inefficiencies, financial costs, or statistical evidence does this source document that proves traditional, manual, or status-quo workflows fail in this domain?

### 2. Technical & Architectural Precedent (For Specific Objectives & Methodology):
- What specific hardware, system architectures, network protocols, algorithmic models, data structures, or evaluation standards (e.g., ISO/IEC 25010, benchmark datasets) does this work validate that justifies the engineering and design choices of the proposed system?

### 3. Implementation Limitation / Operational Barrier (For Justifying Our Contribution):
- What practical constraint, technical bottleneck, or operational boundary did this prior work encounter (e.g., high deployment cost, computational/memory overhead, excessive latency, lack of domain/context integration, reliance on manual configuration, proprietary lock-in, or narrow testing environments)?
- *Note:* Frame this strictly as an operational or engineering challenge, not just a generic "gap."

### 4. 2-Sentence Chapter 1 Synthesis Snippet:
- Provide a polished, publication-ready two-sentence narrative excerpt written strictly in the third person that seamlessly cites this source to directly support the proposed system's Chapter 1 Background or Problem Statement.
