import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, PieChart, DoughnutChart, Reference

def create_erpt_workbook(output_path):
    wb = openpyxl.Workbook()
    wb.remove(wb.active)  # Remove default blank sheet

    # -------------------------------------------------------------
    # Typography & Styles
    # -------------------------------------------------------------
    font_main_title = Font(name="Arial", size=15, bold=True, color="1E3A8A")
    font_treasurer_title = Font(name="Arial", size=15, bold=True, color="065F46")
    font_subtitle = Font(name="Arial", size=9, italic=True, color="4B5563")
    font_section = Font(name="Arial", size=11, bold=True, color="1E3A8A")
    font_section_green = Font(name="Arial", size=11, bold=True, color="065F46")
    
    font_header_white = Font(name="Arial", size=9, bold=True, color="FFFFFF")
    font_bold = Font(name="Arial", size=9, bold=True, color="111827")
    font_regular = Font(name="Arial", size=9, color="1F2937")
    font_italic = Font(name="Arial", size=9, italic=True, color="6B7280")
    
    font_kpi_value_blue = Font(name="Arial", size=15, bold=True, color="1E3A8A")
    font_kpi_value_green = Font(name="Arial", size=15, bold=True, color="047857")
    font_kpi_value_amber = Font(name="Arial", size=15, bold=True, color="B45309")
    font_kpi_label = Font(name="Arial", size=8, bold=True, color="4B5563")

    fill_header_navy = PatternFill(start_color="1E3A8A", end_color="1E3A8A", fill_type="solid")
    fill_header_blue = PatternFill(start_color="2563EB", end_color="2563EB", fill_type="solid")
    fill_header_green = PatternFill(start_color="047857", end_color="047857", fill_type="solid")
    fill_header_emerald = PatternFill(start_color="065F46", end_color="065F46", fill_type="solid")
    fill_header_amber = PatternFill(start_color="D97706", end_color="D97706", fill_type="solid")

    fill_kpi_blue_bg = PatternFill(start_color="EFF6FF", end_color="EFF6FF", fill_type="solid")
    fill_kpi_green_bg = PatternFill(start_color="ECFDF5", end_color="ECFDF5", fill_type="solid")
    fill_kpi_amber_bg = PatternFill(start_color="FFFBEB", end_color="FFFBEB", fill_type="solid")
    fill_zebra = PatternFill(start_color="F9FAFB", end_color="F9FAFB", fill_type="solid")
    
    fill_badge_paid = PatternFill(start_color="D1FAE5", end_color="D1FAE5", fill_type="solid")
    font_badge_paid = Font(name="Arial", size=9, bold=True, color="065F46")
    
    fill_badge_unpaid = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
    font_badge_unpaid = Font(name="Arial", size=9, bold=True, color="92400E")

    fill_badge_error = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
    font_badge_error = Font(name="Arial", size=9, bold=True, color="991B1B")

    thin_border = Border(
        left=Side(style='thin', color='D1D5DB'),
        right=Side(style='thin', color='D1D5DB'),
        top=Side(style='thin', color='D1D5DB'),
        bottom=Side(style='thin', color='D1D5DB')
    )
    total_double_border = Border(
        left=Side(style='thin', color='D1D5DB'),
        right=Side(style='thin', color='D1D5DB'),
        top=Side(style='thin', color='D1D5DB'),
        bottom=Side(style='double', color='111827')
    )

    # =========================================================================
    # TAB 1: EXECUTIVE DASHBOARD
    # =========================================================================
    ws_dash = wb.create_sheet(title="Executive Dashboard")
    ws_dash.views.sheetView[0].showGridLines = True

    # Title Banner
    ws_dash["A1"] = "REAL PROPERTY ASSESSMENT & TAXATION (eRPT) EXECUTIVE DASHBOARD"
    ws_dash["A1"].font = font_main_title
    ws_dash["A2"] = "Inter-Office Synchronization & Revenue Intelligence System | Municipality of Pasacao, Camarines Sur"
    ws_dash["A2"].font = font_subtitle

    # KPI Metric Cards (Row 4 to 6)
    # Structure: (LeftCol, RightCol, Label, Formula, Format, BgFill, ValFont)
    dash_kpis = [
        ("A", "B", "REGISTERED PARCELS", "='Assesment Roll'!B12", "#,##0", fill_kpi_blue_bg, font_kpi_value_blue),
        ("C", "D", "TOTAL MARKET VALUATION", "='Assesment Roll'!H12", "₱#,##0.00", fill_kpi_blue_bg, font_kpi_value_blue),
        ("E", "F", "TOTAL ASSESSED VALUATION", "='Assesment Roll'!J12", "₱#,##0.00", fill_kpi_blue_bg, font_kpi_value_blue),
        ("G", "H", "ANNUAL TAX BILLED (DUE)", "='Assesment Roll'!M12", "₱#,##0.00", fill_kpi_blue_bg, font_kpi_value_blue),
        ("I", "J", "COLLECTIONS REALIZED (PAID)", "='Treasurer Collections'!D11", "₱#,##0.00", fill_kpi_green_bg, font_kpi_value_green),
        ("K", "L", "UNPAID DELINQUENCY TARGET", "=G5-I5", "₱#,##0.00", fill_kpi_amber_bg, font_kpi_value_amber),
        ("M", "N", "COLLECTION EFFICIENCY", "=I5/G5", "0.0%", fill_kpi_green_bg, font_kpi_value_green),
    ]

    for c_l, c_r, lbl, fmla, num_fmt, bg, vfont in dash_kpis:
        # Top Label Row
        ws_dash.merge_cells(f"{c_l}4:{c_r}4")
        lbl_cell = ws_dash[f"{c_l}4"]
        lbl_cell.value = lbl
        lbl_cell.font = font_kpi_label
        lbl_cell.alignment = Alignment(horizontal="center", vertical="center")
        lbl_cell.fill = bg
        
        # Bottom Value Row
        ws_dash.merge_cells(f"{c_l}5:{c_r}5")
        val_cell = ws_dash[f"{c_l}5"]
        val_cell.value = fmla
        val_cell.font = vfont
        val_cell.alignment = Alignment(horizontal="center", vertical="center")
        val_cell.fill = bg
        val_cell.number_format = num_fmt

        # Borders
        c_l_idx = ord(c_l) - 64
        c_r_idx = ord(c_r) - 64
        for r in range(4, 6):
            for c in range(c_l_idx, c_r_idx + 1):
                ws_dash.cell(row=r, column=c).border = thin_border

    # Table 1: Revenue Collection Status: Paid vs. Unpaid (Row 8 to 12)
    ws_dash["A8"] = "1. REVENUE REALIZATION: PAID VS. UNPAID TAX PERFORMANCE"
    ws_dash["A8"].font = font_section

    t1_headers = ["Payment Category", "Parcels", "Total Tax Billed", "Actual Collected", "Unpaid Balance", "Collection %"]
    for c_idx, h in enumerate(t1_headers, start=1):
        cell = ws_dash.cell(row=9, column=c_idx, value=h)
        cell.font = font_header_white
        cell.fill = fill_header_navy
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = thin_border

    t1_rows = [
        ("Settled / Paid Accounts", '=COUNTIF(\'Assesment Roll\'!$N$3:$N$10, "Paid")', '=SUMIF(\'Assesment Roll\'!$N$3:$N$10, "Paid", \'Assesment Roll\'!$M$3:$M$10)', "='Treasurer Collections'!D11", "=C10-D10", "=D10/C10"),
        ("Unpaid / Delinquent Accounts", '=COUNTIF(\'Assesment Roll\'!$N$3:$N$10, "Unpaid")', '=SUMIF(\'Assesment Roll\'!$N$3:$N$10, "Unpaid", \'Assesment Roll\'!$M$3:$M$10)', 0, "=C11-D11", "=D11/C11"),
    ]

    for idx, (cat, cnt, billed, coll, unp, pct) in enumerate(t1_rows, start=10):
        ws_dash.cell(row=idx, column=1, value=cat).font = font_bold
        ws_dash.cell(row=idx, column=2, value=cnt).number_format = "#,##0"
        ws_dash.cell(row=idx, column=3, value=billed).number_format = "₱#,##0.00"
        ws_dash.cell(row=idx, column=4, value=coll).number_format = "₱#,##0.00"
        ws_dash.cell(row=idx, column=5, value=unp).number_format = "₱#,##0.00"
        ws_dash.cell(row=idx, column=6, value=pct).number_format = "0.0%"
        for c in range(1, 7):
            ws_dash.cell(row=idx, column=c).border = thin_border
            if idx == 10:
                ws_dash.cell(row=idx, column=c).fill = fill_badge_paid
            else:
                ws_dash.cell(row=idx, column=c).fill = fill_badge_unpaid

    # Table 1 Totals
    ws_dash.cell(row=12, column=1, value="Total Municipal Assessment").font = font_bold
    ws_dash.cell(row=12, column=2, value="=SUM(B10:B11)").number_format = "#,##0"
    ws_dash.cell(row=12, column=3, value="=SUM(C10:C11)").number_format = "₱#,##0.00"
    ws_dash.cell(row=12, column=4, value="=SUM(D10:D11)").number_format = "₱#,##0.00"
    ws_dash.cell(row=12, column=5, value="=SUM(E10:E11)").number_format = "₱#,##0.00"
    ws_dash.cell(row=12, column=6, value="=D12/C12").number_format = "0.0%"
    for c in range(1, 7):
        cell = ws_dash.cell(row=12, column=c)
        cell.font = font_bold
        cell.border = total_double_border

    # Table 2: Property Classification Breakdown (Row 14 to 19)
    ws_dash["A14"] = "2. VALUATION & TAX YIELD BY PROPERTY CLASSIFICATION"
    ws_dash["A14"].font = font_section

    t2_headers = ["Classification", "Parcels", "Total Market Value", "Total Assessed Value", "Tax Collectible", "Share (%)"]
    for c_idx, h in enumerate(t2_headers, start=1):
        cell = ws_dash.cell(row=15, column=c_idx, value=h)
        cell.font = font_header_white
        cell.fill = fill_header_blue
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = thin_border

    prop_classes = [("Residential", 16), ("Agricultural", 17), ("Commercial", 18)]
    for cl_name, r_idx in prop_classes:
        ws_dash.cell(row=r_idx, column=1, value=cl_name).font = font_bold
        ws_dash.cell(row=r_idx, column=2, value=f"=COUNTIF('Assesment Roll'!$E$3:$E$10, A{r_idx})").number_format = "#,##0"
        ws_dash.cell(row=r_idx, column=3, value=f"=SUMIF('Assesment Roll'!$E$3:$E$10, A{r_idx}, 'Assesment Roll'!$H$3:$H$10)").number_format = "₱#,##0.00"
        ws_dash.cell(row=r_idx, column=4, value=f"=SUMIF('Assesment Roll'!$E$3:$E$10, A{r_idx}, 'Assesment Roll'!$J$3:$J$10)").number_format = "₱#,##0.00"
        ws_dash.cell(row=r_idx, column=5, value=f"=SUMIF('Assesment Roll'!$E$3:$E$10, A{r_idx}, 'Assesment Roll'!$M$3:$M$10)").number_format = "₱#,##0.00"
        ws_dash.cell(row=r_idx, column=6, value=f"=E{r_idx}/$E$19").number_format = "0.0%"
        for c in range(1, 7):
            cell = ws_dash.cell(row=r_idx, column=c)
            cell.font = font_regular if c > 1 else font_bold
            cell.border = thin_border
            if r_idx % 2 == 1:
                cell.fill = fill_zebra

    ws_dash.cell(row=19, column=1, value="Total Municipal Assessment").font = font_bold
    ws_dash.cell(row=19, column=2, value="=SUM(B16:B18)").number_format = "#,##0"
    ws_dash.cell(row=19, column=3, value="=SUM(C16:C18)").number_format = "₱#,##0.00"
    ws_dash.cell(row=19, column=4, value="=SUM(D16:D18)").number_format = "₱#,##0.00"
    ws_dash.cell(row=19, column=5, value="=SUM(E16:E18)").number_format = "₱#,##0.00"
    ws_dash.cell(row=19, column=6, value="=SUM(F16:F18)").number_format = "0.0%"
    for c in range(1, 7):
        cell = ws_dash.cell(row=19, column=c)
        cell.font = font_bold
        cell.border = total_double_border

    # Table 3: Barangay Assessment & Collection Summary (Row 21 to 30)
    ws_dash["A21"] = "3. GEOGRAPHIC PERFORMANCE: BARANGAY TAX MATRIX"
    ws_dash["A21"].font = font_section

    t3_headers = ["Barangay", "Parcels", "Total Assessed Value", "Tax Due (Billed)", "Tax Collected", "Status"]
    for c_idx, h in enumerate(t3_headers, start=1):
        cell = ws_dash.cell(row=22, column=c_idx, value=h)
        cell.font = font_header_white
        cell.fill = fill_header_navy
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = thin_border

    brgys = [
        ("Balogo", 23), ("Caranan", 24), ("Dalupaon", 25), ("Odicon", 26),
        ("Tinalmud", 27), ("Macad", 28), ("Cuco", 29), ("Itulan", 30)
    ]
    for b_name, r_idx in brgys:
        ws_dash.cell(row=r_idx, column=1, value=b_name).font = font_bold
        ws_dash.cell(row=r_idx, column=2, value=f"=COUNTIF('Assesment Roll'!$D$3:$D$10, A{r_idx})").number_format = "#,##0"
        ws_dash.cell(row=r_idx, column=3, value=f"=SUMIF('Assesment Roll'!$D$3:$D$10, A{r_idx}, 'Assesment Roll'!$J$3:$J$10)").number_format = "₱#,##0.00"
        ws_dash.cell(row=r_idx, column=4, value=f"=SUMIF('Assesment Roll'!$D$3:$D$10, A{r_idx}, 'Assesment Roll'!$M$3:$M$10)").number_format = "₱#,##0.00"
        ws_dash.cell(row=r_idx, column=5, value=f"=SUMIFS('Treasurer Collections'!$D$3:$D$7, 'Treasurer Collections'!$C$3:$C$7, VLOOKUP(A{r_idx}, 'Assesment Roll'!$D$3:$A$10, -3, FALSE))").number_format = "₱#,##0.00"
        # Status
        ws_dash.cell(row=r_idx, column=6, value=f'=IF(SUMIF(\'Assesment Roll\'!$D$3:$D$10, A{r_idx}, \'Assesment Roll\'!$N$3:$N$10)="Paid", "Fully Settled", "Delinquent / Pending")').font = font_italic
        for c in range(1, 7):
            cell = ws_dash.cell(row=r_idx, column=c)
            cell.font = font_regular if c != 1 else font_bold
            cell.border = thin_border
            if r_idx % 2 == 1:
                cell.fill = fill_zebra

    # Totals for Barangay Table
    ws_dash.cell(row=31, column=1, value="Total All Barangays").font = font_bold
    ws_dash.cell(row=31, column=2, value="=SUM(B23:B30)").number_format = "#,##0"
    ws_dash.cell(row=31, column=3, value="=SUM(C23:C30)").number_format = "₱#,##0.00"
    ws_dash.cell(row=31, column=4, value="=SUM(D23:D30)").number_format = "₱#,##0.00"
    ws_dash.cell(row=31, column=5, value="=SUM(E23:E30)").number_format = "₱#,##0.00"
    ws_dash.cell(row=31, column=6, value="8 Barangays").font = font_italic
    for c in range(1, 7):
        cell = ws_dash.cell(row=31, column=c)
        cell.font = font_bold
        cell.border = total_double_border

    # -------------------------------------------------------------
    # Executive Dashboard Charts
    # -------------------------------------------------------------
    # Chart D1: Paid vs. Unpaid Collections Share (Doughnut Chart)
    chart_d1 = DoughnutChart()
    chart_d1.title = "Municipal Target: Collections Realized vs. Unpaid Delinquency"
    chart_d1.style = 10
    data_d1 = Reference(ws_dash, min_col=4, min_row=9, max_row=11)
    cats_d1 = Reference(ws_dash, min_col=1, min_row=10, max_row=11)
    chart_d1.add_data(data_d1, titles_from_data=True)
    chart_d1.set_categories(cats_d1)
    chart_d1.width = 14
    chart_d1.height = 7.5
    ws_dash.add_chart(chart_d1, "H8")

    # Chart D2: Tax Collectible by Property Classification (Pie Chart)
    chart_d2 = PieChart()
    chart_d2.title = "Tax Collectible Share by Property Classification"
    chart_d2.style = 11
    data_d2 = Reference(ws_dash, min_col=5, min_row=15, max_row=18)
    cats_d2 = Reference(ws_dash, min_col=1, min_row=16, max_row=18)
    chart_d2.add_data(data_d2, titles_from_data=True)
    chart_d2.set_categories(cats_d2)
    chart_d2.width = 14
    chart_d2.height = 7.5
    ws_dash.add_chart(chart_d2, "N8")

    # Chart D3: Valuation Comparison: Market Value vs. Assessed Value (Bar Chart)
    chart_d3 = BarChart()
    chart_d3.type = "col"
    chart_d3.style = 10
    chart_d3.title = "Valuation Comparison: Market Value vs. Assessed Value"
    chart_d3.y_axis.title = "Valuation in PHP"
    chart_d3.x_axis.title = "Property Classification"
    data_d3 = Reference(ws_dash, min_col=3, min_row=15, max_col=4, max_row=18)
    cats_d3 = Reference(ws_dash, min_col=1, min_row=16, max_row=18)
    chart_d3.add_data(data_d3, titles_from_data=True)
    chart_d3.set_categories(cats_d3)
    chart_d3.width = 14
    chart_d3.height = 7.5
    ws_dash.add_chart(chart_d3, "H18")

    # Chart D4: Assessed Value by Barangay (Clustered Column Chart)
    chart_d4 = BarChart()
    chart_d4.type = "col"
    chart_d4.style = 13
    chart_d4.title = "Taxable Valuation Base (Assessed Value) by Barangay"
    chart_d4.y_axis.title = "Assessed Value in PHP"
    chart_d4.x_axis.title = "Barangay Jurisdiction"
    data_d4 = Reference(ws_dash, min_col=3, min_row=22, max_row=30)
    cats_d4 = Reference(ws_dash, min_col=1, min_row=23, max_row=30)
    chart_d4.add_data(data_d4, titles_from_data=True)
    chart_d4.set_categories(cats_d4)
    chart_d4.width = 14
    chart_d4.height = 7.5
    ws_dash.add_chart(chart_d4, "N18")

    # Adjust Column Widths for Dashboard
    for col in ws_dash.columns:
        col_letter = get_column_letter(col[0].column)
        max_len = max(len(str(cell.value or '')) for cell in col)
        ws_dash.column_dimensions[col_letter].width = max(max_len + 4, 13)

    # =========================================================================
    # TAB 2: ASSESMENT ROLL (Municipal Assessor's Office)
    # =========================================================================
    ws_ass = wb.create_sheet(title="Assesment Roll")
    ws_ass.views.sheetView[0].showGridLines = True

    ws_ass["A1"] = "MUNICIPAL ASSESSOR'S OFFICE - REAL PROPERTY ASSESSMENT ROLL (CY 2026)"
    ws_ass["A1"].font = font_main_title
    ws_ass["A2"] = "Official Register of Taxable Real Properties, Market Values, and Assessment Levels | Municipality of Pasacao"
    ws_ass["A2"].font = font_subtitle

    ass_headers = [
        "TD No.", "PIN", "Owner (Masked)", "Barangay", "Classification", 
        "Area (sqm)", "Unit Value (PHP/sqm)", "Market Value", 
        "Assessment Level", "Assessed Value", "Basic RPT (1%)", 
        "SEF (1%)", "Total Tax Due", "Payment Status", "OR No."
    ]

    for c_idx, h in enumerate(ass_headers, start=1):
        cell = ws_ass.cell(row=3, column=c_idx, value=h)
        cell.font = font_header_white
        cell.fill = fill_header_navy
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = thin_border

    raw_properties = [
        ("TD-26-0001", "041-01-001", "Dela Cruz, J.", "Balogo", "Residential", 250, 1200, "Paid", "7712301"),
        ("TD-26-0002", "041-02-014", "Santos, M.", "Caranan", "Agricultural", 12000, 85, "Unpaid", ""),
        ("TD-26-0003", "041-03-007", "Reyes, A.", "Dalupaon", "Commercial", 400, 2500, "Paid", "7712302"),
        ("TD-26-0004", "041-04-022", "Bautista, R.", "Odicon", "Residential", 180, 1200, "Paid", "7712303"),
        ("TD-26-0005", "041-05-003", "Garcia, L.", "Tinalmud", "Agricultural", 8500, 85, "Unpaid", ""),
        ("TD-26-0006", "041-06-011", "Mendoza, C.", "Macad", "Residential", 320, 1000, "Paid", "7712304"),
        ("TD-26-0007", "041-07-005", "Villanueva, P.", "Cuco", "Commercial", 150, 2500, "Unpaid", ""),
        ("TD-26-0008", "041-08-019", "Ramos, E.", "Itulan", "Agricultural", 15000, 85, "Paid", "7712305"),
    ]

    for idx, (td, pin, owner, brgy, cl, area, uv, p_stat, or_no) in enumerate(raw_properties, start=4):
        ws_ass.cell(row=idx, column=1, value=td)
        ws_ass.cell(row=idx, column=2, value=pin)
        ws_ass.cell(row=idx, column=3, value=owner)
        ws_ass.cell(row=idx, column=4, value=brgy)
        ws_ass.cell(row=idx, column=5, value=cl)
        ws_ass.cell(row=idx, column=6, value=area).number_format = "#,##0"
        ws_ass.cell(row=idx, column=7, value=uv).number_format = "₱#,##0.00"
        
        # Formulas
        ws_ass.cell(row=idx, column=8, value=f"=F{idx}*G{idx}").number_format = "₱#,##0.00"
        ws_ass.cell(row=idx, column=9, value=f'=IF(E{idx}="Residential",0.2,IF(E{idx}="Agricultural",0.4,IF(E{idx}="Commercial",0.5,0.2)))').number_format = "0.0%"
        ws_ass.cell(row=idx, column=10, value=f"=H{idx}*I{idx}").number_format = "₱#,##0.00"
        ws_ass.cell(row=idx, column=11, value=f"=J{idx}*0.01").number_format = "₱#,##0.00"
        ws_ass.cell(row=idx, column=12, value=f"=J{idx}*0.01").number_format = "₱#,##0.00"
        ws_ass.cell(row=idx, column=13, value=f"=K{idx}+L{idx}").number_format = "₱#,##0.00"
        
        # Status & OR
        stat_cell = ws_ass.cell(row=idx, column=14, value=p_stat)
        ws_ass.cell(row=idx, column=15, value=or_no)

        for c in range(1, 16):
            cell = ws_ass.cell(row=idx, column=c)
            cell.font = font_regular
            cell.border = thin_border
            if idx % 2 == 1:
                cell.fill = fill_zebra
        
        if p_stat == "Paid":
            stat_cell.fill = fill_badge_paid
            stat_cell.font = font_badge_paid
        else:
            stat_cell.fill = fill_badge_unpaid
            stat_cell.font = font_badge_unpaid

    # Total Row for Assessor
    tot_row_ass = 12
    ws_ass.cell(row=tot_row_ass, column=1, value="TOTAL MUNICIPAL ROLL").font = font_bold
    ws_ass.cell(row=tot_row_ass, column=2, value="=COUNTA(A4:A11)").number_format = "#,##0"
    ws_ass.cell(row=tot_row_ass, column=6, value="=SUM(F4:F11)").number_format = "#,##0"
    ws_ass.cell(row=tot_row_ass, column=8, value="=SUM(H4:H11)").number_format = "₱#,##0.00"
    ws_ass.cell(row=tot_row_ass, column=10, value="=SUM(J4:J11)").number_format = "₱#,##0.00"
    ws_ass.cell(row=tot_row_ass, column=11, value="=SUM(K4:K11)").number_format = "₱#,##0.00"
    ws_ass.cell(row=tot_row_ass, column=12, value="=SUM(L4:L11)").number_format = "₱#,##0.00"
    ws_ass.cell(row=tot_row_ass, column=13, value="=SUM(M4:M11)").number_format = "₱#,##0.00"

    for c in range(1, 16):
        cell = ws_ass.cell(row=tot_row_ass, column=c)
        cell.font = font_bold
        cell.border = total_double_border

    # Adjust Column Widths for Assesment Roll
    for col in ws_ass.columns:
        col_letter = get_column_letter(col[0].column)
        max_len = max(len(str(cell.value or '')) for cell in col)
        ws_ass.column_dimensions[col_letter].width = max(max_len + 3, 11)

    # =========================================================================
    # TAB 3: TREASURER COLLECTIONS (Municipal Treasurer's Office)
    # =========================================================================
    ws_tr = wb.create_sheet(title="Treasurer Collections")
    ws_tr.views.sheetView[0].showGridLines = True

    # Title Banner
    ws_tr["A1"] = "MUNICIPAL TREASURER'S OFFICE - REAL PROPERTY TAX COLLECTIONS (CY 2026)"
    ws_tr["A1"].font = font_treasurer_title
    ws_tr["A2"] = "Official Collection Register, Real-Time Cross-Department Synchronization & Reconciliation | Municipality of Pasacao"
    ws_tr["A2"].font = font_subtitle

    # KPI Summary Cards for Treasurer (Row 4 to 5)
    tr_kpis = [
        ("A", "B", "TOTAL RECEIPTS ISSUED", "=COUNTA(A10:A14)", "#,##0", fill_kpi_green_bg, font_kpi_value_green),
        ("C", "D", "TOTAL CASH COLLECTED", "=D15", "₱#,##0.00", fill_kpi_green_bg, font_kpi_value_green),
        ("E", "F", "TOTAL BILLED TAX (TARGET)", "='Assesment Roll'!M12", "₱#,##0.00", fill_kpi_blue_bg, font_kpi_value_blue),
        ("G", "H", "UNPAID DELINQUENCY TARGET", "=E5-C5", "₱#,##0.00", fill_kpi_amber_bg, font_kpi_value_amber),
        ("I", "J", "COLLECTION REALIZATION %", "=C5/E5", "0.0%", fill_kpi_green_bg, font_kpi_value_green),
        ("K", "L", "FULLY RECONCILED RECORDS", '=COUNTIF(G10:G14, "Fully Settled")', "#,##0", fill_kpi_green_bg, font_kpi_value_green),
    ]

    for c_l, c_r, lbl, fmla, num_fmt, bg, vfont in tr_kpis:
        ws_tr.merge_cells(f"{c_l}4:{c_r}4")
        lbl_cell = ws_tr[f"{c_l}4"]
        lbl_cell.value = lbl
        lbl_cell.font = font_kpi_label
        lbl_cell.alignment = Alignment(horizontal="center", vertical="center")
        lbl_cell.fill = bg

        ws_tr.merge_cells(f"{c_l}5:{c_r}5")
        val_cell = ws_tr[f"{c_l}5"]
        val_cell.value = fmla
        val_cell.font = vfont
        val_cell.alignment = Alignment(horizontal="center", vertical="center")
        val_cell.fill = bg
        val_cell.number_format = num_fmt

        c_l_idx = ord(c_l) - 64
        c_r_idx = ord(c_r) - 64
        for r in range(4, 6):
            for c in range(c_l_idx, c_r_idx + 1):
                ws_tr.cell(row=r, column=c).border = thin_border

    # Section 1: Main Collection Transactions Table (Row 8 to 15)
    ws_tr["A8"] = "1. TAX COLLECTION TRANSACTIONS & CROSS-OFFICE RECONCILIATION"
    ws_tr["A8"].font = font_section_green

    tr_headers = [
        "OR No.", "Date Paid", "TD No.", "Amount Paid", 
        "Tax Due (Assessor)", "Variance (PHP)", "Reconciliation Status", "Remarks"
    ]

    for c_idx, h in enumerate(tr_headers, start=1):
        cell = ws_tr.cell(row=9, column=c_idx, value=h)
        cell.font = font_header_white
        cell.fill = fill_header_emerald
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = thin_border

    treasurer_entries = [
        ("7712301", "2026-01-15", "TD-26-0001", 1200, "Full payment verified; zero variance"),
        ("7712302", "2026-01-20", "TD-26-0003", 10000, "Full payment verified; zero variance"),
        ("7712303", "2026-02-03", "TD-26-0004", 800, "Partial payment - underpaid balance of ₱64.00"),
        ("7712304", "2026-02-10", "TD-26-0006", 1280, "Full payment verified; zero variance"),
        ("7712305", "2026-03-02", "TD-26-0080", 10200, "TD No. typo (TD-26-0080 missing in Assessor Roll)"),
    ]

    for idx, (or_n, dt, td_n, amt, rem) in enumerate(treasurer_entries, start=10):
        ws_tr.cell(row=idx, column=1, value=or_n)
        ws_tr.cell(row=idx, column=2, value=dt)
        ws_tr.cell(row=idx, column=3, value=td_n)
        ws_tr.cell(row=idx, column=4, value=amt).number_format = "₱#,##0.00"

        # ROBUST FORMULAS
        # Col E: Lookup Total Tax Due from Assesment Roll
        ws_tr.cell(row=idx, column=5, value=f'=IFERROR(VLOOKUP(C{idx}, \'Assesment Roll\'!$A$4:$M$11, 13, FALSE), "RECORD NOT FOUND")')
        
        # Col F: Variance (Amount Paid - Tax Due)
        ws_tr.cell(row=idx, column=6, value=f'=IF(ISNUMBER(E{idx}), D{idx}-E{idx}, "N/A")')
        
        # Col G: Status
        status_cell = ws_tr.cell(row=idx, column=7, value=f'=IF(NOT(ISNUMBER(E{idx})), "Record Missing / Error", IF(F{idx}=0, "Fully Settled", IF(F{idx}<0, "Partial / Underpaid", "Overpaid")))')
        
        # Col H: Remarks
        ws_tr.cell(row=idx, column=8, value=rem)

        for c in range(1, 9):
            cell = ws_tr.cell(row=idx, column=c)
            cell.font = font_regular if c != 7 else font_bold
            cell.border = thin_border
            if idx % 2 == 1:
                cell.fill = fill_zebra

        # Cell specific formatting
        ws_tr.cell(row=idx, column=5).number_format = "₱#,##0.00"
        ws_tr.cell(row=idx, column=6).number_format = "₱#,##0.00"

        # Badge colors based on entry
        if "Full payment" in rem:
            status_cell.fill = fill_badge_paid
            status_cell.font = font_badge_paid
        elif "Partial payment" in rem:
            status_cell.fill = fill_badge_unpaid
            status_cell.font = font_badge_unpaid
        else:
            status_cell.fill = fill_badge_error
            status_cell.font = font_badge_error

    # Total Row for Treasurer Ledger
    ws_tr.cell(row=15, column=1, value="TOTAL REALIZED COLLECTIONS").font = font_bold
    ws_tr.cell(row=15, column=4, value="=SUM(D10:D14)").number_format = "₱#,##0.00"
    for c in range(1, 9):
        cell = ws_tr.cell(row=15, column=c)
        cell.font = font_bold
        cell.border = total_double_border

    # =========================================================================
    # TREASURER SUMMARY TABLES FOR CHARTS (Row 17 to 25)
    # =========================================================================
    ws_tr["A17"] = "2. TREASURER SUMMARY: PAID VS. UNPAID REAL PROPERTY TAX PERFORMANCE"
    ws_tr["A17"].font = font_section_green

    tr_sum_headers = ["Account Classification", "Parcels", "Total Amount Billed", "Actual Realized Collections", "Uncollected / Outstanding", "Realization %"]
    for c_idx, h in enumerate(tr_sum_headers, start=1):
        cell = ws_tr.cell(row=18, column=c_idx, value=h)
        cell.font = font_header_white
        cell.fill = fill_header_green
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = thin_border

    # Summary Row 19: Paid Parcels
    ws_tr.cell(row=19, column=1, value="Paid Real Property Accounts").font = font_bold
    ws_tr.cell(row=19, column=2, value='=COUNTIF(\'Assesment Roll\'!$N$4:$N$11, "Paid")').number_format = "#,##0"
    ws_tr.cell(row=19, column=3, value='=SUMIF(\'Assesment Roll\'!$N$4:$N$11, "Paid", \'Assesment Roll\'!$M$4:$M$11)').number_format = "₱#,##0.00"
    ws_tr.cell(row=19, column=4, value="=D15").number_format = "₱#,##0.00"
    ws_tr.cell(row=19, column=5, value="=C19-D19").number_format = "₱#,##0.00"
    ws_tr.cell(row=19, column=6, value="=D19/C19").number_format = "0.0%"

    # Summary Row 20: Unpaid Parcels
    ws_tr.cell(row=20, column=1, value="Unpaid / Delinquent Accounts").font = font_bold
    ws_tr.cell(row=20, column=2, value='=COUNTIF(\'Assesment Roll\'!$N$4:$N$11, "Unpaid")').number_format = "#,##0"
    ws_tr.cell(row=20, column=3, value='=SUMIF(\'Assesment Roll\'!$N$4:$N$11, "Unpaid", \'Assesment Roll\'!$M$4:$M$11)').number_format = "₱#,##0.00"
    ws_tr.cell(row=20, column=4, value=0).number_format = "₱#,##0.00"
    ws_tr.cell(row=20, column=5, value="=C20-D20").number_format = "₱#,##0.00"
    ws_tr.cell(row=20, column=6, value="=D20/C20").number_format = "0.0%"

    for r in range(19, 21):
        for c in range(1, 7):
            ws_tr.cell(row=r, column=c).border = thin_border
            if r == 19:
                ws_tr.cell(row=r, column=c).fill = fill_badge_paid
            else:
                ws_tr.cell(row=r, column=c).fill = fill_badge_unpaid

    # Summary Row 21: Total
    ws_tr.cell(row=21, column=1, value="Total Municipal Assessment Base").font = font_bold
    ws_tr.cell(row=21, column=2, value="=SUM(B19:B20)").number_format = "#,##0"
    ws_tr.cell(row=21, column=3, value="=SUM(C19:C20)").number_format = "₱#,##0.00"
    ws_tr.cell(row=21, column=4, value="=SUM(D19:D20)").number_format = "₱#,##0.00"
    ws_tr.cell(row=21, column=5, value="=SUM(E19:E20)").number_format = "₱#,##0.00"
    ws_tr.cell(row=21, column=6, value="=D21/C21").number_format = "0.0%"
    for c in range(1, 7):
        cell = ws_tr.cell(row=21, column=c)
        cell.font = font_bold
        cell.border = total_double_border

    # Section 3: Reconciliation Audit Status (Row 23 to 27)
    ws_tr["A23"] = "3. INTER-OFFICE DATA RECONCILIATION BREAKDOWN"
    ws_tr["A23"].font = font_section_green

    recon_headers = ["Synchronization Audit Status", "Receipts (Count)", "Cash Realized (PHP)", "Inter-Office Action"]
    for c_idx, h in enumerate(recon_headers, start=1):
        cell = ws_tr.cell(row=24, column=c_idx, value=h)
        cell.font = font_header_white
        cell.fill = fill_header_emerald
        cell.alignment = Alignment(horizontal="center", vertical="center")
        cell.border = thin_border

    recon_data = [
        ("Fully Reconciled & Settled", '=COUNTIF(G10:G14, "Fully Settled")', '=SUMIF(G10:G14, "Fully Settled", D10:D14)', "Zero variance; tax ledger synchronized with Assessor roll"),
        ("Partial Payment / Pending Bal.", '=COUNTIF(G10:G14, "Partial / Underpaid")', '=SUMIF(G10:G14, "Partial / Underpaid", D10:D14)', "Collectible balance remaining; billing notice to be generated"),
        ("Record Mismatch / Typo Error", '=COUNTIF(G10:G14, "Record Missing / Error")', '=SUMIF(G10:G14, "Record Missing / Error", D10:D14)', "TD No. not found in Assessor roll; manual verification needed"),
    ]

    for idx, (st, cnt, csh, act) in enumerate(recon_data, start=25):
        ws_tr.cell(row=idx, column=1, value=st).font = font_bold
        ws_tr.cell(row=idx, column=2, value=cnt).number_format = "#,##0"
        ws_tr.cell(row=idx, column=3, value=csh).number_format = "₱#,##0.00"
        ws_tr.cell(row=idx, column=4, value=act).font = font_italic
        for c in range(1, 5):
            ws_tr.cell(row=idx, column=c).border = thin_border

    # -------------------------------------------------------------
    # TREASURER TAB CHARTS (USER SPECIFIC REQUEST)
    # -------------------------------------------------------------
    # Chart T1: Paid vs. Unpaid Revenue Realization (Doughnut Chart)
    chart_t1 = DoughnutChart()
    chart_t1.title = "Treasurer Tax Yield: Paid Collections vs. Unpaid Balance"
    chart_t1.style = 13
    data_t1 = Reference(ws_tr, min_col=4, min_row=18, max_row=20)
    cats_t1 = Reference(ws_tr, min_col=1, min_row=19, max_row=20)
    chart_t1.add_data(data_t1, titles_from_data=True)
    chart_t1.set_categories(cats_t1)
    chart_t1.width = 14
    chart_t1.height = 7.5
    ws_tr.add_chart(chart_t1, "J8")

    # Chart T2: Paid vs. Unpaid Parcels (Bar Chart)
    chart_t2 = BarChart()
    chart_t2.type = "col"
    chart_t2.style = 10
    chart_t2.title = "Real Property Accounts: Paid vs. Unpaid Distribution"
    chart_t2.y_axis.title = "Number of Property Parcels"
    chart_t2.x_axis.title = "Payment Status"
    data_t2 = Reference(ws_tr, min_col=2, min_row=18, max_row=20)
    cats_t2 = Reference(ws_tr, min_col=1, min_row=19, max_row=20)
    chart_t2.add_data(data_t2, titles_from_data=True)
    chart_t2.set_categories(cats_t2)
    chart_t2.width = 14
    chart_t2.height = 7.5
    ws_tr.add_chart(chart_t2, "J18")

    # Chart T3: Individual Transactions: Amount Paid vs. Billed Tax Due (Clustered Column Chart)
    chart_t3 = BarChart()
    chart_t3.type = "col"
    chart_t3.style = 11
    chart_t3.title = "Transaction Audit: Amount Paid vs. Assessor Tax Due"
    chart_t3.y_axis.title = "Amount in PHP"
    chart_t3.x_axis.title = "Tax Declaration Number (TD No.)"
    data_t3 = Reference(ws_tr, min_col=4, min_row=9, max_col=5, max_row=14)
    cats_t3 = Reference(ws_tr, min_col=3, min_row=10, max_row=14)
    chart_t3.add_data(data_t3, titles_from_data=True)
    chart_t3.set_categories(cats_t3)
    chart_t3.width = 16
    chart_t3.height = 7.5
    ws_tr.add_chart(chart_t3, "A29")

    # Adjust Column Widths for Treasurer Collections
    for col in ws_tr.columns:
        col_letter = get_column_letter(col[0].column)
        max_len = max(len(str(cell.value or '')) for cell in col)
        ws_tr.column_dimensions[col_letter].width = max(max_len + 4, 14)

    # Save final workbook
    wb.save(output_path)
    print(f"Professional eRPT Workbook successfully written to: {output_path}")

if __name__ == "__main__":
    create_erpt_workbook("/Users/student/Downloads/RPATIS-main/HCI/Case Study (ISO 9241-210)/Professional_eRPT_Spreadsheet_System.xlsx")
