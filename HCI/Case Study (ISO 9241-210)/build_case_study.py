"""
Builds the Google Sheets ISO 9241-210 case study from the GRP23 template.

- Template:  HCI/GRP23_Case Study(ISO 9241-210).docx  (cover, TOC, styles, checklist table are reused)
- Output:    HCI/Case Study (ISO 9241-210)/Case_Study_GoogleSheets_ISO_9241-210.docx
- Screenshots: images/gsheets/S1_grid.png ... S7_version_history.png
  Missing screenshots are replaced by a grey labelled slot so the layout is still complete.
Re-run this script any time screenshots are added or text is edited.
"""
import copy
import os
import re

import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt
from docx.text.paragraph import Paragraph
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(os.path.dirname(HERE), "GRP23_Case Study(ISO 9241-210).docx")
OUTPUT = os.path.join(HERE, "Case_Study_GoogleSheets_ISO_9241-210.docx")
IMG = os.path.join(HERE, "images")
SHOTS = os.path.join(IMG, "gsheets")
SLOTS = os.path.join(SHOTS, "_slots")

# --------------------------------------------------------------------------------------
# CONTENT
# --------------------------------------------------------------------------------------
SCREENSHOTS = [
    ("S1_executive_dashboard.png",
     "Figure 1. Municipal Real Property Tax (eRPT) Executive Dashboard: KPI summary cards, revenue performance, and property classification matrix (Live Google Sheets, 2026).",
     "The Executive Dashboard establishes a centralized operational overview for municipal administrators. Prominent KPI cards summarize registered parcel counts, aggregate market valuation (₱5,228,500.00), total taxable assessed valuation (₱2,061,700.00), and annual tax due. Beneath the metric cards, dynamic tables track collection performance across property classifications (Residential, Agricultural, Commercial) and across eight constituent barangays. Although this dashboard aggregates real-time data, maintaining it in a cloud spreadsheet requires manual formula maintenance across tabs and lacks automated data pipeline triggers."),
    ("S2_dashboard_charts.png",
     "Figure 2. Executive Dashboard revenue analytics: Municipal Target progress (Doughnut Chart) and Valuation Comparison by Classification (Column Chart) (Live Google Sheets, 2026).",
     "Visual analytics enhance executive decision-making by illustrating revenue realization against unpaid municipal delinquency targets. The Doughnut Chart depicts collections realized (Paid accounts) versus outstanding delinquency, providing immediate feedback on collection efficiency. Alongside it, the Clustered Column Chart contrasts total market valuation with assessed taxable valuation across property classes. In an unintegrated spreadsheet environment, however, chart rendering depends on client-side browser performance, and charts cannot trigger automated delinquency notices to property owners."),
    ("S3_assesment_roll.png",
     "Figure 3. Municipal Assessor\u2019s Office - Real Property Assessment Roll showing 15-column valuation register and payment status tracking (Live Google Sheets, 2026).",
     "The Assessment Roll tab functions as the primary cadastre ledger for the Municipal Assessor\u2019s Office. It records Tax Declaration Numbers (TD No.), Property Identification Numbers (PIN), masked owner names, barangay locations, parcel areas, unit values, market values, statutory assessment levels, and computed taxes (Basic RPT 1% and SEF 1%). Color-coded status chips highlight settled accounts versus unpaid accounts. Because this register contains sensitive ownership information, managing it in Google Sheets exposes citizen records to accidental link-sharing risks under RA 10173."),
    ("S4_formula_bar.png",
     "Figure 4. Formula bar exposing automated valuation logic and nested IF classification tiers (Live Google Sheets, 2026).",
     "Clicking on computed cells reveals the underlying computational formulas. The Assessed Value column computes =Market_Value * Assessment_Level, while the Assessment Level column evaluates property classes via nested =IF(E4=\"Residential\", 0.20, IF(E4=\"Agricultural\", 0.40, IF(E4=\"Commercial\", 0.50, 0.20))) logic. Exposing these statutory formulas directly in the spreadsheet grid creates operational vulnerability: an unintentional keystroke or drag-fill by an administrative clerk can overwrite the formula without raising an alert or audit warning."),
    ("S5_treasurer_collections.png",
     "Figure 5. Municipal Treasurer\u2019s Office - Real Property Tax Collections ledger with cross-office VLOOKUP and reconciliation badges (Live Google Sheets, 2026).",
     "The Treasurer Collections tab acts as the cash collection register. Official Receipt numbers, payment dates, and cash receipts are cross-referenced against the Assessor\u2019s Assessment Roll using =IFERROR(VLOOKUP(...), \"RECORD NOT FOUND\"). A calculated variance column automatically audits whether payments match the assessed tax due. Conditional reconciliation badges classify transactions into 'Fully Settled', 'Partial / Underpaid' (such as the ₱64.00 shortfall on TD-26-0004), and 'Record Missing / Error' (such as the typo on TD-26-0080). This demonstrates that while spreadsheets can compute variances, resolving them still requires manual inter-office cross-checking."),
    ("S6_treasurer_paid_unpaid_charts.png",
     "Figure 6. Treasurer Analytics: Paid vs. Unpaid Collections Yield (Doughnut Chart) and Real Property Accounts Distribution (Column Chart) (Live Google Sheets, 2026).",
     "Dedicated visual dashboards on the Treasurer tab monitor municipal cash inflow versus uncollected tax backlog. The 'Treasurer Tax Yield' Doughnut Chart displays the proportion of realized collections against outstanding tax liabilities. Beneath it, the 'Real Property Accounts' Column Chart compares the number of compliant, paid parcels (5 accounts) against delinquent, unpaid parcels (3 accounts). These visualizations allow treasury supervisors to gauge compliance at a glance, though extracting historical compliance trends remains constrained by flat-file data limits."),
    ("S7_share_dialog.png",
     "Figure 7. Google Workspace Share modal showing blanket file permissions and General link access (Live Google Sheets, 2026).",
     "Access governance in Google Sheets is administered on an all-or-nothing file basis (Viewer, Commenter, or Editor). Field-level permissions—such as preventing treasury cashiers from editing valuation baselines or preventing assessors from altering payment receipts—cannot be enforced natively. In addition, configuring General access to 'Anyone with the link' allows public, unauthenticated access, violating the data privacy mandates of Republic Act No. 10173."),
    ("S8_version_history.png",
     "Figure 8. Version history panel listing timestamped revisions without transactional audit metadata (Live Google Sheets, 2026).",
     "The Version History sidebar records chronological revisions and user identities, enabling document rollback. However, it lacks transactional granularity: changes to an individual assessment or tax receipt are aggregated into broad snapshot sessions. The system cannot produce legally binding, immutable audit logs with cryptographic integrity, unlike the dedicated transaction logs required for government fiscal systems."),
]

