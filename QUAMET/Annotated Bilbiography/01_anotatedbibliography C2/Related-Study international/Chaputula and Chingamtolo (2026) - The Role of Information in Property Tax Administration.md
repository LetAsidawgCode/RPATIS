# The Role of Information in Property Tax Administration

**Category:** [[Related Study international C2]]

**Aubrey Harvey Chaputula and Caroline Chingamtolo. 2026. The Role of Information in Property Tax Administration. Journal of Real Estate Practice and Education 28, 1 (April 2026). https://doi.org/10.1080/15214842.2026.2644666**

- **Summary:** Conducting a mixed-methods empirical investigation at Mzuzu City Council in Malawi, Chaputula and Chingamtolo (2026) proved that categorizing municipal records across owner identities, parcel boundaries, and structural building metrics accelerates property registration, but cautioned that uncoordinated administrative handoffs between assessment and revenue offices severely constrain billing throughput.

- **Relevance:** This empirical investigation directly informs the data modeling and input schema of the proposed system's Assessment Request Routing and Tax Payment Synchronization Modules. Translating Chaputula and Chingamtolo’s tripartite data framework, the proposed system guides the browser-based assessment intake forms and automated routing workflows that structure how citizen assessment filings transition into relational database entities. Isolated record systems create communication barriers. In municipal offices where valuation data remains quarantined on standalone computers or paper cards, billing staff cannot verify property improvements without time-consuming manual queries. While Chaputula and Chingamtolo demonstrate the critical value of structured tax information, their research focuses on descriptive management evaluation; they engineer no automated software workflows, tracking dashboards, or relational synchronization algorithms. The proposed system directly resolves this operational limitation by deploying an integrated web platform that captures property improvement data on the Assessor evaluation screen and routes it immediately into the Treasurer collection view, eliminating inter-departmental communication gaps.

- **Source Reference(s):**
  - _Introduction & Information Categorization (pp. 2–5):_ Classifies municipal tax records into three mandatory data categories: taxpayer identification, cadastral parcel attributes, and structural building improvements.
  - _Results & Discussion on Administrative Challenges (pp. 8–14):_ Reports empirical findings demonstrating that lack of integrated software and persistent inter-departmental communication divides severely impair revenue billing efficiency despite improved parcel registration.
