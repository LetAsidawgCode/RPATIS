# Google Sheets Screenshot Guide (Case Study ISO 9241-210)

This takes about 10 minutes. The build script puts each screenshot into the case study automatically when the file name matches.

## 1. Set up the mock sheet

1. Open <https://sheets.new> while signed in to any Google account.
2. Rename the file to: `Pasacao RPT Assessment Roll 2026 (Mock Data)`.
3. Double-click the `Sheet1` tab and rename it to **`Assessment_Roll`** (exact spelling, because the Treasurer formulas point to this name).
4. Open `Assessment_Roll.tsv` (in this folder) in TextEdit. Press Cmd+A, then Cmd+C. Click cell **A1** in Sheets and press Cmd+V. The formulas calculate automatically.
5. Click **+** at the bottom-left to add a sheet. Rename it **`Treasurer_Collections`**. Paste `Treasurer_Collections.tsv` into A1 the same way.
6. Formatting, on `Assessment_Roll`:
   - Row 1: bold, light-blue fill. Then **View > Freeze > 1 row**.
   - Columns G, H, J, K, L, M: **Format > Number > Currency**.
   - Column I: **Format > Number > Percent**.
   - Select E2:E9. Go to **Data > Data validation > Add rule**, choose **Dropdown**, and add the options `Residential`, `Agricultural`, `Commercial`. Click **Done**.
   - Select columns A:O, right-click a column header, choose **Resize columns > Fit to data**.
7. On `Treasurer_Collections`: make row 1 bold with a light fill, then fit the columns. Row 6 shows **NOT FOUND** in column E and **#VALUE!** in column F. This is intentional, because it is evidence for the case study.

Expected Total Tax Due (column M): 1,200 / 8,160 / 10,000 / 864 / 5,780 / 1,280 / 3,750 / 10,200.

## 2. Take the screenshots

Use a wide browser window. Capture the whole Sheets window with **Cmd+Shift+4**, then press **Space**, then click the window. Save each file to:

`HCI/Case Study (ISO 9241-210)/images/gsheets/`

| File name | What must be on screen |
|---|---|
| `S1_grid.png` | `Assessment_Roll` tab with A1 selected. The menu bar, toolbar, formula bar, all 9 rows, and the sheet tabs are visible. |
| `S2_formula_assessed_value.png` | Cell **J3** selected. The formula bar shows `=H3*I3`. |
| `S3_formula_assessment_level.png` | Cell **I4** selected. The formula bar shows the `=IF(...)` assessment level formula. |
| `S4_data_validation.png` | The **Data validation** side panel is open for E2:E9, or the dropdown list on cell E3 is open. |
| `S5_vlookup_treasurer.png` | `Treasurer_Collections` tab with cell **E2** selected so the VLOOKUP shows in the formula bar. Row 6 shows NOT FOUND / #VALUE!. If you hover over the #VALUE! cell, the error tooltip shows. Capturing it is a bonus. |
| `S6_share_dialog.png` | The **Share** dialog (top-right button) with the General access section visible. Do not change anything. |
| `S7_version_history.png` | **File > Version history > See version history** with the panel open. |

## 3. Rebuild the document

When all the files are in `images/gsheets/`, ask the assistant to "re-run the case study build". Or run this yourself:

```
python3 "HCI/Case Study (ISO 9241-210)/build_case_study.py"
```

Any screenshot that is missing stays as a grey labelled slot.