SECTION_A = [
    ("p", "Google Sheets is a free, browser-based spreadsheet application that is part of Google Workspace. "
          "It runs in any modern desktop browser and also has Android and iOS apps. Files are stored in "
          "Google Drive, not on the office computer. One spreadsheet can hold up to 20 million cells. "
          "Several people can edit the same file at once, and each person\u2019s cursor appears in a "
          "different color. Google first released the product in 2006 after acquiring 2Web Technologies "
          "and its XL2Web spreadsheet."),
    ("p", "The course instructor asked the proponents to evaluate a system that is close to them and has an "
          "interface they can open and use directly. Google Sheets fits that instruction. Its two core "
          "features are recording structured data in rows and computing values with formulas, and those "
          "are also two of the core functions of the proposed system. Sheets is also the tool many "
          "municipal clerks, barangay staff, and students open first when they need to keep a list and "
          "total it."),
    ("p", "The connection to real property tax (RPT) administration is direct. Assessor and treasurer staff "
          "often keep assessment rolls, collection logs, and delinquency lists in spreadsheets, sometimes "
          "alongside dedicated tax software. Even Pasacao, which runs a localized eRPT, still moves "
          "collection data between offices as batch spreadsheet files. To test Sheets in this setting, the "
          "proponents built a mock Pasacao assessment roll with masked owner names, in line with RA 10173. "
          "The Assessment_Roll tab records eight tax declarations and computes the Market Value (Area \u00d7 "
          "Unit Value) and the Assessment Level by classification. The levels used are 20% residential, "
          "40% agricultural, and 50% commercial, which are the maximum land rates under Section 218 of "
          "RA 7160. The tab then computes the Assessed Value, the 1% Basic RPT, the 1% Special Education "
          "Fund levy, and the Total Tax Due. A second tab, Treasurer_Collections, imitates the "
          "cashier\u2019s ledger and pulls the tax due from the assessor\u2019s tab through VLOOKUP."),
    ("p", "The exercise shows where Sheets helps and where it stops. Once the formula is right, it computes "
          "the tax correctly. However, it has no concept of a Transfer of Assessment. It cannot route a "
          "document to the Treasurer, and it cannot tell a clerk whether the Provincial Assessor in Pili "
          "has signed off. These are the gaps the proposed system is built to close."),
    ("sub", "1. Core Features Relevant to RPT Recording and Computation"),
    ("label", "Grid-Based Record Keeping: ",
     "Each row holds one tax declaration. Columns hold the TD No., PIN, owner, barangay, classification, "
     "area, and unit value. Freeze panes keep the header row visible while the clerk scrolls."),
    ("label", "Formula Computation Engine: ",
     "Built-in functions such as IF, SUM, VLOOKUP, XLOOKUP (added in August 2022), and ARRAYFORMULA "
     "recompute every dependent cell as soon as an input changes."),
    ("label", "Data Validation: ",
     "Dropdown rules limit a column to listed values, for example Residential, Agricultural, or Commercial. "
     "Entries that break the rule are flagged or rejected."),
    ("label", "Sharing, Permissions, and Protected Ranges: ",
     "Owners grant Viewer, Commenter, or Editor access per person. Protected ranges can lock specific "
     "cells or tabs against editing."),
    ("label", "Version History: ",
     "Edits save automatically. Users can view earlier versions, restore any of them, and name up to 40 "
     "versions per file."),
    ("label", "Offline Access: ",
     "With Chrome or Microsoft Edge and the Google Docs Offline extension, a clerk can keep editing during "
     "an internet outage. Changes sync once the connection returns."),
    ("sub", "2. Interface Views of the System"),
    ("p", "Figures 1 to 8 show the live Google Sheets interface across the Executive Dashboard, the Municipal Assessment Roll, and the Treasurer Collections ledger. A short note after each figure states the HCI and human-centred design concern that the view raises. All owner names, PINs, and amounts are fictitious."),
    ("shots",),
]

SECTION_B = [
    ("p", "ISO 9241-210 Clause 6.2 requires a clear understanding of who uses a system, for which tasks, "
          "with what tools, and in what environment. For Google Sheets used as an RPT ledger, the "
          "proponents identified the following groups and conditions from the Pasacao and Canaman field "
          "interviews and from hands-on use of the mock roll:"),
    ("sub", "1. Primary User Groups"),
    ("label", "Municipal Assessor Personnel (Assessment Clerks, Appraisers, Tax Mappers): ",
     "These staff encode tax declaration data, apply unit values from the Schedule of Market Values, and "
     "maintain the assessment roll. They either write the formulas that compute assessed value or inherit "
     "them from whoever built the file."),
    ("label", "Municipal Treasurer Personnel (Revenue Collection Clerks, Cashiers): ",
     "The cashiers keep a separate collection ledger. They look up the tax due for each TD No., record "
     "Official Receipt numbers, and reconcile payments against the assessor\u2019s figures."),
    ("label", "Office Heads (Municipal Assessor, Municipal Treasurer): ",
     "The heads review totals and delinquency lists, usually with view-only access, and decide who gets "
     "edit rights to the file."),
    ("sub", "2. Secondary User Groups"),
    ("label", "Property Owners and Taxpayers: ",
     "Taxpayers never touch the sheet, but their bills come from it. A broken formula turns into an "
     "overcharge or undercharge at the counter."),
    ("label", "Provincial Assessor\u2019s Office (Pili): ",
     "This office receives printed or emailed extracts for review and approval. It cannot see the "
     "current state of the municipal file."),
    ("label", "Local MIS or IT Staff: ",
     "Where an IT officer exists, that person manages Google accounts and sharing. Where none exists, "
     "files can end up shared from clerks\u2019 personal Gmail accounts."),
    ("sub", "3. Context of Use, Hardware, and Environmental Conditions"),
    ("p", "Staff work inside municipal halls from 8:00 AM to 5:00 PM, Monday to Friday. The heaviest load "
          "comes in January, when early payers claim the prompt-payment discount, and again near the "
          "quarterly deadlines."),
    ("p", "The setting places these constraints on spreadsheet use:"),
    ("label", "Hardware and Terminals: ",
     "Staff use shared Windows desktops or laptops with a browser. Sheets needs no installation, only a "
     "supported browser and a Google account. Some offices still print forms on dot-matrix printers."),
    ("label", "Network Infrastructure: ",
     "Sheets is built for the cloud. Rural connections in Camarines Sur drop out often, and offline mode "
     "works only if someone switched it on beforehand in that browser."),
    ("label", "Physical Office Environment: ",
     "Counters are noisy, queues are long, and rooms get hot. A brownout stops work on desktops without "
     "a UPS. After a dropped connection, the clerk cannot be sure the last entries were saved."),
    ("label", "Legacy Paper Ledgers: ",
     "Records going back to 1949 still have to be read from paper and typed in row by row. Sheets offers "
     "no structured way to bring them in."),
    ("label", "Data Privacy Conditions: ",
     "Owner names, addresses, and property values are personal information under RA 10173. On a free "
     "consumer account, the LGU has little administrative control over where a file goes once it is "
     "shared or downloaded."),
]

