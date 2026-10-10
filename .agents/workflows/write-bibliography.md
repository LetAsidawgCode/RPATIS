---
description: Step by step Of writing A BiblioGraphy
---

# RSS & RRL Annotated Bibliography Generator (Taxonomic & Architectural Framework)

**Description:** An Antigravity workflow to systematically source real literature, empirical studies, or software systems, and generate an ACM-formatted annotated bibliography entry designed for Chapter 1 and Chapter 2 Taxonomic / Architectural synthesis across any project domain.

## Step 1: Request Analysis & Sourcing

- Inspect the active project context defined in `.agents/rules/context.md` to ground domain understanding, target architecture, and research objectives.
- Clarify with the user (or confirm from context) the target source category:
  - **Related Study** (empirical papers with measured data/algorithms)
  - **Related System** (working software/hardware prototypes or existing platforms)
  - **Related Literature** (theoretical frameworks, systematic reviews, or government/industry standards)
  - Target chapter vault: **Chapter 2 (`01_anotatedbibliography C2/`) is the permanent active default**. Chapter 1 (`00_anotatedbibliography/`) is only targeted upon explicit user instruction.
- **Master Source Order Parity:** When generating entries for Chapter 2, follow the exact 1-to-45 sequential order established in `context/md/Chapter 1 Annotated Bibliography.md` (Related Literature 1–15, Related Studies 1–15, Related Systems 1–15) to maintain 1-to-1 consistency across both chapters.
- **Vault Inspection Check:** Before searching for any external sources, inspect the Obsidian vault directories in both `00_anotatedbibliography/` and `01_anotatedbibliography C2/`:
  - `Related-Study international/` (and local)
  - `Related-System international/` (and local)
  - `Related-Literature international/` (and local)
- Do not recommend, select, or generate an entry for any source that already exists within these vault directories to prevent duplicate entries.
- Use search capabilities (`read_url_content`, web search, DOI lookup) to find a **real, existing, and verifiable** source that matches the category.
- **CRITICAL CONSTRAINT:** Do not hallucinate sources. Verify that the study, system, or literature paper actually exists with a valid DOI, URL, or publication record, and inspect the primary text.
- **Mandatory Direct Document Link Protocol:** The agent MUST provide the **direct, specific document or publication link** (e.g., official gazette issuance page, specific memorandum circular repository path, PDF URL, or journal DOI landing page). **NEVER use generic root domains or homepages** (e.g., `https://arta.gov.ph/`, `https://dict.gov.ph/`, `https://privacy.gov.ph/`). Every URL/DOI must be tested and verified as active and accessible. Never output a broken, outdated, DNS-failed, or 404 URL.
- Prioritize recency: sources published between 2021–2026.

## Step 2: ACM Citation Formatting

- Format the retrieved source reference strictly using the Association for Computing Machinery (ACM) reference format in bold: `**[Author(s). Year. Title. Publication Venue. DOI/URL]**`.

## Step 3: Targeted 2-Part Annotation (Taxonomic / Architectural Framework)

Organize literature and existing systems by architectural layers, methodological paradigms, algorithmic frameworks, or deployment topologies rather than isolated paper-by-paper summaries. Each annotation provides raw material for taxonomic grouping, feature comparison matrices, and gap synthesis using strictly two main content sections: **Summary** and **Relevance** (with critique, limitations, and direct architectural relevance unified inside Relevance).

Draft a concise, rigorous 2-part annotation beneath the citation answering these core dimensions:

- **1. Summary (Summary of Scope & Method — 1 Sentence):**
  - **Core Questions Answered:** *What did they do, how did they do it, and what were their core findings?*
  - _For a Study:_ State the research problem addressed, the empirical methodology or algorithmic setup utilized, and the quantitative findings measured.
  - _For a System:_ State the software/hardware architecture developed (input sensors/devices, transport protocol, backend framework, data model, user interface), the operational mechanism, and primary functional results.
  - _For Literature / Policy:_ State the regulatory, statutory, or theoretical domain covered, the analytical/survey framework applied, and the core guidelines or taxonomies established.

- **2. Relevance (Direct Relevance to the Proposed System + Critique & Limitation):**
  - **Core Questions Answered:**
    - *Direct Relevance to the Project:* How does this directly justify the proposed system's research or inform its technical/architectural methodology?
    - *Banned Jargon Directives:* **NEVER repeatedly paste formulaic tier strings** like *"substantiates Tier 1 (Presentation Tier)"* or *"informs Tier 2 (Application and Business Logic) and Tier 3 (Relational Database)"* across entries. Instead, describe the architectural mechanisms directly using concrete, tangible engineering terms (e.g., browser-based assessment evaluation screens, treasury verification views, document routing engine, inter-office synchronization pipeline, centralized relational property database).
    - *Critique & Limitation:* What are the specific weaknesses, blind spots, architectural boundaries, or technological trade-offs of their approach (e.g., excessive latency, high computational overhead, proprietary lock-in, absence of localized operational context, failure to scale, or reliance on manual workflows)?
    - *The Bridge:* Conclude by stating precisely how **the proposed system** resolves these weaknesses and overcomes their operational limitations.
  - *Constraint:* Written strictly in the **third person**. Never use "you," "your," "I," or "my." Always refer to the project strictly as **"the proposed system"**.

