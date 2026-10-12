import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable, Image
)
from reportlab.pdfgen import canvas

PDF_DIR = r"c:\Users\User\Desktop\Assesors Office\Tools\PDFS"
ETC_DIR = r"c:\Users\User\Desktop\Assesors Office\Tools\Etc"
TOOLS_DIR = r"c:\Users\User\Desktop\Assesors Office\Tools"

os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(ETC_DIR, exist_ok=True)
os.makedirs(TOOLS_DIR, exist_ok=True)

LOGO_PATH = os.path.join(ETC_DIR, "unc_logo.png")

PAGE_W, PAGE_H = letter
MARGIN = 36  # 0.5 inch margins
USABLE_W = PAGE_W - 2 * MARGIN  # 540 pt (7.5 in)

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 7.5)
        self.setFillColor(colors.HexColor("#555555"))
        footer_text = "University of Nueva Caceres • School of Computer and Information Sciences • BSIT Capstone AY 2026-2027"
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawString(MARGIN, 22, footer_text)
        self.drawRightString(PAGE_W - MARGIN, 22, page_str)
        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(MARGIN, 32, PAGE_W - MARGIN, 32)
        self.restoreState()

styles = {
    'H1_UNC': ParagraphStyle('H1_UNC', fontName='Helvetica-Bold', fontSize=10, leading=12, textColor=colors.HexColor("#7A1113"), alignment=1),
    'H2_UNC': ParagraphStyle('H2_UNC', fontName='Helvetica', fontSize=8, leading=10, textColor=colors.HexColor("#333333"), alignment=1),
    'H3_UNC': ParagraphStyle('H3_UNC', fontName='Helvetica', fontSize=7.2, leading=9, textColor=colors.HexColor("#666666"), alignment=1),
    'DocTitle': ParagraphStyle('DocTitle', fontName='Helvetica-Bold', fontSize=11.5, leading=14, textColor=colors.HexColor("#1A1A1A"), alignment=1),
    'DocSub': ParagraphStyle('DocSub', fontName='Helvetica', fontSize=8, leading=10, textColor=colors.HexColor("#444444"), alignment=1),
    'SectionHeader': ParagraphStyle('SectionHeader', fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=colors.white),
    'Body': ParagraphStyle('Body', fontName='Helvetica', fontSize=7.8, leading=10.2, textColor=colors.HexColor("#222222")),
    'BodyBold': ParagraphStyle('BodyBold', fontName='Helvetica-Bold', fontSize=7.8, leading=10.2, textColor=colors.HexColor("#222222")),
    'BodySmall': ParagraphStyle('BodySmall', fontName='Helvetica', fontSize=7.2, leading=9.2, textColor=colors.HexColor("#333333")),
    'ItemText': ParagraphStyle('ItemText', fontName='Helvetica', fontSize=7.8, leading=10.2, textColor=colors.HexColor("#222222")),
    'ItemSub': ParagraphStyle('ItemSub', fontName='Helvetica-Oblique', fontSize=7.2, leading=9.2, textColor=colors.HexColor("#444444")),
    'CalloutTitle': ParagraphStyle('CalloutTitle', fontName='Helvetica-Bold', fontSize=8, leading=10, textColor=colors.HexColor("#7A1113")),
    'CalloutP': ParagraphStyle('CalloutP', fontName='Helvetica', fontSize=7.5, leading=9.5, textColor=colors.HexColor("#222222")),
    'TableHeader': ParagraphStyle('TableHeader', fontName='Helvetica-Bold', fontSize=7.5, leading=9.5, textColor=colors.white, alignment=1),
    'TableCell': ParagraphStyle('TableCell', fontName='Helvetica', fontSize=7.2, leading=9.2, textColor=colors.HexColor("#222222")),
    'TableCellCenter': ParagraphStyle('TableCellCenter', fontName='Helvetica', fontSize=7.2, leading=9.2, textColor=colors.HexColor("#222222"), alignment=1),
    'TableCellBold': ParagraphStyle('TableCellBold', fontName='Helvetica-Bold', fontSize=7.2, leading=9.2, textColor=colors.HexColor("#222222")),
}

def create_header(doc_title, doc_sub=""):
    story = []
    text_content = [
        Paragraph("<b>UNIVERSITY OF NUEVA CACERES</b>", styles['H1_UNC']),
        Paragraph("School of Computer and Information Sciences", styles['H2_UNC']),
        Paragraph("Bachelor of Science in Information Technology • Naga City, Camarines Sur", styles['H3_UNC']),
    ]
    if os.path.exists(LOGO_PATH):
        img = Image(LOGO_PATH, width=0.5*inch, height=0.5*inch)
        header_table = Table([[img, text_content]], colWidths=[0.6*inch, USABLE_W - 0.6*inch])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN', (0,0), (0,0), 'CENTER'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(header_table)
    else:
        for p in text_content:
            story.append(p)
            
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#7A1113"), spaceBefore=2, spaceAfter=6))
    story.append(Paragraph(doc_title.upper(), styles['DocTitle']))
    if doc_sub:
        story.append(Spacer(1, 2))
        story.append(Paragraph(doc_sub, styles['DocSub']))
    story.append(Spacer(1, 6))
    return story