SECTION_C = [
    ("p", "Hands-on use of the mock roll showed clear strengths, along with usability problems that become "
          "serious once the data is public revenue:"),
    ("sub", "1. Usability Strengths"),
    ("label", "Low Learning Barrier: ",
     "The grid, A1 cell references, and formula syntax follow Excel conventions. Function autocomplete "
     "shows each function\u2019s arguments as the clerk types."),
    ("label", "Instant Computation: ",
     "When the clerk changes the area or unit value, the market value, assessed value, and total tax due "
     "update on the spot. Nobody has to redo the arithmetic by hand (Figures 2 and 3)."),
    ("label", "Real-Time Collaboration: ",
     "Two clerks can encode different rows at the same time. Comments and @mentions let them ask "
     "questions inside the file instead of leaving their desks."),
    ("label", "Error Recovery: ",
     "Undo and version history can roll back a bad edit, and data validation blocks invalid "
     "classifications before they reach the formulas (Figures 4 and 7)."),
    ("label", "Zero Installation and Low Cost: ",
     "Sheets runs in any modern browser and is free with a Google account. For an LGU with no IT budget, "
     "that matters."),
    ("sub", "2. Usability Issues and Operational Pain Points"),
    ("label", "Fragile, Hidden Formulas: ",
     "The tax logic is written in cell references. Deleting a column or pasting over a formula breaks the "
     "computation chain without any warning, and the wrong tax due still looks like a normal number."),
    ("label", "Manual Inter-Office Matching: ",
     "The Assessor and the Treasurer keep separate tabs or files. Matching between them depends on typing "
     "the TD No. exactly (Figure 5). VLOOKUP or IMPORTRANGE can link the files, but someone has to build "
     "and maintain that link, and one typo breaks it."),
    ("label", "No Workflow or Status Tracking: ",
     "A \u201cStatus\u201d column is plain text. Sheets cannot route a Transfer of Assessment, enforce "
     "the order of approvals, or show where a document is between the municipality and Pili. In Pasacao, "
     "transfers still take more than seven days. In Canaman, building assessments wait 7 to 14 days for "
     "provincial approval."),
    ("label", "Cryptic Error Feedback: ",
     "Codes such as #VALUE!, #REF!, and #N/A mean little to a clerk unless they hover over the cell or "
     "already know what the code means."),
    ("label", "Weak Governance for Public Records: ",
     "Anyone with edit access can change a rate, and \u201cAnyone with the link\u201d sharing can expose "
     "taxpayer data. Appraisal entry and cashiering stay separate only if protected ranges are set up "
     "carefully, and in small offices that rarely happens."),
    ("label", "Internet Dependence: ",
     "Offline editing needs prior setup on Chrome or Edge. Without it, a service interruption stops the "
     "counter."),
]

SECTION_D_INTRO = [
    ("p", "ISO 9241-210:2010 sets requirements and recommendations for human-centred design across the "
          "life cycle of an interactive system. Annex B, Table B.1, gives the checklist for assessing "
          "conformance. The proponents evaluated Google Sheets against that checklist using three sources: "
          "Google\u2019s public documentation (Help Center articles, the Workspace Updates blog, and the "
          "Google Accessibility Conformance Reports), a hands-on walkthrough of the mock assessment roll "
          "(Figures 1 to 7), and the Pasacao and Canaman findings from the proponents\u2019 needs "
          "assessment."),
    ("sub", "Synthesis of Human-Centered Design Conformance"),
]

SECTION_D_BODY = [
    ("p", "The results fall along one dividing line. As a general spreadsheet product, Google Sheets shows "
          "strong human-centred design: {met} of the {total} checklist items were met. As an RPT ledger, "
          "it falls short on the remaining {notmet}, mostly because Google never designed it for municipal "
          "tax work. In that setting, the LGU staff become the designers, and they have no HCD process at "
          "all."),
    ("p", "Under Clause 4 (Principles), Sheets meets Principle 4.5 (iteration) through a steady stream of "
          "releases, from XLOOKUP in 2022 to the Tables feature in 2024. It meets Principle 4.6 by keeping "
          "Excel\u2019s mental model, so trained clerks need almost no retraining. It fails Principle 4.2 "
          "for this context, because assessors, cashiers, and taxpayers are not identified user groups. "
          "It also fails the function-allocation items of 4.6. Error-prone work, such as matching records "
          "between offices and checking formulas, stays with the clerk instead of moving to the system."),
    ("p", "Clause 5 (Planning) is the hardest to verify. Google does not publish its internal HCD plans, "
          "milestones, or trade-off rationales, so those items are marked \u201cNo\u201d under the "
          "evidence rule. Some planning is visible, though. Staged Rapid and Scheduled Release tracks, "
          "early-access programs, and Material Design guidelines all point to a planned feedback cycle. "
          "What is missing for the LGU case is any assessment of risk. A wrong cell reference in a public "
          "revenue file quietly changes what a taxpayer owes."),
    ("p", "Clauses 6.2 and 6.3 (Context and Requirements) split the same way. Google documents the "
          "technical context in detail: supported browsers, offline setup, and the 20-million-cell limit. "
          "The municipal context is not covered at all. Brownouts, shared terminals, January queues, "
          "1949 paper ledgers, and the Assessor-Treasurer-Province approval chain are outside the "
          "product\u2019s scope. There are no measurable usability criteria such as task time or error "
          "rate, so the requirements cannot be tested in the sense that Clause 6.3.5 expects."),
    ("p", "Under Clauses 6.4 and 6.5 (Design and Evaluation), Sheets does well on most ISO 9241-110 dialogue "
          "principles: suitability for the task, conformity with expectations, controllability, error "
          "tolerance, and individualization. It is weaker on self-descriptiveness, because formulas and "
          "error codes need prior knowledge to read (Figures 2, 3, and 5). It also has no concept of task "
          "sequence. A record can be marked \u201cPaid\u201d before it is assessed. On evaluation, "
          "Google\u2019s Accessibility Conformance Reports apply WCAG 2.1 methods with experienced "
          "testers. No evaluation covers high-risk uses such as computing local taxes, and nobody tested "
          "Sheets with municipal clerks doing RPT tasks."),
]