- **3. Source Reference(s):**
  - Pinpoint exact section names (e.g., "Section 3.2 Methodology"), table numbers, page numbers, or short direct quotes verifying where data was retrieved.

## Step 4: Tone and Style Constraints

You must strictly adhere to the following academic writing rules when drafting the annotation:

1. **Zero-Hallucination Rule:** Do not add external speculation to the summary. If the primary text does not mention a specific metric or finding, do not include it.
2. **Banned AI Vocabulary:** NEVER use overused AI buzzwords (e.g., _delve, testament, paramount, seamless, robust, pivotal, fostering, game-changer, moreover, furthermore, beacon, cornerstone, revolutionizing, state-of-the-art, cutting-edge_).
3. **Ban Manufactured Rhetoric:**
   - Avoid forced rule-of-three rhythm lists (e.g., "improves workflow, enhances accuracy, and optimizes throughput").
   - Avoid X-not-Y parallel constructions (e.g., "the challenge is not X, but Y"). Rewrite as direct statements.
   - Do not use melodramatic summaries or punchlines at paragraph endings.
4. **Academic Hedging:** Use evidence-based qualifiers (_"suggests", "indicates", "demonstrates an accuracy of", "yields an error margin of"_) rather than absolute claims (_"completely solves", "guarantees", "eliminates"_).
5. **Direct Transitions:** Use functional research connectors (_"However," "Specifically," "In contrast," "Conversely"_) instead of conversational filler.
6. **Technical Grounding over Vague Praise:** Replace abstract descriptive hype with concrete engineering metrics (e.g., transmission latency in ms, RAM/CPU overhead, F1-score/precision/recall, or specific architectural designs).

## Step 5: Presentation & Single Entry Output

- Output entries matching the clean user-facing presentation format:

  ```text
  **[Number]. [Full Title]**

  **[Full ACM Citation with author, year, title, publication venue, location, and DOI/URL link]**

  Summary: [1-sentence summary of scope & method: what was done, how it was done, and core findings]

  Relevance: [Direct relevance informing the proposed system's operational architecture and functional modules without repetitive tier jargon, integrated with an explicit critique of specific weaknesses, blind spots, or boundaries of their approach and how the proposed system resolves them]
  ```

- **Formatting Rules:**
  - **Uniform Body Font:** Always format the title as plain bold text (`**[Number]. [Full Title]**`). **NEVER** use Markdown headings (`#`, `##`, `###`) so that font size remains identical to body text when copy-pasted into word processors.
  - **No Clutter in Chat:** Do NOT output redundant Markdown vault codeblocks in the chat unless explicitly requested. Provide the clean entry directly and save the vault markdown file behind the scenes upon approval.

- Also maintain the corresponding Obsidian vault structure for when the file is committed upon approval:

  ```markdown
  # [Paper / System / Literature Full Title]

  **Category:** [[<Category Hub Name>]]

  **[Full ACM Citation with author, year, title, publication venue, and DOI/URL link]**

  - **Summary:** [1-sentence summary of scope & method: what was done, how it was done, and core findings]

  - **Relevance:** [Direct relevance informing/justifying the proposed system's architectural tier or methodology based on .agents/rules/context.md, integrated with an explicit critique of specific weaknesses, blind spots, or boundaries of their approach and how the proposed system resolves them]

  - **Source Reference(s):**
    - _[Section / Page 1]:_ [Details or direct quote]
    - _[Section / Page 2]:_ [Details or direct quote]
  ```

- Ask the user for approval or feedback on the entry. **Stop execution.** Do not generate the next entry or execute any file transfers until the user explicitly approves the current one.

## Step 6: Obsidian Vault Integration & Routing

- Upon receiving explicit user approval, automatically transfer and save the approved entry as a Markdown (`.md`) file into the local Obsidian vault.
- Determine the target chapter and geographic origin to route the file to the correct directory:
  - **Chapter 2 Vault (`01_anotatedbibliography C2/`):**
    - Study international: `01_anotatedbibliography C2/Related-Study international/` (Category: `[[Related Study international C2]]`)
    - Study local: `01_anotatedbibliography C2/Related-Study local/` (Category: `[[Related Study local C2]]`)
    - System international: `01_anotatedbibliography C2/Related-System international/` (Category: `[[Related System international C2]]`)
    - System local: `01_anotatedbibliography C2/Related-System local/` (Category: `[[Related System local C2]]`)
    - Literature international: `01_anotatedbibliography C2/Related-Literature international/` (Category: `[[Related Literature international C2]]`)
    - Literature local: `01_anotatedbibliography C2/Related-Literature local/` (Category: `[[Related Literature local C2]]`)
  - **Chapter 1 Vault (`00_anotatedbibliography/`):**
    - Routes to corresponding `00_anotatedbibliography/` subdirectories with base hub links (e.g., `[[Related Literature local]]`).
