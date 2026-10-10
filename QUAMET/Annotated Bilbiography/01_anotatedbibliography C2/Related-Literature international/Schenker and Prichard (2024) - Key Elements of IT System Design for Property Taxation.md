# Key Elements of IT System Design for Property Taxation

**Category:** [[Related Literature international C2]]

**Xaver Schenker and Wilson Prichard. 2024. Key Elements of IT System Design for Property Taxation. LoGRI Guidance Note No. 04. Local Government Revenue Initiative, University of Toronto, Toronto, ON, Canada. https://logri.org/resources/key-elements-of-it-system-design-for-property-taxation/**

- **Summary:** Published by the Local Government Revenue Initiative, this international technical guidance note synthesizes architectural criteria for subnational property tax IT systems, arguing that monolithic software platforms fail in developing municipalities unless designed with modular subsystems, open relational data pipelines, and synchronized inter-office workflows.

- **Relevance:** This technical guidance directly provides the architectural blueprint and operational rationale for the proposed system's modular web architecture. Applying Schenker and Prichard’s modularity principles, the proposed system partitions its browser-based evaluation interfaces, automated routing engine, and centralized relational database to establish a clean boundary between the Assessment Request Routing Module and the Tax Payment Synchronization Module. Monolithic commercial software frequently cripples rural municipalities. Proprietary licensing costs and rigid vendor frameworks prevent resource-constrained LGUs from integrating their valuation and treasury operations. Although Schenker and Prichard outline core functional modules spanning property discovery to collection, their work remains an advisory policy blueprint; they present no empirical time-motion evaluations or localized relational data schemas tested within Philippine municipal settings. The proposed system resolves this gap by conducting a rigorous needs assessment across Pasacao, Canaman, Magarao, and San Fernando and deploying a lightweight, open-source web platform that automates document routing and links valuation updates directly with treasury tax ledgers.

- **Source Reference(s):**
  - _Section 2: Core Functional Requirements (pp. 4–8):_ Identifies the mandatory sequential pipeline linking property discovery, physical parcel appraisal, valuation roll publication, billing, and tax collection.
  - _Section 4: Technical Design Principles and Modular Architecture (pp. 9–14):_ Recommends decoupled application layers, open relational databases, and standardized API interchanges to prevent departmental data silos and high vendor licensing lock-in.