SECTION_E = [
    ("p", "The checklist findings point to five design recommendations for spreadsheet-based RPT record "
          "keeping. Each one carries into a specific part of the proposed system:"),
    ("label", "1. Replace Hand-Built Formulas with Locked, Rule-Based Computation: ",
     "In Sheets, assessment levels and tax rates live inside editable formulas (Figure 4). Recommendation: "
     "keep the rates in a single reference table and lock every computed column. Lesson Applied to the "
     "Proposed System: the proposed system computes assessed value and tax due in its application tier, "
     "using one rate table that only authorized administrators can change. A rate revision then takes "
     "effect everywhere at once."),
    ("label", "2. Link Assessor and Treasurer Records by Key, Not by Typed Text: ",
     "The cashier\u2019s VLOOKUP fails on a single wrong digit (Figure 5). Recommendation: select records "
     "from a controlled list and share one record between the two offices instead of keeping two copies. "
     "Lesson Applied to the Proposed System: the Tax Payment Synchronization Module lets the "
     "Treasurer\u2019s validation view read the same database record the Assessor maintains. Nobody "
     "retypes data, and nobody cross-checks by hand."),
    ("label", "3. Add Workflow States and Document Tracking: ",
     "In Sheets, status is a free-text column with no rules and no timestamps. Recommendation: define "
     "each stage of a request, the allowed moves between stages, and the time each move happens. Lesson "
     "Applied to the Proposed System: the Assessment Request Routing and Document Tracking Module, "
     "together with the Administrative Workflow Panel, shows where each request is between the Assessor, "
     "the Treasurer, and the Provincial Capitol in Pili. It logs the time at every step, so the 7-to-14-day "
     "waits become measurable."),
    ("label", "4. Make Errors Self-Explanatory and Labels Task-Based: ",
     "Codes such as #VALUE! and formulas written in cell addresses work against self-descriptiveness. "
     "Recommendation: write validation messages in tax terms and label every field by its meaning. "
     "Lesson Applied to the Proposed System: the proposed system uses labelled fields (Market Value, "
     "Assessment Level, Assessed Value) with inline messages such as \u201cTD No. not found in the "
     "assessment roll. Check the number or contact the Assessor\u2019s Office.\u201d"),
    ("label", "5. Enforce Role-Based Access and Test with Real Clerks: ",
     "Sheets controls access per file, and link sharing is easy to switch on (Figure 7). Recommendation: "
     "set permissions per function, keep an audit log, and run usability tests with the people who will "
     "use the system. Lesson Applied to the Proposed System: role-based access control separates Assessor "
     "entry from Treasurer validation. Live records are encrypted under RA 10173, and development uses "
     "only mock data. Two-week Agile sprints end with ISO/IEC 25010 evaluations by staff from Pasacao, "
     "Canaman, Magarao, and San Fernando."),
]

CHECKLIST_INTRO = (
    "This checklist evaluates Google Sheets, as used for RPT assessment recording and computation, "
    "against ISO 9241-210:2010 Annex B Table B.1. Items are judged on two grounds: what Google publicly "
    "documents about the product, and how well the product serves the municipal Assessor and Treasurer "
    "context described in Section B. Items with no verifiable public evidence are marked \u2018No,\u2019 "
    "and the comments column explains each judgment.")