def make_banner(text):
    p = Paragraph(f"<b>{text.upper()}</b>", styles['SectionHeader'])
    t = Table([[p]], colWidths=[USABLE_W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#7A1113")),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    return t

def make_callout_box(title, text_list):
    content = []
    if title:
        content.append(Paragraph(f"<b>{title}</b>", styles['CalloutTitle']))
        content.append(Spacer(1, 2))
    for t in text_list:
        content.append(Paragraph(t, styles['CalloutP']))
    t = Table([[content]], colWidths=[USABLE_W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8F9FA")),
        ('BOX', (0,0), (-1,-1), 0.75, colors.HexColor("#CED4DA")),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    return t

# ==============================================================================
# STEP 01: EXPERT VALIDATION SHEET (PRE-DEPLOYMENT)
# ==============================================================================
def generate_step_01():
    out_pdf = os.path.join(PDF_DIR, "01_Expert_Validation_Sheet_Pre_Deployment.pdf")
    doc = SimpleDocTemplate(out_pdf, pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    story = create_header(
        "Expert Validation Sheet for Research Instruments",
        "Step 1: Content Validity, Construct Adequacy, and Methodological Rigor Evaluation Protocol"
    )
    
    story.append(make_callout_box("RESEARCH TIMELINE STAGE: STEP 1 (PRE-DEPLOYMENT VALIDATION)", [
        "<b>When to Use:</b> Submit this form to expert validators <i>before</i> field deployment to formally evaluate and certify the research tools.",
        "<b>Study Title:</b> Needs Assessment for a Real Property Assessment Tracking and Inter-Office Synchronization System: Resolving Disconnected Records and Workflow Delays in Municipal Assessor and Treasurer Offices in Pasacao",
        "<b>Student Researchers:</b> Rizalina A. Ortega | John Kenneth P. Calubad | Christian Louise O. Asido",
        "<b>Instruments Evaluated by the Validator:</b><br/>"
        "&bull; <b>Step 2 Tool:</b> Participant Consent and Data Privacy Agreement Form (Ethical & RA 10173 Compliance)<br/>"
        "&bull; <b>Step 3 Tool:</b> Stakeholder Needs Assessment Interview Guide (Qualitative Bottlenecks & Requirements)<br/>"
        "&bull; <b>Step 4 Tool:</b> Time-Motion and Workflow Latency Log Sheet (Quantitative Baseline & Turnaround Time)<br/>"
        "&bull; <b>Step 5 Tool:</b> Software Quality Evaluation Survey (Quantitative ISO/IEC 25010 Standards)",
    ]))
    story.append(Spacer(1, 5))
    
    # Validator Profile Grid
    val_data = [
        [Paragraph("<b>Validator Name:</b> ___________________________", styles['BodySmall']),
         Paragraph("<b>Date of Evaluation:</b> ___________________________", styles['BodySmall'])],
        [Paragraph("<b>Current Position / Designation:</b> ___________________________", styles['BodySmall']),
         Paragraph("<b>Institutional Affiliation:</b> ___________________________", styles['BodySmall'])],
        [Paragraph("<b>Area of Professional Expertise:</b><br/>[  ] Information Technology / Software Engineering<br/>[  ] Public Administration / Local Governance (LGU)<br/>[  ] Academic Research / Statistical Methods<br/>[  ] Other: ___________________________", styles['BodySmall']),
         Paragraph("<b>Highest Educational Attainment:</b><br/>[  ] Master's Degree (MS / MIT / MPA)<br/>[  ] Doctorate Degree (PhD / DIT / DPA)<br/>[  ] Professional License (CPA / REA / REB)<br/>Years in Field: ______ years", styles['BodySmall'])],
    ]
    t_val = Table(val_data, colWidths=[USABLE_W * 0.52, USABLE_W * 0.48])
    t_val.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CCCCCC")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E5E5E5")),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_val)
    story.append(Spacer(1, 5))
    
    story.append(make_callout_box("RATING SCALE & BENCHMARK", [
        "<b>5 = Strongly Agree</b> (Exceptionally satisfied) &bull; <b>4 = Agree</b> (Adequately satisfied) &bull; <b>3 = Neutral</b> (Moderately satisfied; revisions suggested) &bull; <b>2 = Disagree</b> (Substantial restructuring needed) &bull; <b>1 = Strongly Disagree</b> (Invalid/Inadequate)"
    ]))
    story.append(Spacer(1, 5))
    
    # Validation Matrix Table
    story.append(make_banner("Instrument Validation Matrix (Criteria Across Tools)"))
    story.append(Spacer(1, 3))
    
    val_headers = [
        Paragraph("<b>#</b>", styles['TableHeader']),
        Paragraph("<b>Validation Evaluation Criterion</b>", styles['TableHeader']),
        Paragraph("<b>Step 2<br/>(Consent)</b>", styles['TableHeader']),
        Paragraph("<b>Step 3<br/>(Interview)</b>", styles['TableHeader']),
        Paragraph("<b>Step 4<br/>(Time-Motion)</b>", styles['TableHeader']),
        Paragraph("<b>Step 5<br/>(ISO 25010)</b>", styles['TableHeader']),
    ]
    
    criteria_list = [
        ("1", "<b>Construct & Objective Alignment:</b> Items directly measure the operational variables and objectives specified in Chapter 1."),
        ("2", "<b>Clarity and Unambiguity:</b> Questions, rating indicators, and instructions are phrased clearly and free of confusing wording."),
        ("3", "<b>Language Appropriateness:</b> Vocabulary and phrasing match the professional profile of municipal and provincial personnel."),
        ("4", "<b>Content Comprehensiveness:</b> The tools comprehensively cover administrative workflows, timing metrics, and software quality."),
        ("5", "<b>Objectivity and Non-Bias:</b> Items are neutral, balanced, and free from leading questions or presupposed outcomes."),
        ("6", "<b>Measurement Scale Suitability:</b> Response options, timestamp entries, and Likert scales are operationally and statistically sound."),
        ("7", "<b>Instrument Economy:</b> Length and completion duration are realistic and respectful of municipal operating hours."),
        ("8", "<b>Ethical and Statutory Soundness:</b> Conforms strictly to the Data Privacy Act (RA 10173) and UNC ethics guidelines."),
    ]
    
    val_rows = [val_headers]
    for num, text in criteria_list:
        val_rows.append([
            Paragraph(num, styles['TableCellCenter']),
            Paragraph(text, styles['TableCell']),
            Paragraph("[ &nbsp;&nbsp;&nbsp; ]", styles['TableCellCenter']),
            Paragraph("[ &nbsp;&nbsp;&nbsp; ]", styles['TableCellCenter']),
            Paragraph("[ &nbsp;&nbsp;&nbsp; ]", styles['TableCellCenter']),
            Paragraph("[ &nbsp;&nbsp;&nbsp; ]", styles['TableCellCenter']),
        ])
    val_rows.append([
        Paragraph("<b>&sum;</b>", styles['TableCellCenter']),
        Paragraph("<b>COMPOSITE MEAN RATING</b>", styles['TableCellBold']),
        Paragraph("<b>______</b>", styles['TableCellCenter']),
        Paragraph("<b>______</b>", styles['TableCellCenter']),
        Paragraph("<b>______</b>", styles['TableCellCenter']),
        Paragraph("<b>______</b>", styles['TableCellCenter']),
    ])
    
    t_val_matrix = Table(val_rows, colWidths=[20, 280, 60, 60, 60, 60])
    t_val_matrix.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#7A1113")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#7A1113")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#D0D5DD")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#F8F9FA")),
    ]))
    story.append(KeepTogether([t_val_matrix]))
    story.append(Spacer(1, 5))
    
    story.append(make_callout_box("QUANTITATIVE VALIDITY INTERPRETATION BENCHMARK", [
        "<b>Mean Rating Ranges:</b> 4.21 – 5.00: <b>Highly Valid (Approved for administration)</b> &bull; 3.41 – 4.20: <b>Valid (Approved with minor suggested revisions)</b> &bull; 2.61 – 3.40: <b>Moderately Valid (Requires substantive revisions)</b> &bull; 1.00 – 2.60: <b>Not Valid (Substantial restructuring mandatory)</b>"
    ]))
    story.append(Spacer(1, 5))
    
    story.append(KeepTogether([make_callout_box("", [
        "<b>SPECIFIC ITEM-LEVEL COMMENTS AND QUALITATIVE RECOMMENDATIONS</b>",
        "Step 2 Tool (Consent Form): _____________________________________________________________________________",
        "Step 3 Tool (Interview Guide): __________________________________________________________________________",
        "Step 4 Tool (Time-Motion Log): __________________________________________________________________________",
        "Step 5 Tool (ISO 25010 Survey): _________________________________________________________________________",
        "<br/><b>OVERALL VALIDATION VERDICT:</b>&nbsp;&nbsp;&nbsp;&nbsp;[  ] Approved for Field Use&nbsp;&nbsp;&nbsp;&nbsp;[  ] Approved with Minor Revisions&nbsp;&nbsp;&nbsp;&nbsp;[  ] Needs Major Revisions",
        "<br/>Validator Signature: ____________________________________&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Date: ________________________",
        "Printed Name: __________________________________________&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Official Seal / Stamp: ____________"
    ])]))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print("Step 01 generated successfully.")

