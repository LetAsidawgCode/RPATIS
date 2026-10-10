---
name: write-annotated-bibliography
description: >-
  Standardized protocol and master guide for sourcing, structuring, expanding, and synthesizing
  annotated bibliography entries and literature matrices for Chapter 1 and Chapter 2 in strict
  accordance with the University of Nueva Caceres (UNC) Research Manual (Revised Edition 2025,
  Chapter 8), the Quamet Rubric 26-27 (100-point standard), and mandatory writing style and
  humanization constraints. Chapter 2 is the permanent active default mode.
---

# Master Annotated Bibliography Skill (UNC Academic & Quamet Standard)

This master skill defines the standardized protocol for creating, expanding, formatting,
and evaluating **Annotated Bibliography Entries** and **Literature Matrices** for:
- **Chapter 2: Review of Related Literature, Studies, and Systems & Synthesis (PERMANENT ACTIVE DEFAULT)**
- **Chapter 1: Introduction & Theoretical Grounding (Archival / Explicit Override Only)**

All entries are strictly evaluated against the **Quamet Rubric 26-27 (100-point standard)**,
grounded in the **University of Nueva Caceres (UNC) Research Manual (Revised Edition 2025, Chapter 8)**,
and compliant with **`.agents/rules/writing-style-humanization.md`**.

---

## 0. Operating Mode Selector & Automatic Default Rule

> **CRITICAL ROUTING DIRECTIVE (NO PROMPT REPETITION NEEDED):**  
> **Chapter 2 is the PERMANENT ACTIVE DEFAULT MODE.**  
> Because Chapter 1 has been fully compiled and submitted, **all incoming requests** to source,
> write, expand, format, or audit bibliography entries **MUST automatically execute in Chapter 2 Mode**
> without requiring the user to specify "C2" or "Chapter 2".  
> **Chapter 1 Mode is ONLY executed if the user explicitly specifies "for Chapter 1" or "for C1".**

| Feature | Chapter 2 Mode (**ACTIVE DEFAULT**) | Chapter 1 Mode (*Explicit Request Only*) |
|---|---|---|
| **Vault Directory** | `01_anotatedbibliography C2/` | `00_anotatedbibliography/` |
| **Category Wikilinks** | `[[<Category Name> C2]]` | `[[<Category Name>]]` |
| **Parent Hub Link** | `[[Bibliography C2]]` | `[[Bibliography]]` |
| **Relevance Scope** | **5-Layer Deep Method:** Architectural Tier + Module Justification + Authors' Stated Limitations + Proposed System Resolution + Quamet Check | **1-2 Sentence Problem Anchor:** Urgent real-world bottleneck or conceptual framework anchor |
| **Source References** | **Minimum 2 grounded sub-bullets:** (1) tech specs/empirical findings, (2) authors' explicit limitation | 1+ sub-bullets for baseline grounding |
| **Chapter Bridge** | Bridges to RRL, RSS, Related Systems, and the **Comparative Synthesis Matrix** | Bridges to Background (Inverted Pyramid), Objectives, and IPO Framework |

---

## 1. Mandatory Pre-Writing Protocol

Before generating or updating any bibliography entry, execute these steps in order:

1. **Load Active Project Context:** Read `.agents/rules/context.md` for active system title, 3-tier architecture, research variables, and target LGU profile (Pasacao benchmark; Canaman, Magarao, San Fernando).
2. **Follow Chapter 1 Master Source Parity & Order:** Sourced directly from `context/md/Chapter 1 Annotated Bibliography.md`. For Chapter 2, strictly follow the exact 1-to-45 sequential order established in Chapter 1 across categories (Related Literature 1–15, Related Studies 1–15, Related Systems 1–15) to ensure 1-to-1 alignment between chapters.
3. **Primary Source Verification:** Follow `.agents/rules/mandatory-primary-source-reading.md`. Retrieve the actual text via `read_url_content`, DOI resolvers, or university repositories. **Never** rehash vault notes, abstracts, or metadata snippets alone.
4. **Mandatory Direct Document URL Protocol:** The ACM citation URL MUST point directly to the specific document (specific PDF, official gazette issuance page, or journal DOI landing page). **NEVER use generic root domains or homepages** (`https://arta.gov.ph/`, `https://dict.gov.ph/`, etc.). Every URL must be tested and verified as live and accessible.
5. **Enforce Humanization Rules:** Read `.agents/rules/writing-style-humanization.md`. Enforce sentence burstiness, break repetitive opening formulas, eliminate all banned AI transition words, and adopt an authentic, pragmatic researcher voice.

---

## 2. Vault Taxonomy & Directory Routing

Entries must be classified into one of the six standardized categories:

