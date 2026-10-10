---
name: write-background-of-the-study
description: >-
  Standardized protocol and guide for drafting, refining, and evaluating the "Background of the Study" 
  for academic research, capstone, and thesis manuscripts in strict accordance with the University 
  of Nueva Caceres (UNC) Research Manual (Revised Edition 2025, Chapter 8). Use this skill whenever 
  the user asks to write, structure, or improve the Background of the Study or Chapter 1 Introduction for any project.
---

# Writing the Background of the Study: UNC Academic Standard

This skill encapsulates the formal procedure, structural architecture, and quality standards for drafting a publication-grade **Background of the Study** in accordance with the **University of Nueva Caceres (UNC) Research Manual (Revised Edition 2025, Chapter 8: The University Research Format, pp. 91–92)**.

---

## 1. Core Functions of the Background

According to the UNC Research Manual, the Background of the Study is the opening foundation of the manuscript and must fulfill four critical functions:

1. **Provide Context:** Establish the current state of knowledge using empirical data and cited literature from credible international and local sources.
2. **Connect Real-World & Local Issues:** Anchor the study in pressing practical, economic, operational, or social challenges, specifically highlighting how they manifest within the target local community, institution, or industry setting.
3. **Identify the Gap:** Synthesize previous studies to expose limitations, conflicting findings, technological trade-offs, or unaddressed operational blind spots that justify the research.
4. **Frame the Research Problem:** Formulate the specific operational bottleneck addressed, demonstrating why existing approaches fail and leading directly into the proposed technical intervention.

---

## 2. The Five Essential Questions

A well-crafted Background of the Study must answer the following five questions within **3 to 4 pages**:

| # | Question | Drafting Focus |
|---|---|---|
| **1** | *What is the topic of your research?* | Clearly define the domain, technological scope, and core subject matter. |
| **2** | *What led you to your study? Why is this problem worth studying?* | Document the catalyst, real-world urgency, operational costs, inefficiency, and impact on stakeholders. |
| **3** | *What was previously known about this topic?* | Cite past literature, empirical studies, and systems being built upon or distinguished from. |
| **4** | *How will your research add to existing knowledge?* | Articulate the unique technical, algorithmic, or architectural contribution filling the identified gap. |
| **5** | *What are the potential implications?* | Outline both theoretical contributions (e.g., algorithmic evaluation, models) and practical stakeholder utility. |

---

## 3. Structural Architecture: The "Inverted Pyramid" Model

The UNC Research Manual explicitly mandates an **Inverted Pyramid (Funnel)** structure, moving progressively from broad global concepts down to specific institutional applications.