# ==============================================================================
# STEP 02: PARTICIPANT CONSENT AND DATA PRIVACY AGREEMENT
# ==============================================================================
def generate_step_02():
    out_pdf = os.path.join(PDF_DIR, "02_Participant_Consent_and_Data_Privacy_Agreement.pdf")
    doc = SimpleDocTemplate(out_pdf, pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    story = create_header(
        "Participant Consent and Data Privacy Agreement Form",
        "Step 2: Republic Act No. 10173 Compliance & UNC Institutional Ethics Protocol"
    )
    
    story.append(make_callout_box("RESEARCH TIMELINE STAGE: STEP 2 (PARTICIPANT ETHICAL CLEARANCE)", [
        "<b>When to Use:</b> Must be signed by municipal personnel and evaluators <i>before</i> any interview, timing observation, or system testing.",
        "<b>Project Title:</b> Needs Assessment for a Real Property Assessment Tracking and Inter-Office Synchronization System: Resolving Disconnected Records and Workflow Delays in Municipal Assessor and Treasurer Offices in Pasacao",
        "<b>Student Researchers:</b> Rizalina A. Ortega | John Kenneth P. Calubad | Christian Louise O. Asido",
        "<b>Academic Affiliation:</b> School of Computer and Information Sciences, University of Nueva Caceres (UNC), Naga City",
    ]))
    story.append(Spacer(1, 5))
    
    sections = [
        ("1. Purpose and Nature of the Research",
         "The research team is conducting a study to analyze operational workflows, administrative disconnects, and document routing latency between the Municipal Assessor's Office, the Municipal Treasurer's Office, and the Provincial Assessor's Office in Pili. The ultimate objective is to design, develop, and evaluate a web-based Real Property Assessment Tracking and Inter-Office Synchronization System that eliminates manual cross-checking and streamlines document routing."),
        
        ("2. Participant Roles and Required Activities",
         "As a designated municipal or provincial official, administrative staff member, or technical expert, you may be invited to participate in one or more of the following evaluation activities:<br/>"
         "&bull; <b>Stakeholder Needs Assessment Interview:</b> Answering semi-structured questions regarding daily office workflows, document verification, legacy archives, and inter-office bottlenecks (approx. 20–30 minutes).<br/>"
         "&bull; <b>Time-Motion Workflow Observation:</b> Allowing the research team to observe and record chronological processing durations for routine assessment and reconciliation tasks (approx. 15–30 minutes).<br/>"
         "&bull; <b>Software Pilot Testing & ISO/IEC 25010 Evaluation:</b> Testing the prototype web application and completing an evaluation survey assessing functional suitability, efficiency, usability, security, and reliability (approx. 20–30 minutes)."),
        
        ("3. Voluntary Participation and Right of Withdrawal",
         "Your participation in this research study is entirely voluntary. You reserve the absolute right to refuse to answer any individual question, decline to participate in specific procedures, or terminate your participation at any time without penalty, prejudice, or impact on your official employment status."),
        
        ("4. Strict Confidentiality and Data Privacy Protections (RA 10173)",
         "In strict compliance with Republic Act No. 10173 (Data Privacy Act of 2012), the research team enforces rigorous data protection safeguards:<br/>"
         "&bull; <b>Strict Anonymity:</b> Published findings, academic manuscripts, and statistical tables will strictly report aggregate metrics and anonymized designations. Personal names will never appear.<br/>"
         "&bull; <b>Zero Exposure of Citizen Records:</b> During development, testing, and simulation trials, only masked or synthetic dummy property records will be utilized. No actual private taxpayer financial data or confidential titles will be recorded.<br/>"
         "&bull; <b>Data Security & Retention:</b> All qualitative notes, observation sheets, and survey data will be securely stored in encrypted academic repositories accessible solely to the research proponents and their academic adviser, and will be destroyed following final project completion.<br/>"
         "&bull; <b>Audio Recording Consent:</b> Audio recording during interviews is strictly optional and requires explicit affirmative consent. Recordings will serve solely for verbatim transcript transcription."),
        
        ("5. Assessment of Risks and Anticipated Benefits",
         "There are no foreseeable physical, legal, or psychological risks associated with this study beyond routine professional office interactions. While participants receive no direct financial compensation, your expert contributions will directly shape a software intervention designed to eliminate tedious manual paper handoffs, shorten transaction delays, and improve frontline public services for local taxpayers."),
        
        ("6. Research Inquiries and Institutional Contact",
         "If you have inquiries, concerns, or require clarification regarding this study or your rights under the Data Privacy Act, you may contact the student researchers or the Capstone Committee via the School of Computer and Information Sciences, University of Nueva Caceres, J. Hernandez Ave., Naga City, Camarines Sur."),
    ]
    
    for title, text in sections:
        sec_content = [
            Paragraph(f"<b>{title}</b>", styles['BodyBold']),
            Spacer(1, 2),
            Paragraph(text, styles['BodySmall']),
        ]
        story.append(KeepTogether(sec_content))
        story.append(Spacer(1, 4))
        
    story.append(make_banner("Affirmative Participant Consent and Authorization"))
    story.append(Spacer(1, 3))
    
    consent_table_data = [
        [Paragraph("I have read and understood the information provided in this Informed Consent and Data Privacy Agreement Form. I have been afforded sufficient opportunity to ask questions, which were answered to my satisfaction. I voluntarily agree to participate in this academic research study.", styles['BodySmall'])],
        [Paragraph("<b>Audio Recording Authorization:</b><br/>[  ] <b>YES</b>, I consent to audio recording for note-taking purposes only.<br/>[  ] <b>NO</b>, I do not consent to audio recording; written notes only.", styles['BodySmall'])],
        [Table([
            [Paragraph("<b>Participant Printed Name:</b> ___________________________", styles['BodySmall']),
             Paragraph("<b>Official Designation / Position:</b> ___________________________", styles['BodySmall'])],
            [Paragraph("<b>Participant Signature:</b> ___________________________", styles['BodySmall']),
             Paragraph("<b>Date Signed:</b> ___________________________", styles['BodySmall'])],
            [Paragraph("<b>Researcher Printed Name:</b> ___________________________", styles['BodySmall']),
             Paragraph("<b>Researcher Signature:</b> ___________________________", styles['BodySmall'])],
        ], colWidths=[USABLE_W * 0.52, USABLE_W * 0.48])],
    ]
    t_consent = Table(consent_table_data, colWidths=[USABLE_W])
    t_consent.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#7A1113")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E5E5E5")),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FDF7F7")),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(KeepTogether([t_consent]))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print("Step 02 generated successfully.")

# ==============================================================================
# STEP 03: STAKEHOLDER NEEDS ASSESSMENT INTERVIEW GUIDE
# ==============================================================================
def generate_step_03():
    out_pdf = os.path.join(PDF_DIR, "03_Stakeholder_Needs_Assessment_Interview_Guide.pdf")
    doc = SimpleDocTemplate(out_pdf, pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    story = create_header(
        "Stakeholder Needs Assessment Interview Guide",
        "Step 3: Semi-Structured Qualitative Protocol for Municipal & Provincial Personnel"
    )
    
    story.append(make_callout_box("RESEARCH TIMELINE STAGE: STEP 3 (NEEDS ASSESSMENT & PROBLEM DISCOVERY)", [
        "<b>When to Use:</b> Conducted with municipal and provincial officers during the requirements analysis phase to document workflow bottlenecks, disconnected records, and system requirements.",
        "<b>Target Offices:</b> Municipal Assessor's Office, Municipal Treasurer's Office, Provincial Assessor's Office (Pili).",
        "<b>Student Researchers:</b> Rizalina A. Ortega | John Kenneth P. Calubad | Christian Louise O. Asido",
        "<b>Data Privacy Notice (RA 10173):</b> All responses are confidential and used solely for academic research. No personal taxpayer data is recorded.",
    ]))
    story.append(Spacer(1, 5))
    
    details_data = [
        [Paragraph("<b>Date of Interview:</b> ____________________", styles['BodySmall']),
         Paragraph("<b>Interviewer:</b> ____________________", styles['BodySmall'])],
        [Paragraph("<b>Target Office:</b> [  ] Municipal Assessor's Office    [  ] Municipal Treasurer's Office    [  ] Provincial Assessor's Office", styles['BodySmall']),
         Paragraph("<b>Recorded:</b> [  ] Yes (Consented)  [  ] Notes Only", styles['BodySmall'])],
        [Paragraph("<b>Designation / Position:</b> ____________________", styles['BodySmall']),
         Paragraph("<b>Years of Service in Office:</b> ______ years", styles['BodySmall'])],
    ]
    det_table = Table(details_data, colWidths=[USABLE_W * 0.65, USABLE_W * 0.35])
    det_table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CCCCCC")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E5E5E5")),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFFFFF")),
    ]))
    story.append(det_table)
    story.append(Spacer(1, 6))
    
    sections = [
        ("Part A: Office Setup and Personnel Profile (All Participating Offices)", [
            "1. How many staff members currently work in your office, and what are their primary functional roles?",
            "2. On average, how many property tax transactions or client requests does your office handle on a typical day versus during peak deadline months?",
            "3. Which specific months or days of the week experience the highest volume of client visits, and what drives this surge?",
            "4. What are the most frequent counter requests, certifications, or official documents requested by property owners and other offices?",
        ]),
        ("Part B: Municipal Assessor's Office Workflows and Valuation Procedures", [
            "5. Could you walk us through the step-by-step process of handling a Transfer of Assessment, from initial document submission at the counter to final release of the new Tax Declaration?",
            "6. What specific documentary prerequisites must property owners submit for each major transaction?<br/>&nbsp;&nbsp;&nbsp;&nbsp;<b>a.</b> New Tax Declaration (newly declared land, building/house, or machinery)<br/>&nbsp;&nbsp;&nbsp;&nbsp;<b>b.</b> Transfer of Ownership (Deed of Sale, BIR CAR, transfer tax receipt, previous clearances)<br/>&nbsp;&nbsp;&nbsp;&nbsp;<b>c.</b> Reassessment / Correction of Value (physical appraisal, reclassification)<br/>&nbsp;&nbsp;&nbsp;&nbsp;<b>d.</b> Issuance of Clearances (Certificate of Land Holding, Certificate of No Property, Certificate of No Improvement)",
            "7. Once documents are submitted, how do personnel verify authenticity, and who conducts intermediate review and final approval prior to document release?",
            "8. How does your office compute assessed values and tax liabilities from start to finish? Is this done manually using physical appraisal tables, automated spreadsheets, or electronic software?",
            "9. Where and in what physical/electronic format are property records and assessment rolls currently stored? How do personnel retrieve an existing parcel record when an owner inquires?",
            "10. If your office currently utilizes a software system, what specific functions does it perform effectively, where does it fall short, and which procedural steps still strictly require paper handoffs?",
            "11. How frequently do clients experience repeated visits (pabalik-balik) due to incomplete paperwork or clerical errors, and which transaction types cause this most frequently?",
            "12. How does your office organize, protect, and retrieve decades-old legacy property archives (dating back to 1949 or earlier) against wear, deterioration, or loss?",
        ]),
        ("Part C: Municipal Treasurer's Office Workflows and Record Reconciliation", [
            "13. How does your office receive updated assessment rolls and tax declarations from the Assessor's Office? How frequently does this data exchange occur, and in what format?",
            "14. What is your step-by-step process for verifying whether a property tax has been paid before issuing official receipts or clearances? How do you link payment receipts to property records?",
            "15. On average, how many staff hours per week or month are spent manually cross-checking real property payment records against the municipal assessment roll?",
            "16. How does your office identify, track, and follow up delinquent or uncollected real property accounts?",
            "17. How are statutory prompt-payment discounts, interest penalties, and tax clearances computed and verified across multi-year assessment histories?",
            "18. Does your office utilize an electronic collection database or spreadsheet? Is it digitally synchronized with the Assessor's property records, or does it operate independently?",
            "19. What discrepancies or data mismatches happen most frequently between assessment records and payment rolls, and what protocol is followed to reconcile them?",
        ]),
        ("Part D: Provincial Assessor's Office Coordination and Approval (Pili Endorsement)", [
            "20. Which specific assessment transactions strictly require review, endorsement, and final statutory approval from the Provincial Assessor's Office?",
            "21. How are assessment packets physically transported from the municipality to the Provincial Capitol in Pili (physical courier, personnel delivery, mail), and what transit schedule is maintained?",
            "22. On average, how long does the provincial review and approval cycle take from the date of submission to physical return to the municipality, and what factors cause delays?",
            "23. What are the most common deficiencies or clerical errors that result in submitted packets being rejected or returned to the municipality for corrections?",
            "24. Is digital review or electronic endorsement of assessment documents permissible or viable under existing administrative standards? What technical and security safeguards would be required?",
            "25. How does your office currently communicate document processing status, endorsements, or required revisions back to municipal personnel?",
        ]),
        ("Part E: Inter-Office Coordination and Information Flow (Assessor, Treasurer, Provincial)", [
            "26. Which assessment and collection transactions demand close inter-office coordination, and through what communication channels is this handled (phone calls, personal office visits, paper memos, chat)?",
            "27. Do frontline staff currently possess visibility into where a document is queued across departments? How do personnel respond when a taxpayer requests a real-time status update?",
            "28. What procedural phase represents the single largest bottleneck or source of processing latency in the end-to-end workflow?",
            "29. What core capabilities should an integrated inter-office web portal provide to eliminate manual friction between the Assessor, Treasurer, and Provincial offices?",
        ]),
        ("Part F: Time-Motion Estimates (Self-Reported Perceptions)", [
            "30. For one typical Transfer of Assessment, estimate the average duration spent on each phase:<br/>&nbsp;&nbsp;&nbsp;&nbsp;<b>a.</b> Counter requirement verification: ______ minutes<br/>&nbsp;&nbsp;&nbsp;&nbsp;<b>b.</b> Archival record search and retrieval: ______ minutes<br/>&nbsp;&nbsp;&nbsp;&nbsp;<b>c.</b> Valuation computation and encoding: ______ minutes<br/>&nbsp;&nbsp;&nbsp;&nbsp;<b>d.</b> Supervisory review and municipal approval: ______ minutes<br/>&nbsp;&nbsp;&nbsp;&nbsp;<b>e.</b> Inter-office transit and provincial approval queue: ______ days / hours<br/>&nbsp;&nbsp;&nbsp;&nbsp;<b>f.</b> Total turnaround time from filing to release: ______ days",
            "31. For cross-checking tax payment rolls against property assessment ledgers, estimate the time spent per property record: ______ minutes.",
        ]),
        ("Part G: Stakeholder Feedback on the Proposed Technical Intervention", [
            "32. The proposed system provides a web-based platform that automates document routing, monitors transaction status in real-time, and synchronizes assessment and tax payment data. Which of your routine tasks would this simplify?",
            "33. What operational or technical concerns do you foresee regarding implementation (internet stability, staff digital literacy, data privacy, workflow adaptation)?",
            "34. What specific features or safeguards are indispensable for your office to adopt the proposed system?",
            "35. Would your office be open to participating in a simulated trial or parallel run alongside current office procedures using masked dummy data?",
            "36. Are there specific local ordinances, tax codes, or institutional procedures that the software engineering team must adhere to in designing the business logic?",
            "37. Do you have any additional recommendations or insights to guide the development of the system?",
        ]),
    ]
    
    for title, q_list in sections:
        items = []
        items.append(make_banner(title))
        items.append(Spacer(1, 4))
        for q in q_list:
            items.append(Paragraph(q, styles['ItemText']))
            items.append(Spacer(1, 4))
        story.append(KeepTogether(items))
        story.append(Spacer(1, 4))
        
    story.append(KeepTogether([make_callout_box("", [
        "<b>ACKNOWLEDGMENT & PARTICIPANT SIGN-OFF</b>",
        "I hereby confirm that I have participated in this stakeholder interview and provided feedback for academic research purposes under RA 10173.",
        "<br/>Participant Signature: ____________________________________&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Date: ________________________",
        "Printed Name (Optional): __________________________________&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Designation: ____________________"
    ])]))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print("Step 03 generated successfully.")