# (applicable, reason_na, met 'Y'/'N', comment) -- one tuple per Table B.1 row, in template order
CHECKLIST = [
    ("Y", "", "Y", "Google applies Material Design guidelines and UX research across Workspace. The approach is user-centred for general spreadsheet work, not for LGU tax administration."),
    ("Y", "", "Y", "Sheets serves individual, education, and business users, including people who only view or comment on a file."),
    ("Y", "", "N", "Municipal assessors, cashiers, and taxpayers are not identified groups. RPT offices must adapt a general tool themselves."),
    ("Y", "", "Y", "User input is gathered through Help > Help Sheets improve and through early-access programs before general release."),
    ("Y", "", "N", "Feedback comes from Google\u2019s broad user base. Rural clerks with limited spreadsheet literacy are not specifically represented."),
    ("Y", "", "Y", "Features roll out in stages through Rapid and Scheduled Release tracks, so user response is observed before full release."),
    ("Y", "", "Y", "The Workspace Updates blog records frequent Sheets releases, e.g., XLOOKUP (Aug. 2022) and Tables (May 2024)."),
    ("Y", "", "Y", "Grid layout, A1 references, and formula syntax mirror Excel, so trained clerks carry over their skills (Figure 1)."),
    ("Y", "", "N", "Formula writing, record checking, and cross-office matching stay with the clerk. Error-prone RPT tasks are not shifted to the system."),
    ("Y", "", "N", "No evidence that LGU staff helped decide which RPT tasks Sheets automates. Clerks build their own formulas."),
    ("Y", "", "Y", "Encoding, computing, sorting, and filtering form a coherent task set that matches daily ledger work."),
    ("Y", "", "Y", "Google staffs Workspace with UX researchers, interaction designers, accessibility specialists, and engineers."),
    ("Y", "", "Y", "Public Material Design 3 guidance and staged releases show HCD built into Google\u2019s product life cycle."),
    ("Y", "", "Y", "Usability is central to Sheets\u2019 purpose as a self-service tool that people use without formal training."),
    ("Y", "", "N", "The risk of formula errors in public revenue records is not addressed. A wrong reference silently changes a taxpayer\u2019s assessed value."),
    ("Y", "", "Y", "As a cloud web app, Sheets ships updates to all users without local installation."),
    ("Y", "", "N", "The specific HCD methods and resources used for Sheets are not published, so this item cannot be verified."),
    ("Y", "", "N", "Internal procedures linking HCD activities to engineering work are not publicly documented."),
    ("Y", "", "Y", "Accessibility and Workspace UX roles are publicly identified functions within Google."),
    ("Y", "", "N", "Changes are announced, but the human-factors reasons behind trade-offs are rarely documented."),
    ("Y", "", "N", "HCD milestones in Google\u2019s development schedule are not public."),
    ("Y", "", "Y", "Release tracks set a fixed window for collecting feedback before a feature reaches all users."),
    ("Y", "", "N", "Not verifiable from public sources."),
    ("Y", "", "N", "Not verifiable from public sources."),
    ("Y", "", "Y", "Workspace Updates posts often cite user feedback as the reason for a change, showing that plans are revised."),
    ("Y", "", "N", "Resource allocation for HCD is internal to Google and not published."),
    ("Y", "", "Y", "Staged rollouts and early-access programs leave time for user feedback before general availability."),
    ("Y", "", "N", "Time set aside for design-team communication on trade-offs is not documented."),
    ("Y", "", "N", "Sheets began as an acquired product (XL2Web, 2006). Early-stage HCD activity is undocumented."),
    ("Y", "", "Y", "Two decades of interface updates, including the Material Design 3 refresh, show review throughout the product\u2019s life."),
    ("Y", "", "Y", "Desktop, mobile, and offline contexts are specified in Google\u2019s documentation."),
    ("Y", "", "Y", "Supported tasks and limits (e.g., 20 million cells per file) are specified in the Help Center."),
    ("Y", "", "Y", "Design solutions such as the formula bar, Smart Fill, and dropdown chips are produced and refined across releases."),
    ("Y", "", "Y", "Accessibility Conformance Reports evaluate Sheets against WCAG 2.1 and Section 508."),
    ("Y", "", "Y", "Owner, Editor, Commenter, and Viewer are defined roles with distinct goals in the sharing model (Figure 7)."),
    ("Y", "", "N", "Characteristics of LGU clerks, such as spreadsheet literacy and typing load, are not considered by a general product."),
    ("Y", "", "Y", "Personal, education, and business users are separated through Workspace editions and admin controls."),
    ("Y", "", "Y", "Screen reader, braille, and magnifier support is documented, and ACRs report WCAG 2.1 conformance."),
    ("Y", "", "Y", "The goal of organizing, computing, and sharing tabular data is clearly stated."),
    ("Y", "", "N", "RPT tasks (appraisal, transfer, endorsement) follow legal sequences that Sheets neither describes nor supports."),
    ("Y", "", "N", "No guidance covers eye strain from long encoding sessions on dense grids during peak tax season."),
    ("Y", "", "N", "A wrong assessment level or a broken formula chain is not flagged. The error flows straight into the tax due."),
    ("Y", "", "N", "Documentation describes features and functions, not municipal tasks such as a Transfer of Assessment."),
    ("Y", "", "Y", "Supported browsers and offline requirements (Chrome or Edge plus the Docs Offline extension) are documented."),
    ("Y", "", "N", "Crowded counters, brownouts, and shared PCs in municipal halls are outside the described context."),
    ("Y", "", "N", "For RPT work, the context lacks the approval chain between Assessor, Treasurer, and Provincial Capitol."),
    ("Y", "", "Y", "General office and personal data work is the stated intended context."),
    ("Y", "", "Y", "Collaboration, computation, and sharing requirements are stated in the product\u2019s documentation."),
    ("Y", "", "N", "The split between the Assessor and Treasurer offices is not reflected. Each office keeps its own file."),
    ("Y", "", "Y", "Needs for collaboration and access from anywhere are met by cloud storage and real-time co-editing."),
    ("Y", "", "N", "Unstable rural internet is only partly addressed. Offline mode has to be set up in advance on each browser."),
    ("Y", "", "Y", "Offline, mobile, and desktop contexts appear in the documented conditions of use."),
    ("Y", "", "Y", "Features such as Smart Fill and assignable comments respond to observed user needs."),
    ("Y", "", "Y", "Material Design and WCAG 2.1 guidelines inform the interface."),
    ("Y", "", "N", "No published task-time, error-rate, or satisfaction targets exist for Sheets."),
    ("Y", "", "N", "LGU requirements such as per-transaction audit trails and RA 10173 controls must be added by the user."),
    ("Y", "", "Y", "Simplicity and power are balanced by keeping advanced tools in menus and offering Apps Script for advanced users."),
    ("Y", "", "N", "Rationales for human-system trade-offs are not published."),
    ("Y", "", "N", "No testable usability requirements are publicly stated."),
    ("Y", "", "N", "Not verifiable. LGU stakeholders were never involved in verifying requirements."),
    ("Y", "", "Y", "Docs, Sheets, and Slides behave consistently, with shared menus, the same sharing model, and the same version history."),
    ("Y", "", "Y", "Requirements change with releases. New functions and the Tables feature were added in response to user demand."),
    ("Y", "", "Y", "The toolbar, formula bar, and context menus are designed as one consistent workspace (Figure 1)."),
    ("Y", "", "Y", "Features reach users first through early-access and Rapid Release tracks, which act as working prototypes."),
    ("Y", "", "Y", "Feedback sent through Help > Help Sheets improve feeds into feature revisions."),
    ("Y", "", "Y", "Material Design specifications give designers and engineers a shared design language."),
    ("Y", "", "Y", "Formulas compute market value, assessed value, and tax due instantly, which fits the clerk\u2019s computation task (Figures 3\u20134)."),
    ("Y", "", "N", "Error codes such as #VALUE! need a hover to explain them, and hard-coded rates mean nothing to a new clerk (Figures 4 and 5)."),
    ("Y", "", "Y", "Behavior and shortcuts match Excel, so the product does what users expect."),
    ("Y", "", "Y", "Function autocomplete with argument hints and the shortcut list (Ctrl+/) support learning."),
    ("Y", "", "Y", "Users control pace and navigation, and filter views let one clerk sort without disturbing others."),
    ("Y", "", "Y", "Undo, version restore, and data validation allow recovery from mistakes (Figures 7 and 8)."),
    ("Y", "", "Y", "Zoom, custom number formats, themes, and freeze panes let users adjust the workspace."),
    ("Y", "", "Y", "Choosing a browser-based, cloud-synced grid is a clear high-level design decision."),
    ("Y", "", "N", "RPT sub-tasks (appraisal, approval, endorsement, payment posting) are not modelled. Clerks improvise structure with columns."),
    ("Y", "", "N", "Recalculation is automated, but matching records between offices stays manual (Figure 5)."),
    ("Y", "", "Y", "Cells, dropdown chips, checkboxes, and smart chips are well-defined interaction objects."),
    ("Y", "", "Y", "Direct manipulation, menus, and typed formula entry are combined appropriately."),
    ("Y", "", "N", "Nothing enforces the order of steps. A record can be marked \u201cPaid\u201d before it is assessed, and there are no deadlines."),
    ("Y", "", "Y", "Menus (File, Edit, View, Insert, Format, Data, Tools) group functions logically, and tabs separate datasets."),
    ("Y", "", "Y", "The software design follows WCAG 2.1 and Material Design. No hardware is involved."),
    ("Y", "", "Y", "Live features in early-access releases are realistic prototypes."),
    ("Y", "", "Y", "Workspace Updates posts note changes made in response to user feedback."),
    ("Y", "", "N", "Cost-benefit analyses of design changes are not publicly documented."),
    ("Y", "", "Y", "Continuous cloud deployment allows changes at any time without users reinstalling anything."),
    ("Y", "", "Y", "The feedback tool, the Docs Editors Community forum, and the Workspace Updates blog form ongoing channels."),
    ("Y", "", "Y", "Workspace Updates posts explain what changed, who is affected, and why."),
    ("Y", "", "Y", "Updates state edition availability and rollout pace, which takes admin constraints into account."),
    ("Y", "", "Y", "ACR testing and staged rollouts show that evaluation is an ongoing activity."),
    ("Y", "", "N", "Early concept evaluation for Sheets is undocumented."),
    ("Y", "", "Y", "ACRs combine automated checks with expert review using assistive technologies."),
    ("Y", "", "Y", "Early-access programs set aside a user base for early feedback."),
    ("Y", "", "Y", "Release tracks fit evaluation into the rollout calendar."),
    ("Y", "", "N", "No published testing covers government revenue or LGU record-keeping scenarios."),
    ("Y", "", "N", "How issues are prioritized is internal and not published."),
    ("Y", "", "Y", "Fixes and changes are communicated through the Workspace Updates blog and release notes."),
    ("Y", "", "Y", "ACRs are prepared by Google\u2019s accessibility specialists using WCAG methods."),
    ("Y", "", "Y", "Manual screen-reader testing plus automated checks are appropriate methods for accessibility evaluation."),
    ("Y", "", "N", "Results of summative usability validation are not published."),
    ("Y", "", "N", "High-risk uses such as computing local taxes are not treated as a separate evaluation case."),
    ("Y", "", "Y", "Early-access users do real work with pre-release features instead of watching demonstrations."),
    ("Y", "", "Y", "As a cloud service, Sheets allows Google to monitor feature use and collect feedback over time."),
    ("Y", "", "N", "Monitoring is aggregate, so problems specific to small LGU users (e.g., broken VLOOKUP chains) would not surface early."),
]

