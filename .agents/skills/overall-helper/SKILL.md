---
name: overall-helper
description: >-
  Assists in writing, revising, evaluating, and enriching Chapter 1 (Introduction) and Chapter 2 
  (Review of Related Literature, Studies, and Systems) for any academic research, capstone, or thesis project.
  Chapter 1 coverage: Background of the Study, Objectives, Scope and Delimitation, Significance of the Study, 
  Definition of Terms, and Conceptual Framework (IPO Model). Chapter 2 coverage: RRL, RSS, Related Systems, 
  and Synthesis — using verified vault sources and rigorous academic standards.
---

# Academic Research Writing Skill — Overall Helper

## Purpose

This skill guides the agent in assisting researchers to draft, refine, or audit any section of **Chapter 1** or **Chapter 2** of an academic capstone or thesis manuscript. All drafting must be grounded in the active project profile defined in `.agents/rules/context.md`, draw from verified vault sources, and adhere to publication-grade academic writing standards.

---

## Step 0: Load Active Project Context

Before generating or revising manuscript sections, **always read the project context** from:
- `.agents/rules/context.md`

Extract:
- **Project Identity:** Title, degree program, and target institution or community locale.
- **Problem Formulation:** Macro driver, local operational bottleneck, and target stakeholders.
- **Proposed Architecture:** System tiers (Input/Edge, Network/Transport, Processing/ML, UI/Presentation).
- **Specific Objectives & Metrics:** Action verbs, deliverables, and evaluation standards (e.g., ISO/IEC 25010).

---

## Step 1: Identify Section Scope

Clarify with the user (or determine from the prompt) which chapter and section require assistance:

### Chapter 1 Sections
1. **Background of the Study** — Funnel narrative (Inverted Pyramid) moving from global context (SDGs/benchmarks) to national mandates, local institutional bottlenecks, gap synthesis (granularity, context, algorithmic, operational), and the proposed system.
2. **Objectives of the Study** — One overarching primary objective followed by enumerated, action-verb driven specific objectives (Develop, Integrate/Implement, Deploy/Design, Evaluate).
3. **Scope and Delimitation** — Clear delineation of functional/spatial/temporal boundaries (Scope) and justified exclusions (Delimitations) such as regulatory barriers, third-party constraints, or safety limits.
4. **Significance of the Study** — Distinct stakeholder impact statements detailing how each beneficiary group (e.g., institution management, staff/operators, end-users, future researchers, policy bodies) gains value.
5. **Definition of Terms** — Operational definitions defining how each technical term, variable, or metric functions specifically within the proposed system (in a single unified definition format).
6. **Conceptual Framework** — Input-Process-Output (IPO) model narrative detailing raw inputs, algorithmic/computational processes, and resulting outputs, coupled with feedback loops.

### Chapter 2 Sections
1. **Review of Related Literature (RRL)** — Synthesis of theoretical literature, industry standards, and regulatory frameworks from the vault contextualizing the study's domain.
2. **Review of Related Studies (RSS)** — Synthesis of empirical research presenting quantitative benchmarks, experimental datasets, and algorithmic findings.
3. **Review of Related Systems (RSS)** — Architectural comparison of existing software systems, prototypes, and platforms, highlighting their structural designs and operational mechanisms.
4. **Synthesis of the State of the Art** — Cross-cutting comparative matrix and narrative identifying the exact architectural and operational void filled by **the proposed system**.

---

## Step 2: Citation Discipline

- **Vault Grounding:** Prioritize sources stored in the Obsidian vault directories (`00_anotatedbibliography/` or `01_anotatedbibliography C2/`).
- **Zero Hallucination:** Never invent studies, citations, authors, or DOIs.
- **Verification:** Inspect the source's Summary and Relevance before citing to ensure alignment with the claim.
- **In-Text Citation Format:** Use formal author-date formatting: `(Author et al., Year)`.

---

## Step 3: Academic Writing Standards

Enforce these linguistic rules across every drafted sentence:

### Academic Tone & Third Person
- Strictly write in the third person. Never use "we," "our," "I," or "you."
- Refer to the project strictly as **"the proposed system"** or **"this study"**.

### Banned AI Vocabulary
Never use overused AI buzzwords:
- *delve, testament, paramount, seamless, robust, pivotal, fostering, game-changer, moreover, furthermore, beacon, cornerstone, revolutionizing, state-of-the-art, cutting-edge*

### Banned Rhetorical Patterns
- No rule-of-three cadence lists (e.g., "improves workflow, enhances accuracy, and optimizes throughput").
- No X-not-Y parallel structures. State claims directly.
- No dramatic or melodramatic closing punchlines.

### Evidence-Based Qualifiers
Use hedged academic expressions:
- *Acceptable:* "suggests," "indicates," "demonstrates an error margin of," "has been shown to"
- *Unacceptable:* "completely solves," "guarantees," "eliminates," "proves beyond doubt"

### Direct Technical Connectors
Use functional transitions (*"However," "Specifically," "In contrast," "Conversely," "Building on this"*) instead of filler (*"In today's fast-paced world"*, *"It is obvious that"*).

---

## Step 4: Chapter 1 — Section-by-Section Guidelines

### 1. Background of the Study
- Follow the 5-stage Inverted Pyramid model (Global -> National -> Local -> Gap Analysis -> Proposed Intervention).
- Ground every claim in verified literature and empirical studies from the vault.

### 2. Objectives of the Study
- Structure:
  - *General Objective:* To design, develop, and evaluate [Project Title] to [Core Purpose].
  - *Specific Objectives:*
    1. Develop/Engineer the [Tier 1 / Data Acquisition / Input component].
    2. Design/Implement the [Tier 2 & 3 / Core Engine / Algorithm / Backend pipeline].
    3. Deploy/Construct the [Tier 4 / User Interface / Dashboard / Notification system].
    4. Evaluate the proposed system in terms of [Software Quality Standard e.g., ISO/IEC 25010 (Performance Efficiency, Usability, Reliability)] and empirical performance metrics.

### 3. Scope and Delimitation
- **Scope:** Defines the active operational environment, target user population, hardware/software stack, and primary features.
- **Delimitations:** Explicitly enumerates what the system does NOT do, backed by technical, legal, or safety justifications.

### 4. Significance of the Study
- Provide dedicated paragraphs for each key stakeholder group defined in `context.md`:
  - Target Organization / Client Administration
  - Primary End-Users / Operational Staff
  - Academic Community & Future Researchers
  - Broader Industry / Socio-Economic Context

### 5. Definition of Terms
- Present terms alphabetically.
- Use a **single-definition format** that merges technical definition with concrete operational usage in the study.
- Example: **[Term Name]** — [Conceptual meaning], utilized in this study to [specific operational role/measurement within the proposed system].

### 6. Conceptual Framework
- Ground in the **Input-Process-Output (IPO)** paradigm:
  - *Input:* Hardware devices, raw data feeds, institutional records, user inputs, configuration parameters.
  - *Process:* Architectural pipeline, algorithms, data processing, security controls, development methodology (e.g., Agile), and ISO/IEC 25010 evaluation procedures.
  - *Output:* Functional platform, actionable analytics, alerts, reports, and evaluated software quality metrics.