# ==============================================================================
# STEP 04: TIME-MOTION AND WORKFLOW LATENCY LOG SHEET
# ==============================================================================
def generate_step_04():
    out_pdf = os.path.join(PDF_DIR, "04_Time_Motion_and_Workflow_Latency_Log_Sheet.pdf")
    doc = SimpleDocTemplate(out_pdf, pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    story = create_header(
        "Time-Motion and Workflow Latency Log Sheet",
        "Step 4: Objective Timing Instrument for Baseline (Pre) vs. System (Post) Processing"
    )
    
    story.append(make_callout_box("RESEARCH TIMELINE STAGE: STEP 4 (TIMING OBSERVATION - BASELINE & POST-TEST)", [
        "<b>When to Use:</b> Used in two phases: (1) <i>Baseline Run</i> before system deployment to record current manual/eRPT delays, and (2) <i>Post-Test Run</i> to record turnaround times using the web synchronization system.",
        "<b>Primary Quantitative Variables:</b> (1) <i>Document Processing Latency</i> (days/hours) and (2) <i>Record Reconciliation Time</i> (minutes per property).",
        "<b>Instructions:</b> Log timestamps for each processing phase per case code (e.g., TOA-001). Do not record personal taxpayer details.",
    ]))
    story.append(Spacer(1, 5))
    
    grid_data = [
        [Paragraph("<b>Case Transaction Code:</b> ____________________", styles['BodySmall']),
         Paragraph("<b>Run Condition:</b> [  ] BASELINE (Manual/Current)   [  ] SYSTEM (Proposed)", styles['BodySmall'])],
        [Paragraph("<b>Transaction Type:</b><br/>[  ] Transfer of Assessment<br/>[  ] New Tax Declaration / Building<br/>[  ] Reassessment / Value Revision<br/>[  ] Tax Clearance / Certification<br/>[  ] Other: ____________________", styles['BodySmall']),
         Paragraph("<b>Observed Department(s):</b><br/>[  ] Municipal Assessor's Office<br/>[  ] Municipal Treasurer's Office<br/>[  ] Provincial Assessor's Office (Pili)<br/><br/><b>Data Classification:</b><br/>[  ] Masked / Dummy Test Data&nbsp;&nbsp;[  ] Actual Workflow Log", styles['BodySmall'])],
        [Paragraph("<b>Date of Observation:</b> ____________________", styles['BodySmall']),
         Paragraph("<b>Lead Observer / Researcher:</b> ____________________", styles['BodySmall'])],
    ]
    t_grid = Table(grid_data, colWidths=[USABLE_W * 0.52, USABLE_W * 0.48])
    t_grid.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CCCCCC")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E5E5E5")),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_grid)
    story.append(Spacer(1, 5))
    
    story.append(make_banner("Table A: Phase-by-Phase Transaction Processing Latency"))
    story.append(Spacer(1, 3))
    
    t_a_headers = [
        Paragraph("<b>Ph</b>", styles['TableHeader']),
        Paragraph("<b>Operational Process Phase</b>", styles['TableHeader']),
        Paragraph("<b>Dept</b>", styles['TableHeader']),
        Paragraph("<b>Start Timestamp<br/>(Date / HH:MM)</b>", styles['TableHeader']),
        Paragraph("<b>End Timestamp<br/>(Date / HH:MM)</b>", styles['TableHeader']),
        Paragraph("<b>Duration<br/>(Min / Days)</b>", styles['TableHeader']),
        Paragraph("<b>Bottleneck / Error Remarks</b>", styles['TableHeader']),
    ]
    
    t_a_rows = [
        ["1", "Counter intake & initial documentary completeness verification", "MAO", "", "", "", ""],
        ["2", "Property record search, manual ledger/eRPT parcel retrieval", "MAO", "", "", "", ""],
        ["3", "Field appraisal calculation, valuation encoding, FAAS prep", "MAO", "", "", "", ""],
        ["4", "Municipal Assessor review, endorsement & signature", "MAO", "", "", "", ""],
        ["5", "Inter-office document transfer to Municipal Treasurer queue", "Transit", "", "", "", ""],
        ["6", "Treasurer tax payment cross-check & clearance validation", "MTO", "", "", "", ""],
        ["7", "Physical/digital batch transport to Provincial Assessor (Pili)", "Transit", "", "", "", ""],
        ["8", "Provincial appraisal evaluation, title review & formal approval", "PAO", "", "", "", ""],
        ["9", "Return transit, final municipal encoding & Tax Declaration release", "MAO", "", "", "", ""],
    ]
    
    t_a_data = [t_a_headers]
    for r in t_a_rows:
        t_a_data.append([
            Paragraph(r[0], styles['TableCellCenter']),
            Paragraph(r[1], styles['TableCell']),
            Paragraph(r[2], styles['TableCellCenter']),
            Paragraph(r[3], styles['TableCellCenter']),
            Paragraph(r[4], styles['TableCellCenter']),
            Paragraph(r[5], styles['TableCellCenter']),
            Paragraph(r[6], styles['TableCell']),
        ])
        
    t_a_table = Table(t_a_data, colWidths=[20, 160, 36, 80, 80, 64, 100])
    t_a_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#7A1113")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#7A1113")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#D0D5DD")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_a_table)
    story.append(Spacer(1, 5))
    
    summary_box_data = [
        [Paragraph("<b>TOTAL ELAPSED TIME (Intake to Release):</b><br/>______ Days ______ Hours ______ Minutes", styles['BodySmall']),
         Paragraph("<b>NET ACTIVE WORK TIME (Total Processing):</b><br/>______ Minutes / Hours", styles['BodySmall']),
         Paragraph("<b>QUEUE / INTER-OFFICE TRANSIT LATENCY:</b><br/>______ Days / Hours", styles['BodySmall'])],
    ]
    t_sum_box = Table(summary_box_data, colWidths=[USABLE_W/3, USABLE_W/3, USABLE_W/3])
    t_sum_box.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#7A1113")),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FDF7F7")),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_sum_box)
    story.append(Spacer(1, 5))
    
    story.append(make_banner("Table B: Record Reconciliation and Payment Verification Metrics"))
    story.append(Spacer(1, 3))
    
    recon_data = [
        [Paragraph("<b>Batch Reconciliation Parameter</b>", styles['TableHeader']),
         Paragraph("<b>Observed Metric Value</b>", styles['TableHeader']),
         Paragraph("<b>Operational Context & Methodological Notes</b>", styles['TableHeader'])],
        [Paragraph("Total Property Records Checked in Batch", styles['TableCellBold']),
         Paragraph("______ records", styles['TableCellCenter']),
         Paragraph("Sample batch of property accounts cross-referenced against collection rolls.", styles['TableCell'])],
        [Paragraph("Batch Verification Start Timestamp", styles['TableCellBold']),
         Paragraph("Date: ____________  Time: ________", styles['TableCellCenter']),
         Paragraph("Clock time upon initiation of record cross-checking procedure.", styles['TableCell'])],
        [Paragraph("Batch Verification Completion Timestamp", styles['TableCellBold']),
         Paragraph("Date: ____________  Time: ________", styles['TableCellCenter']),
         Paragraph("Clock time upon resolution/verification of the final record in batch.", styles['TableCell'])],
        [Paragraph("Total Batch Execution Duration", styles['TableCellBold']),
         Paragraph("______ minutes", styles['TableCellCenter']),
         Paragraph("Net active minutes elapsed to reconcile the complete record batch.", styles['TableCell'])],
        [Paragraph("Average Reconciliation Latency per Record", styles['TableCellBold']),
         Paragraph("______ min/record", styles['TableCellCenter']),
         Paragraph("Average active minutes elapsed per individual record verification.", styles['TableCell'])],
        [Paragraph("Discrepancies / Data Mismatches Detected", styles['TableCellBold']),
         Paragraph("______ mismatches", styles['TableCellCenter']),
         Paragraph("Frequency of PIN, owner, or assessment valuation mismatches identified.", styles['TableCell'])],
        [Paragraph("Reconciliation Mechanism Employed", styles['TableCellBold']),
         Paragraph("[  ] Manual Ledgers / Excel<br/>[  ] Proposed Sync Engine", styles['TableCellCenter']),
         Paragraph("Comparative verification method utilized during observation.", styles['TableCell'])],
    ]
    t_recon = Table(recon_data, colWidths=[180, 140, 220])
    t_recon.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#7A1113")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#7A1113")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#D0D5DD")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_recon)
    story.append(Spacer(1, 5))
    
    story.append(make_banner("Table C: Comparative Evaluation Summary and Reduction Analysis"))
    story.append(Spacer(1, 3))
    
    comp_data = [
        [Paragraph("<b>Performance Indicator Metric</b>", styles['TableHeader']),
         Paragraph("<b>Baseline Mean (T<sub>0</sub>)</b>", styles['TableHeader']),
         Paragraph("<b>System Mean (T<sub>1</sub>)</b>", styles['TableHeader']),
         Paragraph("<b>Absolute Difference (&Delta;)</b>", styles['TableHeader']),
         Paragraph("<b>Percentage Reduction (% Red)</b>", styles['TableHeader'])],
        [Paragraph("Document Processing Latency (Transfer of Assessment, days)", styles['TableCell']),
         Paragraph("______ days", styles['TableCellCenter']), Paragraph("______ days", styles['TableCellCenter']),
         Paragraph("______ days", styles['TableCellCenter']), Paragraph("______ %", styles['TableCellCenter'])],
        [Paragraph("Building Assessment End-to-End Latency (days)", styles['TableCell']),
         Paragraph("______ days", styles['TableCellCenter']), Paragraph("______ days", styles['TableCellCenter']),
         Paragraph("______ days", styles['TableCellCenter']), Paragraph("______ %", styles['TableCellCenter'])],
        [Paragraph("Record Reconciliation Latency per Property (minutes)", styles['TableCell']),
         Paragraph("______ min", styles['TableCellCenter']), Paragraph("______ min", styles['TableCellCenter']),
         Paragraph("______ min", styles['TableCellCenter']), Paragraph("______ %", styles['TableCellCenter'])],
        [Paragraph("Frequency of In-Person Status Inquiries per Transaction", styles['TableCell']),
         Paragraph("______ visits", styles['TableCellCenter']), Paragraph("______ visits", styles['TableCellCenter']),
         Paragraph("______ visits", styles['TableCellCenter']), Paragraph("______ %", styles['TableCellCenter'])],
    ]
    t_comp = Table(comp_data, colWidths=[200, 85, 85, 85, 85])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#7A1113")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#7A1113")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#D0D5DD")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_comp)
    story.append(Spacer(1, 4))
    
    story.append(make_callout_box("OBSERVER VERIFICATION & SUBMISSION", [
        "I hereby certify that the timestamps and duration metrics recorded in this observation log accurately reflect the observed workflow times.",
        "<br/>Observer Signature: ____________________________________&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Verification Date: ________________________",
        "Printed Name: __________________________________________&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Office / Station: ____________________"
    ]))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print("Step 04 generated successfully.")