SECTION_F_REFS = [
    "Norberto Arrocena Chinilla and Glenne Berja Lagura. 2025. Enhanced tax revenue assessment and collection system through the lens of the municipal treasurers and assessors. International Journal for Multidisciplinary Research (IJFMR) 7, 4 (2025), 1\u201342. DOI: https://doi.org/10.36948/ijfmr.2025.v07i04.51726",
    "Department of Information and Communications Technology. 2023. Electronic Real Property Tax System (eRPT) Implementation Guidelines and Local Government Technical Standards. DICT, Quezon City, Philippines.",
    "Google. 2026. Accessibility Conformance Reports. Google Accessibility. Retrieved October 13, 2026 from https://www.google.com/accessibility/conformance-reports/",
    "Google. 2026. Create an in-cell dropdown list. Google Docs Editors Help. Retrieved October 13, 2026 from https://support.google.com/docs/answer/186103",
    "Google. 2026. Files you can store in Google Drive. Google Drive Help. Retrieved October 13, 2026 from https://support.google.com/drive/answer/37603",
    "Google. 2026. Find what\u2019s changed in a file. Google Docs Editors Help. Retrieved October 13, 2026 from https://support.google.com/docs/answer/190843",
    "Google. 2026. Protect, hide & edit sheets. Google Docs Editors Help. Retrieved October 13, 2026 from https://support.google.com/docs/answer/1218656",
    "Google. 2026. Share files from Google Drive. Google Drive Help. Retrieved October 13, 2026 from https://support.google.com/drive/answer/2494822",
    "Google. 2026. Work on Google Docs, Sheets, & Slides offline. Google Docs Editors Help. Retrieved October 13, 2026 from https://support.google.com/docs/answer/6388102",
    "Google Workspace Updates. 2022. New functions in Google Sheets: XLOOKUP, XMATCH, LAMBDA, and named functions (August 2022 posts). Retrieved October 13, 2026 from https://workspaceupdates.googleblog.com/2022/08/",
    "Google Workspace Updates. 2024. Convert data ranges to tables in Google Sheets (May 2024 posts). Retrieved October 13, 2026 from https://workspaceupdates.googleblog.com/2024/05/",
    "International Organization for Standardization. 2006. ISO 9241-110:2006: Ergonomics of human-system interaction \u2014 Part 110: Dialogue principles. ISO, Geneva, Switzerland.",
    "International Organization for Standardization. 2010. ISO 9241-210:2010: Ergonomics of human-system interaction \u2014 Part 210: Human-centred design for interactive systems. ISO, Geneva, Switzerland.",
    "Ma. Angelica Mendoza. 2025. Comparative study on the manual and computer-assisted assessment of real property taxes in Victoria, Laguna. International Journal of Research Publications (IJRP) 173, 1 (2025), 1104\u20131148. DOI: https://doi.org/10.47119/10.47119/IJRP1001731520257969",
    "Republic of the Philippines. 1991. Republic Act No. 7160: An Act Providing for a Local Government Code of 1991. Official Gazette of the Republic of the Philippines, Manila.",
    "Republic of the Philippines. 2012. Republic Act No. 10173: Data Privacy Act of 2012. Official Gazette of the Republic of the Philippines, Manila.",
    "Republic of the Philippines. 2024. Republic Act No. 12001: Real Property Valuation and Assessment Reform Act (RPVARA). Official Gazette of the Republic of the Philippines, Manila.",
    "Maria Santos and Juan Reyes. 2024. Assessing administrative efficiency and revenue collection bottlenecks in municipal real property taxation. Philippine Journal of Public Administration 68, 2 (2024), 112\u2013135.",
]

