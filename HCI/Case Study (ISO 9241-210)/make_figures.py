"""Draws the two appendix diagrams for the Google Sheets ISO 9241-210 case study."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "images")

INK = "#1f2937"
GREEN = "#0f9d58"      # Google Sheets green
GREEN_L = "#e6f4ea"
RED = "#c5221f"
RED_L = "#fce8e6"
BLUE = "#1a56db"
BLUE_L = "#e8f0fe"
GREY_L = "#f3f4f6"


def box(ax, x, y, w, h, text, fc, ec, fs=9.5, bold=False, tc=INK):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012,rounding_size=0.018",
                                fc=fc, ec=ec, lw=1.4))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=tc,
            fontweight="bold" if bold else "normal", wrap=True, linespacing=1.25)


def arrow(ax, x1, y1, x2, y2, color=INK, style="-|>", ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=13,
                                 color=color, lw=1.4, linestyle=ls))


def workflow_comparison():
    fig, ax = plt.subplots(figsize=(13, 8.2), dpi=200)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.text(0.5, 0.975, "Workflow Comparison: Google Sheets-Based RPT Records vs. the Proposed System",
            ha="center", va="top", fontsize=14, fontweight="bold", color=INK)

    # ---- Left panel: Google Sheets ----
    ax.add_patch(FancyBboxPatch((0.02, 0.04), 0.46, 0.87, boxstyle="round,pad=0.005,rounding_size=0.02",
                                fc=GREY_L, ec="#9ca3af", lw=1))
    ax.text(0.25, 0.885, "CURRENT: Google Sheets as RPT Ledger", ha="center", fontsize=11.5,
            fontweight="bold", color=GREEN)
    steps = [
        "1  Assessor clerk encodes tax declaration data\nin the Assessment_Roll sheet",
        "2  Formulas compute Market Value, Assessed Value,\nBasic RPT (1%), SEF (1%), Total Tax Due",
        "3  File shared by link or downloaded as .xlsx\nand sent to the Treasurer's Office",
        "4  Cashier types the TD No. in a separate\nCollections sheet; VLOOKUP pulls the tax due",
        "5  Typos / stale values return NOT FOUND or #VALUE!\nresolved by phone call or walk-over",
        "6  Paper endorsement to Provincial Assessor (Pili)\nstatus kept as free text, not tracked",
    ]
    pains = [None, "hard-coded rates\nin formulas", "copies drift\napart", "exact text match\nrequired",
             "manual cross-\nchecking", "7-14 day wait,\nno visibility"]
    y = 0.775
    for i, s in enumerate(steps):
        bad = i >= 2
        box(ax, 0.045, y, 0.30, 0.088, s, RED_L if bad else GREEN_L, RED if bad else GREEN, fs=8.6)
        if pains[i]:
            ax.text(0.405, y + 0.044, pains[i], ha="center", va="center", fontsize=7.8, color=RED,
                    style="italic")
            arrow(ax, 0.365, y + 0.044, 0.35, y + 0.044, color=RED, style="-")
        if i < len(steps) - 1:
            arrow(ax, 0.195, y, 0.195, y - 0.034)
        y -= 0.122

    # ---- Right panel: Proposed system ----
    ax.add_patch(FancyBboxPatch((0.52, 0.04), 0.46, 0.87, boxstyle="round,pad=0.005,rounding_size=0.02",
                                fc="#f8fafc", ec="#9ca3af", lw=1))
    ax.text(0.75, 0.885, "PROPOSED SYSTEM: Three-Tier Web Platform", ha="center",
            fontsize=11.5, fontweight="bold", color=BLUE)
    tiers = [
        ("TIER 1  Presentation (Web Browser)",
         "Assessor evaluation screens  |  Treasurer payment\nvalidation view  |  Document tracking monitor"),
        ("TIER 2  Application / Business Logic",
         "Assessment request routing  |  Rule-based tax computation\nTax payment synchronization  |  RBAC + audit log"),
        ("TIER 3  Data",
         "Centralized relational database: synchronized property\nrecords, assessment statuses, transaction logs"),
    ]
    y = 0.70
    for i, (t, d) in enumerate(tiers):
        box(ax, 0.55, y, 0.40, 0.15, "", BLUE_L, BLUE)
        ax.text(0.75, y + 0.115, t, ha="center", fontsize=10, fontweight="bold", color=BLUE)
        ax.text(0.75, y + 0.055, d, ha="center", va="center", fontsize=8.6, color=INK, linespacing=1.3)
        if i < 2:
            arrow(ax, 0.73, y, 0.73, y - 0.045, color=BLUE, style="<|-|>")
        y -= 0.20
    outcomes = ("One shared record per TD No. (no re-typing)\n"
                "Timestamped status at each routing step\n"
                "Assessor > Treasurer > Provincial Capitol (Pili)\n"
                "Rates kept in one table; computed fields locked")
    box(ax, 0.55, 0.07, 0.40, 0.15, outcomes, GREEN_L, GREEN, fs=8.6)
    ax.text(0.75, 0.235, "Expected outcomes", ha="center", fontsize=9.5, fontweight="bold", color=GREEN)

    fig.text(0.5, 0.06, "Authors' synthesis, 2026. Data shown in the Google Sheets workflow is mock data (RA 10173).",
             ha="center", fontsize=8, color="#6b7280", style="italic")
    fig.savefig(os.path.join(OUT, "gsheets_workflow_comparison.png"), bbox_inches="tight", facecolor="white")
    plt.close(fig)


def hcd_cycle():
    fig, ax = plt.subplots(figsize=(13, 8.6), dpi=200)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    ax.text(0.5, 0.98, "ISO 9241-210 Human-Centred Design Cycle: Google Sheets vs. the Proposed System",
            ha="center", va="top", fontsize=14, fontweight="bold", color=INK)

    # Cycle (left)
    box(ax, 0.10, 0.83, 0.26, 0.07, "Plan the human-centred design process (Cl. 5)", GREY_L, INK, fs=9, bold=True)
    nodes = {
        "ctx": (0.03, 0.58, "6.2  Understand and specify\nthe context of use"),
        "req": (0.25, 0.58, "6.3  Specify the\nuser requirements"),
        "des": (0.25, 0.33, "6.4  Produce design solutions\nto meet requirements"),
        "eva": (0.03, 0.33, "6.5  Evaluate the designs\nagainst requirements"),
    }
    for k, (x, y, t) in nodes.items():
        box(ax, x, y, 0.18, 0.10, t, BLUE_L, BLUE, fs=8.6)
    arrow(ax, 0.23, 0.83, 0.12, 0.685)
    arrow(ax, 0.21, 0.63, 0.25, 0.63, color=BLUE)
    arrow(ax, 0.34, 0.58, 0.34, 0.435, color=BLUE)
    arrow(ax, 0.25, 0.38, 0.21, 0.38, color=BLUE)
    arrow(ax, 0.12, 0.435, 0.12, 0.58, color=BLUE)
    ax.text(0.04, 0.505, "iterate", fontsize=8.5, color=BLUE, style="italic", rotation=90, va="center")
    box(ax, 0.06, 0.12, 0.30, 0.09, "Designed solution meets user requirements", GREEN_L, GREEN, fs=9, bold=True)
    arrow(ax, 0.12, 0.33, 0.15, 0.215, color=GREEN)

    # Table (right)
    rows = [
        ("Clause", "Google Sheets\n(general product)", "Sheets used as\nLGU RPT ledger", "Proposed system\n(Agile sprints)"),
        ("5  Planning", "Staged releases;\npublic Material Design", "No plan for RPT\nrisks or roles", "HCD tasks in every\n2-week sprint"),
        ("6.2  Context", "Desktop, mobile,\noffline documented", "Brownouts, 1949\nledgers ignored", "Field interviews in\nPasacao & Canaman"),
        ("6.3  User\nRequirements", "WCAG 2.1, Material\nguidelines", "No task-time or\nerror targets", "Latency and\nreconciliation targets"),
        ("6.4  Design", "Familiar grid, formula\nbar, dropdowns", "Hidden formulas; no\nworkflow states", "Labelled forms, routing,\nstatus tracking"),
        ("6.5  Evaluation", "ACRs, early-access\nfeedback", "No testing with\nmunicipal clerks", "ISO/IEC 25010 survey\nwith LGU staff"),
    ]
    x0, y0, cw, rh = 0.45, 0.78, [0.12, 0.14, 0.14, 0.14], 0.11
    colors = [None, GREEN_L, RED_L, BLUE_L]
    edges = [INK, GREEN, RED, BLUE]
    for r, row in enumerate(rows):
        x = x0
        for c, cell in enumerate(row):
            fc = "#e5e7eb" if r == 0 else (GREY_L if c == 0 else colors[c])
            ec = INK if (r == 0 or c == 0) else edges[c]
            ax.add_patch(plt.Rectangle((x, y0 - r * rh), cw[c], rh, fc=fc, ec=ec, lw=0.9))
            ax.text(x + cw[c] / 2, y0 - r * rh + rh / 2, cell, ha="center", va="center",
                    fontsize=7.9 if r else 8.4, fontweight="bold" if (r == 0 or c == 0) else "normal",
                    color=INK, linespacing=1.25)
            x += cw[c]
    fig.text(0.5, 0.08, "Authors' synthesis, 2026, based on ISO 9241-210:2010 Clause 4-6 and Annex B Table B.1.",
             ha="center", fontsize=8, color="#6b7280", style="italic")
    fig.savefig(os.path.join(OUT, "gsheets_iso_hcd_cycle.png"), bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    workflow_comparison()
    hcd_cycle()
    print("figures written to", OUT)