- **Category Hub Linking:** Append the new note's wikilink `[[<Note Name>]]` with a checkbox (`- [ ] [[<Note Name>]]`) to the corresponding category hub note (e.g., `Related Study international C2.md`), which connects to its parent `[[Bibliography C2]]` or `[[Bibliography]]`.
- **Graph Hierarchy Maintained:**
  `[[Bibliography C2]]` ➔ `[[<Category Hub C2>]]` ➔ `[[<Individual Entry>]]`

---

## QUAMET Annotated Bibliography Rubric (AY 2026–2027)

Use this rubric to self-evaluate every annotated bibliography entry **before** presenting it to the user. Each entry must score at least **Proficient (3 pts)** in all criteria. Do not submit an entry that scores **Developing (2 pts)** or **Needs Improvement (1 pt)** in any criterion.

| Criterion | Points | Excellent (4 pts) | Proficient (3 pts) | Developing (2 pts) | Needs Improvement (1 pt) |
|---|---|---|---|---|---|
| **ACM Citation Accuracy** | 20 | Comprehensively establishes the context, clearly defines a compelling research problem, and strongly justifies the rationale with robust, cited evidence. | Establishes the context and defines the problem clearly. Provides an adequate rationale with some supporting evidence, though it may lack deep synthesis. | Context is somewhat vague, or the research problem is unclear. Rationale is present but lacks sufficient evidence, depth, or logical flow. | Fails to establish context. The research problem is missing, poorly defined, or lacks any clear, evidence-based rationale. |
| **Coverage & Selection (Lit, Studies, Systems)** | 20 | Objectives are highly specific, measurable, achievable, relevant, and time-bound (SMART). They perfectly align with and address the stated research problem. | Objectives are mostly SMART and align well with the problem, though 1–2 objectives may have minor clarity or measurability issues. | Objectives are too broad, lack measurable outcomes, or only partially align with the overarching research problem. | Objectives are excessively vague, unmeasurable, missing entirely, or have no logical connection to the research problem. |
| **Annotation Quality: Summary & Critique** | 25 | Boundaries, subjects, and specific limitations are explicitly and logically defined, providing a crystal-clear scope of what is and is not covered in the study. | Boundaries are clearly stated but may miss minor parameters (e.g., specific timeframe or geographic nuance). Limitations are adequately explained. | The scope is overly broad or vaguely defined. Limitations are only briefly mentioned and weakly justified. | Fails to clearly define the scope of the study. Limitations are entirely omitted, illogical, or demonstrate a misunderstanding of the research boundaries. |
| **Relevance & Application to Project** | 25 | Flawlessly anchors the study to highly relevant, established theories. Demonstrates deep synthesis and explicitly connects the theory to the study's variables. | Connects the study to relevant theories adequately. The connection is clear, but the synthesis lacks deep integration with the specific research problem. | Mentions established theories but fails to clearly connect them to the current study. Demonstrates only a superficial understanding of the underlying concepts. | Theories are irrelevant, missing, or fundamentally misunderstood. No clear theoretical basis is established for the research. |
| **Writing Mechanics & Organization** | 10 | Provides an exceptionally logical, visually clear paradigm (e.g., IPO model) of variables. Textual explanation perfectly matches and expands upon the diagram. | Visual and textual representations are clear and mostly logical. There may be minor gaps or discrepancies between the diagram and the written explanation. | Visual representation is confusing, cluttered, or incomplete. Textual explanation merely repeats the diagram without explaining the relationships between variables. | Conceptual framework is missing, or both visual and textual elements are completely illogical and fail to map out the study's variables. |

**Total Points:** 100

### Entry Type Definitions (per Rubric)

- **Related Literature:** Books, articles, and whitepapers that discuss the theoretical concepts, frameworks, algorithms, or domain knowledge necessary to understand the project.
- **Related Studies:** Peer-reviewed journals and conference papers detailing prior research, experiments, and methodologies. Answers: *What have other researchers discovered or proven about this topic?*
- **Related Systems:** Existing software, applications, platforms, or prototypes (both commercial and academic) that are similar to the proposed project. Answers: *What technologies already exist, and what are their limitations?*

### Example Entry (ACM Format — Related System)

```
[1] John Doe and Jane Smith. 2025. EduTech: A Smart LMS for Rural Areas.
    ACM Trans. Comput. Educ. 25, 4, Article 11 (October 2025), 15 pages.
    https://doi.org/10.1145/1234567.8901234

Annotation: This paper presents EduTech, an existing learning management system
designed for low-bandwidth environments. The authors detail the system's
offline-sync architecture and evaluate its usability among 500 students. While
the system excels in data compression, the authors admit it lacks real-time
collaborative features. This system is highly relevant to the proposed project;
a similar offline-first database structure will be adopted, but the proposed
system will improve upon EduTech by introducing a lightweight, text-based
collaborative module that operates on intermittent connections.
```
