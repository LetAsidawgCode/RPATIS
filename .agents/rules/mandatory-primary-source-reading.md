---
trigger: always_on
---

# Mandatory Primary Source Reading Rule

**AI Directive:** When drafting, updating, or rewriting any annotated bibliography entry for Chapter 1 or Chapter 2 (e.g., in `00_anotatedbibliography/` or `01_anotatedbibliography C2/`), the AI must **NEVER** merely rehash or summarize existing vault notes, abstracts, or metadata snippets.

## Mandatory Retrieval & Reading Protocol

Before presenting any draft entry for user review:

1. **Retrieve the Actual Primary Source:**
   - Use `read_url_content`, web search, DOI resolvers, open-access university repositories, or IEEE/ACM/ScienceDirect/Google Scholar records to access the actual full text, conference proceedings, or published manuscript.
2. **Extract Concrete Technical Details from the Primary Text:**
   - *Architecture & Implementation:* Exact hardware models (if embedded/IoT), software stacks, languages, libraries, database engines, network protocols, algorithmic models, or physical/simulation testbeds utilized.
   - *Empirical Findings & Quantified Metrics:* Concrete numbers, measurement accuracy, latency (ms), precision, recall, F1-scores, throughput, error margins (e.g., ±1.5%), computational/resource overhead, or standardized survey scores.
   - *Actual Stated Boundaries & Future Work:* Thoroughly review the paper's actual Discussion, Conclusion, and Limitations sections to identify what the authors explicitly acknowledged their system or methodology lacked.
3. **Grounding in 3-Question Framework:**
   - **Summary of Scope & Method:** Exactly what the authors did, how they built or tested it, and what empirical results they achieved (strictly 1 concise sentence).
   - **Relevance (Tier Justification + Critique & Limitation):** How the cited work directly justifies the proposed system's architectural tier, algorithmic pipeline, or methodology (referencing the active project profile in `.agents/rules/context.md`), contrasted against the cited work's specific blind spots, bottlenecks, or trade-offs, and explicitly stating how the proposed system resolves them.
   - **Source Reference(s):** Direct section headings, table numbers, page numbers, or short direct quotes from the primary publication.