| Category Hub (C2 Default) | Target Vault Directory | Primary Role |
|---|---|---|
| `[[Related Literature international C2]]` | `01_anotatedbibliography C2/Related-Literature international/` | International theoretical frameworks, e-governance standards (UN SDGs, ISO/LADM), and public sector software architectures. |
| `[[Related Literature local C2]]` | `01_anotatedbibliography C2/Related-Literature local/` | Philippine statutory frameworks (RA 7160, RA 10173, RA 12001), administrative circulars (ARTA, NPC), and national masterplans (DGMP, PeGIF). |
| `[[Related Study international C2]]` | `01_anotatedbibliography C2/Related-Study international/` | International empirical research presenting measured datasets, algorithms, and quantitative evaluations. |
| `[[Related Study local C2]]` | `01_anotatedbibliography C2/Related-Study local/` | Philippine empirical studies on municipal assessor/treasurer workflows, transaction turnaround times, and local e-readiness. |
| `[[Related System international C2]]` | `01_anotatedbibliography C2/Related-System international/` | Working software platforms, valuation portals, and digital land registries developed abroad. |
| `[[Related System local C2]]` | `01_anotatedbibliography C2/Related-System local/` | Philippine LGU property assessment portals, eRPT platforms (Pasacao benchmark), eLGU systems, and municipal workflow platforms. |

*(For Chapter 1 explicit requests, substitute target directory `00_anotatedbibliography/` and omit ` C2` from the hub wikilink).*

---

## 3. Entry Formulation Protocol

### A. Presentation Format (User Delivery)
```text
**[Number]. [Full Title]**

**[Full ACM Citation in bold with Author(s), Year, Title, Publication Venue, and direct DOI/URL]**

Summary: [1-sentence dense summary: problem, methodology/architecture, and primary finding]

Relevance: [Third-person statement detailing functional architecture, module justification, authors' stated limitations, and proposed system resolution—written with concrete mechanisms, NOT repetitive tier boilerplate]
```

> **Presentation Directives:**
> - **Uniform Body Font:** Always format the entry title as plain bold body text (`**[Number]. [Full Title]**`). **NEVER** use Markdown headings (`#`, `##`, `###`) so that when the user pastes the entry into word processors or Google Docs, the font size remains identical to the body text.
> - **No Cluttered Vault Previews:** Do not output redundant Markdown vault codeblocks in the chat unless explicitly requested. Provide the clean, copy-paste-ready entry directly and save the vault markdown file behind the scenes upon approval.

### B. Obsidian Vault Markdown Structure (File Storage)
```markdown
# [Paper / System / Literature Full Title]

**Category:** [[<Category Hub Name C2>]]

**[Full ACM Citation in bold with Author(s), Year, Title, Publication Venue, and direct DOI/URL link]**

- **Summary:** [1-sentence dense summary: problem, methodology/architecture, and primary finding]

- **Relevance:** [Third-person multi-sentence statement applying the 5-Layer Method:
  (1) Names the specific architectural and functional mechanisms of the proposed system (without repetitive tier labels),
  (2) Names the specific functional module justified,
  (3) Cites the authors' own stated limitations or trade-offs from the primary text,
  (4) Explains how the proposed system specifically resolves those limitations]

- **Source Reference(s):**
  - _[Section / Page / Table 1]:_ [Specific finding, technical parameter, or direct quote]
  - _[Section / Page / Table 2]:_ [Specific authors' limitation, architectural detail, or metric]
```

---

## 4. The 5-Layer Relevance Method (Chapter 2 Depth Standard)

Every Chapter 2 Relevance section must satisfy all five layers while maintaining natural, academic prose:

1. **Layer 1 — Architectural Mechanism Mapping (No Formulaic Tier Jargon):**
   - **STRICTLY PROHIBITED:** Never repeatedly paste formulaic strings like *"substantiates Tier 1 (Presentation Tier)"* or *"informs Tier 2 (Application and Business Logic) and Tier 3 (Relational Database)"* across entries. This reads as repetitive AI boilerplate.
   - **REQUIRED APPROACH:** Describe the architectural mechanisms directly using concrete, tangible engineering terms:
     - *Presentation/Interface Layer:* Browser-based assessment evaluation screens, treasury verification views, citizen tax order retrieval interfaces.
     - *Application/Logic Layer:* Assessment document routing engine, role-based access control, event-triggered inter-office data pipelines, provincial escalation monitors.
     - *Data/Storage Layer:* Centralized relational property database, synchronized valuation-collection ledgers, audit logging repositories.
     - *Evaluation Layer:* ISO/IEC 25010 software quality benchmarks (performance efficiency, usability, security).
2. **Layer 2 — Module-Level Justification:** Map to one of the four core functional modules:
   - *Needs Assessment & Comparative Evaluation Module*
   - *Assessment Request Routing & Document Tracking Module*
   - *Tax Payment Synchronization Module*
   - *Administrative Workflow Panel*