BANNED = ["furthermore", "moreover", "in conclusion", "it is crucial", "it is important to note",
          "pivotal role", "cornerstone", "underscores the necessity", "masterfully", "delves into",
          "testament to", "seamless", "holistic", "synergy"]

# --------------------------------------------------------------------------------------
# DOCX HELPERS
# --------------------------------------------------------------------------------------
W_P, W_R, W_HL, W_PPR = qn("w:p"), qn("w:r"), qn("w:hyperlink"), qn("w:pPr")


def text_of(el):
    return "".join(t.text or "" for t in el.iter(qn("w:t")))


def has_sectpr(el):
    return el.tag == W_P and el.find(".//" + qn("w:sectPr")) is not None


def is_heading(el, doc):
    if el.tag != W_P:
        return False
    sty = Paragraph(el, doc._body).style
    return sty is not None and sty.name.lower().startswith("heading")


def blank_from(proto):
    """Copy a prototype paragraph, keeping only its paragraph properties."""
    p = copy.deepcopy(proto)
    for ch in list(p):
        if ch.tag != W_PPR:
            p.remove(ch)
    ppr = p.find(W_PPR)
    if ppr is not None:  # drop section/page-break remnants
        for s in ppr.findall(qn("w:sectPr")):
            ppr.remove(s)
    return p


class Builder:
    def __init__(self, doc, protos):
        self.doc, self.pr = doc, protos

    def para(self, kind, *args):
        d = self.doc
        if kind == "p":
            el = blank_from(self.pr["body"]); P = Paragraph(el, d._body); P.add_run(args[0])
        elif kind == "sub":
            el = blank_from(self.pr["sub"]); P = Paragraph(el, d._body); P.add_run(args[0]).bold = True
        elif kind == "label":
            el = blank_from(self.pr["label"]); P = Paragraph(el, d._body)
            P.add_run(args[0]).bold = True; P.add_run(args[1])
        elif kind == "caption":
            el = blank_from(self.pr["caption"]); P = Paragraph(el, d._body); P.add_run(args[0]).italic = True
        elif kind == "ref":
            el = blank_from(self.pr["ref"]); P = Paragraph(el, d._body); P.add_run(args[0])
        elif kind == "blank":
            el = blank_from(self.pr["body"])
        elif kind == "image":
            el = blank_from(self.pr["body"]); P = Paragraph(el, d._body)
            P.alignment = WD_ALIGN_PARAGRAPH.CENTER
            P.paragraph_format.keep_with_next = True
            P.add_run().add_picture(args[0], width=Inches(args[1] if len(args) > 1 else 6.5))
        elif kind == "pagebreak":
            el = blank_from(self.pr["body"]); r = OxmlElement("w:r"); br = OxmlElement("w:br")
            br.set(qn("w:type"), "page"); r.append(br); el.append(r)
        else:
            raise ValueError(kind)
        return el

    def expand(self, items):
        out = []
        for it in items:
            if it[0] == "shots":
                for fname, cap, note in SCREENSHOTS:
                    out.append(self.para("image", screenshot_or_slot(fname, cap)))
                    out.append(self.para("caption", cap))
                    out.append(self.para("p", note))
                    out.append(self.para("blank"))
            else:
                out.append(self.para(*it))
        return out


def replace_region(doc, heading_text, new_elements, stop_at_table=False):
    """Delete everything after the heading up to the next heading (keeping section-break
    paragraphs) and insert new_elements directly after the heading."""
    body = doc.element.body
    kids = list(body)
    start = next(i for i, el in enumerate(kids)
                 if el.tag == W_P and is_heading(el, doc) and text_of(el).strip() == heading_text)
    heading = kids[start]
    for el in kids[start + 1:]:
        if el.tag == qn("w:sectPr"):
            break
        if is_heading(el, doc) or (stop_at_table and el.tag == qn("w:tbl")):
            break
        if el.tag == qn("w:tbl") or has_sectpr(el):
            continue
        body.remove(el)
    anchor = heading
    for el in new_elements:
        anchor.addnext(el)
        anchor = el


def set_cell(cell, value):
    p = cell.paragraphs[0]
    runs = p.runs
    if runs:
        runs[0].text = value
        for r in runs[1:]:
            r._r.getparent().remove(r._r)
    else:
        p.add_run(value)
    for extra in cell.paragraphs[1:]:
        extra._p.getparent().remove(extra._p)


# --------------------------------------------------------------------------------------
# IMAGES
# --------------------------------------------------------------------------------------
def _font(size):
    for f in ["/System/Library/Fonts/Supplemental/Arial.ttf", "/System/Library/Fonts/Helvetica.ttc",
              "/Library/Fonts/Arial.ttf"]:
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()


