# ISO 19152-4:2025: Geographic Information — Land Administration Domain Model (LADM) — Part 4: Valuation Information

**Category:** [[Related Literature international C2]]

**International Organization for Standardization. 2025. ISO 19152-4:2025: Geographic Information — Land Administration Domain Model (LADM) — Part 4: Valuation Information. International Organization for Standardization, Geneva, Switzerland. https://www.iso.org/standard/81266.html**

- **Summary:** Promulgated in 2025 as Part 4 of the Land Administration Domain Model, ISO 19152-4 establishes international UML conceptual packages and semantic classes that standardize administrative property valuations, valuation units, and transaction records to enable interoperability between land registries and municipal fiscal systems.

- **Relevance:** This global data standard provides the definitive structural foundation for the proposed system's centralized database schema and relational entity design. Grounded in ISO 19152-4’s valuation packages, the proposed system adapts these international standards into the centralized relational database schema, foreign-key mapping logic, and data validation routines of the Tax Payment Synchronization Module. Conceptual models require tangible software engines. While the standard establishes rigorous UML class abstractions for parcel valuations and tax assessments, it deliberately omits physical relational DDL schemas, user interface layouts, or inter-office document routing logic adapted to rural municipal halls. In municipalities like Canaman, Magarao, San Fernando, and Pasacao, staff struggle with manual paper cards dating back to 1949 and disjointed payment ledgers rather than abstract modeling deficits. The proposed system directly overcomes this architectural barrier by translating ISO 19152-4’s valuation classes into an operational web platform that joins property appraisal records with treasury collection rolls through automated foreign-key mapping and real-time document tracking.

- **Source Reference(s):**
  - _Clause 5: Conformance and Abstract Test Suite (pp. 6–10):_ Outlines semantic interoperability criteria and mandatory abstract test suites for linking land valuation records with local taxation systems.
  - _Clause 6: Valuation Information Package (pp. 12–28):_ Specifies standardized UML conceptual classes—including `ValuationUnit`, `PropertyAssessment`, and `ValuationSource`—to structure appraisal records and fiscal transaction linkages.