3. **Layer 3 — Authors' Stated Limitation (Primary Source Only):** Cite the exact limitation, blind spot, or operational trade-off acknowledged by the authors in the Discussion, Conclusion, or Limitations section of the primary text.
4. **Layer 4 — Proposed System Resolution:** Explicitly state how the proposed system's technical design or workflow model overcomes that limitation.
5. **Layer 5 — Quamet Alignment Check:** Verify the entry anchors to established theories, demonstrates deep synthesis, and connects directly to the study's variables.

---

## 5. Writing Style & Humanization Constraints

Ground all writing in `.agents/rules/writing-style-humanization.md`:

1. **Sentence Burstiness & Cadence:** Vary sentence lengths. Avoid uniform 20–25 word blocks. Follow an 8-word punchy statement with a 35-word complex sentence. Mix compound, complex, loose, and periodic structures.
2. **Strictly Banned LLM Phrases & Clichés:**
   - *Banned words:* delve, testament, paramount, seamless, robust, pivotal, fostering, game-changer, beacon, cornerstone, revolutionizing, furthermore, moreover, state-of-the-art, cutting-edge, holistic, transformative.
   - *Banned phrases:* "In conclusion", "It is crucial / important to note", "Plays a pivotal role", "Serves as a cornerstone", "Underscores the necessity", "Masterfully weaves".
   - *Natural Academic Bridges:* Use direct connectors (*"However,"*, *"Because of this,"*, *"In practice,"*, *"By contrast,"*, *"Specifically,"*) or lead straight with the technical point.
3. **Break Repetitive Templates:** Never open consecutive summaries with the same syntactic formula (e.g., avoid repeating *"The [Author] (Year) investigated..."* or *"This study examines..."*). Alternate openers using prepositional phrases, dependent clauses, participial phrases, or active verbs.
4. **Specificity Over Generic Buzzwords:** Eliminate fluff (*"fostering holistic paradigms"*, *"seamless synergy"*). State concrete facts, exact numbers, specific municipal departments (Assessor vs. Treasurer), statutory sections, and local technical mechanisms.
5. **Authentic Undergraduate Tone:** Write with practical, active clarity from the perspective of student researchers tackling tangible municipal bottlenecks.
6. **Third-Person Naming Mandate:** Refer to the project strictly as **"the proposed system"** throughout. Never use "we," "our," "this project," or informal aliases.

---

## 6. Quamet Rubric Compliance Map (100-Point Target)

| Quamet Criterion | Points | Excellent (4 pts) Compliance Standard |
|---|:---:|---|
| **ACM Citation Accuracy** | 20 | Full ACM format with direct, verified document URL (never generic homepages). |
| **Coverage & Selection** | 20 | Peer-reviewed journal, IEEE/ACM/Scopus, official government/statutory issuance. Published 2021–2026. Routed to correct vault category. |
| **Annotation Quality: Summary & Critique** | 25 | Dense 1-sentence summary with varied syntactic opener. Multi-sentence critique grounded in authors' own stated limitations. |
| **Relevance & Application to Project** | 25 | 5-Layer Method satisfied. Architectural tier and functional module named. Proposed system resolution is technically specific. |
| **Writing Mechanics & Organization** | 10 | Third-person voice. Zero banned AI vocabulary/clichés. Varied sentence burstiness. Exact markdown vault structure. |
| **Total** | **100** | |

---

## 7. Quality Verification Checklist

Before saving any entry into the vault, verify:

- [ ] Has the **primary source been retrieved and read**?
- [ ] Is the source published between **2021 and 2026** (or an active statutory law/standard)?
- [ ] Does the URL point to the **direct document/issuance** (NOT a root homepage)?
- [ ] Has the URL been **verified as live** (no 404 or DNS failure)?
- [ ] Is the category wikilink set to the correct variant (`C2` by default)?
- [ ] Is the full ACM citation formatted in bold?
- [ ] Is the Summary exactly **one dense sentence** opening with a varied clause?
- [ ] Does the Relevance name the specific **architectural tier** and **functional module**?
- [ ] Does the Relevance cite the **authors' own stated limitation** from the text?
- [ ] Does the Relevance explicitly state how the proposed system resolves that limitation?
- [ ] Are there **at minimum two grounded sub-bullets** under `Source Reference(s)`?
- [ ] Are sentence burstiness and cadence varied (no robotic 20-word uniformity)?
- [ ] Are all banned AI buzzwords and clichés strictly eliminated?
- [ ] Is the project referred to strictly as **"the proposed system"** in third person?
- [ ] Has the entry been linked with a checkbox in the corresponding Category Hub note?