# ==============================================================================
# STEP 05: ISO/IEC 25010 SOFTWARE QUALITY EVALUATION SURVEY
# ==============================================================================
def generate_step_05():
    out_pdf = os.path.join(PDF_DIR, "05_ISO_IEC_25010_Software_Quality_Evaluation_Survey.pdf")
    doc = SimpleDocTemplate(out_pdf, pagesize=letter, leftMargin=MARGIN, rightMargin=MARGIN, topMargin=MARGIN, bottomMargin=MARGIN)
    story = create_header(
        "Software Quality Evaluation Survey (ISO/IEC 25010)",
        "Step 5: Post-Implementation System Quality Rating Instrument"
    )
    
    story.append(make_callout_box("RESEARCH TIMELINE STAGE: STEP 5 (POST-DEVELOPMENT SYSTEM EVALUATION)", [
        "<b>When to Use:</b> Administered <i>after</i> municipal staff and IT experts test the developed web portal and document routing engine.",
        "<b>Target Respondent Groups:</b> Municipal Assessor staff, Municipal Treasurer staff, Provincial Assessor officers, and IT Experts.",
        "<b>Standard 5-Point Likert Scale:</b> [ 5 ] Excellent | [ 4 ] Very Good | [ 3 ] Good | [ 2 ] Fair | [ 1 ] Poor",
        "<b>Directions:</b> Following hands-on interaction with the system, please mark the rating (1 to 5) corresponding to each evaluation statement.",
    ]))
    story.append(Spacer(1, 5))
    
    prof_data = [
        [Paragraph("<b>Respondent Name (Optional):</b> ___________________________", styles['BodySmall']),
         Paragraph("<b>Date of Evaluation:</b> ___________________________", styles['BodySmall'])],
        [Paragraph("<b>Institutional Department / Group:</b><br/>[  ] Municipal Assessor's Office<br/>[  ] Municipal Treasurer's Office<br/>[  ] Provincial Assessor's Office (Pili)<br/>[  ] IT Expert / Systems Evaluator", styles['BodySmall']),
         Paragraph("<b>Designation / Role:</b> ___________________________<br/><br/><b>Years of Service:</b> [  ] &lt; 1 yr  [  ] 1-5 yrs  [  ] 6-10 yrs  [  ] &gt; 10 yrs<br/><br/><b>Computer Literacy:</b> [  ] Basic  [  ] Intermediate  [  ] Advanced", styles['BodySmall'])],
    ]
    t_prof = Table(prof_data, colWidths=[USABLE_W * 0.52, USABLE_W * 0.48])
    t_prof.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CCCCCC")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E5E5E5")),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_prof)
    story.append(Spacer(1, 5))
    
    iso_sections = [
        ("A. Functional Suitability", [
            ("1", "The system allows personnel to generate, update, and manage property assessment records according to statutory valuation rules."),
            ("2", "The automated document routing engine dispatches assessment packets accurately across Assessor, Treasurer, and Provincial queues."),
            ("3", "The payment synchronization module matches municipal treasury payment entries with corresponding property assessment records reliably."),
            ("4", "The platform detects and flags discrepancies or duplicate entries between assessment rolls and collection ledgers."),
            ("5", "Automated computations for assessed values, basic tax liabilities, and Special Education Fund (SEF) dues are precise and error-free."),
            ("6", "The functional scope covers the core requirements necessary to eliminate manual paper transfers and physical reconciliation."),
        ]),
        ("B. Performance Efficiency", [
            ("7", "System interfaces, data tables, and interactive dashboards load promptly without noticeable latency."),
            ("8", "Document routing status transitions update in real time across departmental monitors upon completion of procedural actions."),
            ("9", "Property index search queries (PIN, owner name, ARP number) return matching parcel records within three seconds."),
            ("10", "End-to-end transaction duration (e.g., Transfer of Assessment) is noticeably shorter compared to legacy manual workflows."),
            ("11", "System responsiveness remains consistent and stable when multiple municipal staff access the platform concurrently."),
        ]),
        ("C. Usability", [
            ("12", "User interface layouts and visual hierarchies are clear, structured, and straightforward to navigate."),
            ("13", "Frontline staff can comprehend and master primary transactional workflows with minimal technical training."),
            ("14", "Routine operational tasks (record intake, validation, clearance issuance) can be accomplished within a few user actions."),
            ("15", "The real-time document tracking dashboard transparently displays current document location, queue status, and assigned personnel."),
            ("16", "System feedback, input validations, and error notifications provide actionable and understandable instructions to the user."),
            ("17", "The software substantially simplifies inter-office coordination and eliminates tedious manual verification handoffs."),
        ]),
        ("D. Security", [
            ("18", "The system enforces secure user authentication protocols and prevents unauthorized system entry."),
            ("19", "Role-Based Access Control (RBAC) restricts data views and transactional privileges strictly to authorized municipal roles."),
            ("20", "Automated session timeouts terminate inactive user sessions to prevent unauthorized terminal access."),
            ("21", "An unalterable audit trail accurately logs all document modifications, status updates, and supervisory approvals with timestamps."),
            ("22", "Citizen property records and assessment rolls are effectively protected in accordance with the Data Privacy Act (RA 10173)."),
        ]),
        ("E. Reliability", [
            ("23", "The web application functions stably without sudden runtime crashes, deadlocks, or unhandled system exceptions."),
            ("24", "Recorded property assessments, payment logs, and file attachments remain intact and uncorrupted following logout and re-authentication."),
            ("25", "Atomic database transactions guarantee that interrupted or failed actions do not result in corrupted, partial, or orphaned records."),
            ("26", "The system maintains continuous availability during standard municipal operating hours."),
            ("27", "The platform recovers gracefully from intermittent network disconnections without causing transactional data loss."),
        ]),
        ("F. Compatibility (Platform Interoperability)", [
            ("28", "The web application functions identically and consistently across major modern web browsers (Chrome, Edge, Firefox)."),
            ("29", "The system operates smoothly on standard municipal office desktop computers without requiring proprietary hardware upgrades."),
        ]),
    ]
    
    col_w = [22, 378, 28, 28, 28, 28, 28]
    
    for sec_title, items in iso_sections:
        t_rows = [
            [Paragraph(f"<b>{sec_title.upper()}</b>", styles['TableHeader']), "",
             Paragraph("<b>5</b>", styles['TableHeader']), Paragraph("<b>4</b>", styles['TableHeader']),
             Paragraph("<b>3</b>", styles['TableHeader']), Paragraph("<b>2</b>", styles['TableHeader']),
             Paragraph("<b>1</b>", styles['TableHeader'])]
        ]
        for num, text in items:
            t_rows.append([
                Paragraph(num, styles['TableCellCenter']),
                Paragraph(text, styles['TableCell']),
                Paragraph("[  ]", styles['TableCellCenter']),
                Paragraph("[  ]", styles['TableCellCenter']),
                Paragraph("[  ]", styles['TableCellCenter']),
                Paragraph("[  ]", styles['TableCellCenter']),
                Paragraph("[  ]", styles['TableCellCenter']),
            ])
        t_sec = Table(t_rows, colWidths=col_w)
        t_sec.setStyle(TableStyle([
            ('SPAN', (0,0), (1,0)),
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#7A1113")),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#7A1113")),
            ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#D0D5DD")),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ('LEFTPADDING', (0,0), (-1,-1), 3),
            ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ]))
        story.append(KeepTogether([t_sec]))
        story.append(Spacer(1, 4))
        
    story.append(KeepTogether([make_callout_box("", [
        "<b>QUALITATIVE FEEDBACK & USER ACCEPTANCE</b>",
        "<b>1. Which feature or capability provided the greatest operational benefit to your workflow?</b><br/>____________________________________________________________________________________________________________",
        "<b>2. What operational difficulties or technical bugs did you encounter during testing?</b><br/>____________________________________________________________________________________________________________",
        "<b>3. What modifications or additional features would you recommend for future versions?</b><br/>____________________________________________________________________________________________________________",
        "<b>4. Would you endorse adopting the proposed system in your office?</b>&nbsp;&nbsp;&nbsp;&nbsp;[  ] Yes&nbsp;&nbsp;&nbsp;&nbsp;[  ] No&nbsp;&nbsp;&nbsp;&nbsp;[  ] Conditional<br/>Reason: ___________________________________________________________________________________________________"
    ])]))
    story.append(Spacer(1, 4))
    
    story.append(make_callout_box("EVALUATOR VERIFICATION & SUBMISSION", [
        "I hereby certify that I have thoroughly evaluated the software features and that the ratings provided above reflect my genuine operational and technical evaluation of the platform.",
        "<br/>Evaluator Signature: ____________________________________&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Submission Date: ________________________",
        "Printed Name: __________________________________________&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Official Designation: ____________________"
    ]))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print("Step 05 generated successfully.")

if __name__ == "__main__":
    generate_step_01()
    generate_step_02()
    generate_step_03()
    generate_step_04()
    generate_step_05()
    print("ALL 5 TOOLS IN CHRONOLOGICAL ORDER GENERATED SUCCESSFULLY!")