def screenshot_or_slot(fname, caption):
    path = os.path.join(SHOTS, fname)
    if os.path.exists(path):
        return path
    os.makedirs(SLOTS, exist_ok=True)
    slot = os.path.join(SLOTS, fname)
    im = Image.new("RGB", (1600, 900), "#eef2f7")
    dr = ImageDraw.Draw(im)
    dr.rectangle([12, 12, 1588, 888], outline="#0f9d58", width=6)
    for x in range(12, 1588, 40):  # dashed inner frame
        dr.line([(x, 40), (x + 20, 40)], fill="#9ca3af", width=2)
        dr.line([(x, 860), (x + 20, 860)], fill="#9ca3af", width=2)
    dr.text((800, 330), "GOOGLE SHEETS SCREENSHOT SLOT", font=_font(64), fill="#0f9d58", anchor="mm")
    dr.text((800, 430), caption.split(".")[0] + "  \u2192  save as:", font=_font(40), fill="#374151", anchor="mm")
    dr.text((800, 500), "images/gsheets/" + fname, font=_font(44), fill="#111827", anchor="mm")
    dr.text((800, 600), "See gsheets_mock/SCREENSHOT_GUIDE.md, then re-run build_case_study.py",
            font=_font(30), fill="#6b7280", anchor="mm")
    im.save(slot)
    return slot


# --------------------------------------------------------------------------------------
# BUILD
# --------------------------------------------------------------------------------------
def main():
    assert len(CHECKLIST) == 103, len(CHECKLIST)
    all_text = " ".join(str(x) for blk in (SECTION_A, SECTION_B, SECTION_C, SECTION_D_INTRO, SECTION_D_BODY,
                                           SECTION_E) for it in blk for x in it[1:])
    all_text += " ".join(c[3] for c in CHECKLIST) + " ".join(s[1] + s[2] for s in SCREENSHOTS)
    for b in BANNED:
        assert b not in all_text.lower(), "banned phrase: " + b

    doc = docx.Document(TEMPLATE)
    body = doc.element.body
    paras = [el for el in body if el.tag == W_P]

    def find(pred):
        return next(el for el in paras if pred(text_of(el)))

    protos = {
        "body": find(lambda t: t.startswith("The Department of Information")),
        "sub": find(lambda t: t.strip() == "1. Primary User Groups"),
        "label": find(lambda t: t.startswith("Municipal Assessor Personnel")),
        "caption": find(lambda t: t.startswith("Figure 1. Architectural")),
        "ref": find(lambda t: t.startswith("Norberto Arrocena")),
    }
    protos = {k: copy.deepcopy(v) for k, v in protos.items()}
    b = Builder(doc, protos)

    # Cover subtitle
    cover = doc.paragraphs
    for idx, (txt, size) in {3: ("Evaluated System: Google Sheets", 15),
                             4: ("A Spreadsheet-Based Real Property Assessment Recording and Computation Tool", 12)}.items():
        P = cover[idx]
        P.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = P.add_run(txt); r.font.size = Pt(size); r.bold = idx == 3; r.italic = idx == 4

    met = sum(1 for c in CHECKLIST if c[2] == "Y")
    fmt = {"met": met, "total": len(CHECKLIST), "notmet": len(CHECKLIST) - met}
    d_body = [(k, t.format(**fmt)) for k, t in SECTION_D_BODY]

    replace_region(doc, "A. System Overview", b.expand(SECTION_A))
    replace_region(doc, "B. Identified Users and Context of Use", b.expand(SECTION_B))
    replace_region(doc, "C. Usability Strengths and Issues", b.expand(SECTION_C + [("blank",)]))
    replace_region(doc, "D. Evaluation Using ISO 9241-210 Framework",
                   b.expand(SECTION_D_INTRO + d_body + [("blank",)]))
    replace_region(doc, "E. Recommendations for Improvement and Connection to the Proposed System",
                   b.expand(SECTION_E + [("blank",)]))

    # Checklist intro (between heading and table)
    intro = [b.para("sub", "Completed ISO 9241-210:2010 Conformance Checklist (Table B.1): Google Sheets"),
             b.para("blank"), b.para("p", CHECKLIST_INTRO),
             b.para("p", f"Summary: {met} of {len(CHECKLIST)} items met; {len(CHECKLIST) - met} not met; "
                         f"all {len(CHECKLIST)} items judged applicable."),
             b.para("blank")]
    replace_region(doc, "Conformance Checklist", intro, stop_at_table=True)

    table = doc.tables[0]
    for row, (app, reason, ok, comment) in zip(table.rows[1:], CHECKLIST):
        c = row.cells
        set_cell(c[2], app); set_cell(c[3], reason)
        set_cell(c[4], "Y" if ok == "Y" else ""); set_cell(c[5], "N" if ok == "N" else "")
        set_cell(c[6], comment)

    # Section F
    f_items = [b.para("blank"),
               b.para("p", "This section presents the workflow and life-cycle diagrams that summarize the "
                           "evaluation, followed by the formal references."),
               b.para("sub", "Appendix 1: System Workflow Visuals and Architectural Diagrams"),
               b.para("image", os.path.join(IMG, "gsheets_workflow_comparison.png")),
               b.para("caption", "Figure 9. Workflow Comparison: Google Sheets-Based RPT Record Keeping vs. "
                                 "the Proposed System\u2019s Three-Tier Synchronized Web Platform "
                                 "(Authors\u2019 Synthesis, 2026)."),
               b.para("blank"),
               b.para("image", os.path.join(IMG, "gsheets_iso_hcd_cycle.png")),
               b.para("caption", "Figure 10. ISO 9241-210 Human-Centered Design Life Cycle: Google Sheets "
                                 "Conformance vs. LGU Deployment Gaps vs. the Proposed System\u2019s Agile "
                                 "Methodology (Authors\u2019 Synthesis, 2026)."),
               b.para("pagebreak"),
               b.para("sub", "Appendix 2: Formal References")]
    f_items += [b.para("ref", r) for r in SECTION_F_REFS]
    replace_region(doc, "F. References and Appendices", f_items)

    # Ask Word to refresh the TOC page numbers on open
    settings = doc.settings.element
    if settings.find(qn("w:updateFields")) is None:
        uf = OxmlElement("w:updateFields"); uf.set(qn("w:val"), "true"); settings.append(uf)

    doc.save(OUTPUT)
    found = [s[0] for s in SCREENSHOTS if os.path.exists(os.path.join(SHOTS, s[0]))]
    print(f"Saved: {OUTPUT}")
    print(f"Checklist: {met}/{len(CHECKLIST)} met")
    print(f"Screenshots embedded: {len(found)}/8 {found}")


if __name__ == "__main__":
    main()