```
┌────────────────────────────────────────────────────────────────────────┐
│ STAGE 1: GLOBAL CONTEXT (Macro Level)                                  │
│ - Global landscape, international trends, and universal imperatives    │
│ - United Nations Sustainable Development Goals (SDGs) or global norms  │
│ - International peer-reviewed literature and benchmark empirical data  │
├────────────────────────────────────────────────────────────────────────┤
│ STAGE 2: NATIONAL & REGULATORY CONTEXT (Meso Level)                    │
│ - Philippine statutory mandates, national laws, and agency directives  │
│ - National socio-economic conditions, domestic sector challenges       │
│ - Studies conducted in Philippine institutions, industries, or agencies│
├────────────────────────────────────────────────────────────────────────┤
│ STAGE 3: LOCAL & INSTITUTIONAL CONTEXT (Micro Level - Sharpen Focus)   │
│ - Target operational reality (target university, client, or locale)    │
│ - Local workflows, administrative blind spots, manual inspection limits│
│ - Documenting concrete operational bottlenecks or workflow failures    │
├────────────────────────────────────────────────────────────────────────┤
│ STAGE 4: CRITICAL SYNTHESIS OF RESEARCH GAPS                           │
│ - Why existing commercial or academic solutions are insufficient       │
│ - Categorize gaps: Granularity, Context, Algorithmic, Operational      │
│ - Expose the exact technical void the study resolves                   │
├────────────────────────────────────────────────────────────────────────┤
│ STAGE 5: THE PROPOSED INTERVENTION & STAKEHOLDER RATIONALE             │
│ - Introduce "the proposed system" and its core architectural tiers     │
│ - Input/Edge + Network/Transport + Processing/ML + UI/Dashboard tiers  │
│ - Direct value delivery to targeted stakeholder groups & beneficiaries │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Step-by-Step Execution Protocol

When drafting the Background of the Study, execute the following systematic procedure:

### Step 0: Read the Active Project Context
Before drafting, inspect `.agents/rules/context.md` to extract:
- Project title, domain, and target institution/community
- Core operational bottlenecks and regulatory drivers
- Proposed architectural tiers and specific evaluation criteria (e.g., ISO/IEC 25010)

### Step 1: Work Backward from the Thesis Statement
- Formulate the precise core thesis statement: *"To solve [Target Bottleneck], the proposed system implements [Core Technological Innovation] for [Target Stakeholders] to achieve [Measurable Outcome]."*
- Use this statement to determine exactly what prior literature and national policies must be established in the opening paragraphs.

### Step 2: Assemble Evidence from the Vault Categories
Cross-reference evidence from the vault bibliography quadrants:
- **Global / Policy:** [[Related Literature international]] & [[Related Literature local]]
- **Empirical Baseline:** [[Related Study international]] & [[Related Study local]]
- **Existing Prototypes & Competitors:** [[Related System international]] & [[Related System local]]

### Step 3: Draft by Pyramid Stage

#### Stage 1: Global Context
- Open with high-level socio-technical, environmental, or technological trends.
- Frame the problem through global accords (e.g., UN SDGs) and international peer-reviewed literature.
- *Active tone:* Describe real-world challenges faced globally rather than dictionary definitions.

#### Stage 2: National Context
- Transition to the Philippine setting using functional connectors (e.g., *"In the Philippine institutional landscape...", "Under national statutory mandates..."*).
- Cite governing Republic Acts, department administrative orders, or regulatory frameworks.
- Highlight national economic, operational, or infrastructure realities.

#### Stage 3: Local / Institutional Context
- Narrow the lens to the specific study locale, client organization, or campus identified in `context.md`.
- Contrast macro-level administrative policies with micro-level operational realities.
- Introduce concrete human, organizational, or behavioral factors (e.g., reliance on manual logs, delayed discovery, lack of departmental accountability).
- Quantify or qualify the operational bottleneck currently occurring.

#### Stage 4: Critical Synthesis of Gaps
Categorize the failure of past solutions into clear analytical gap archetypes:
1. **Granularity Gap:** Existing tools or practices provide only aggregate, high-level summaries; localized, fine-grained telemetry or itemized tracking is absent.
2. **Contextual / Semantic Gap:** Existing systems log raw data without correlating operational context (e.g., schedules, user permissions, environmental conditions), leading to false interpretations.
3. **Algorithmic / Technical Gap:** Traditional approaches rely on rigid manual thresholds or heavy models that yield unacceptable false alarms, high latency, or excessive computational overhead.
4. **Operational / Workflow Gap:** Feedback loops are retrospective and delayed (e.g., post-event audits or monthly reports), preventing timely, proactive intervention.

#### Stage 5: The Proposed System & Impact
- Formally present the technical architecture of **the proposed system**.
- Detail the multi-tier pipeline (as defined in `context.md`: Input/Edge tier, Transport tier, Backend/Processing/ML tier, and UI/Governance tier).
- Conclude with the theoretical and evaluation grounding (e.g., IPO Model, software engineering methodology, and ISO/IEC 25010 Software Quality Standards).

---

## 5. Style, Tone, and Linguistic Constraints

Adhere strictly to UNC's editorial guidelines and project rules:

1. **Active Voice:** Prioritize active construction (e.g., *"The proposed system processes real-time telemetry"* instead of *"Real-time telemetry is processed by the proposed system"*).
2. **Third-Person Academic Tone:** Strictly avoid first-person pronouns (*I, we, our, the researchers*).
3. **Strict Referencing Directive:** Always identify the project strictly as **"the proposed system"** (never use informal product names, "our app", or colloquial abbreviations).
4. **No Filler Words:** Eliminate decorative rhetoric (*"In this modern fast-paced world..."*, *"Since time immemorial..."*). Every sentence must deliver context, evidence, or critical argumentation.
5. **In-Text Citation Standard:** Integrate formal citations in APA author-date format (e.g., *Santos et al., 2024; Department of Science and Technology, 2023*).

---

## 6. Background Evaluation Checklist

Before finalizing any Background of the Study draft, verify against this rubric:

- [ ] Does it start with a global perspective and international benchmarks/SDGs?
- [ ] Does it cite relevant Philippine legal, statutory, or regulatory mandates?
- [ ] Does it clearly define the local problem at the target institution/community from `context.md`?
- [ ] Does it explicitly articulate the 4 research gaps (granularity, context, algorithmic, operational)?
- [ ] Does it refer to the project strictly as "the proposed system"?
- [ ] Are the proposed system's multi-tier architecture and evaluation standard (e.g., ISO/IEC 25010) explicitly specified?
- [ ] Is it written in active voice and third-person perspective?
- [ ] Is the length concise and substantive (targeting 3 to 4 pages)?
