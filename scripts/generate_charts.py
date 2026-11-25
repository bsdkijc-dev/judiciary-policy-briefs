#!/usr/bin/env python3
"""
Generate publication-quality charts for PB-JUD-2026-001.
Outputs PNGs to assets/PB-JUD-2026-001/ and docs/assets/images/.
"""
from pathlib import Path
import shutil
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "PB-JUD-2026-001"
ASSETS_DIR = BASE_DIR / "assets" / "PB-JUD-2026-001"
DOCS_IMG_DIR = BASE_DIR / "docs" / "assets" / "images"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)
DOCS_IMG_DIR.mkdir(parents=True, exist_ok=True)

NAVY = "#1e3a5f"
BLUE = "#2b6cb0"
TEAL = "#0f766e"
AMBER = "#d97706"
SLATE = "#475569"

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["font.size"] = 10
plt.rcParams["axes.edgecolor"] = "#cbd5e1"
plt.rcParams["axes.linewidth"] = 0.8

def main():
    df = pd.read_csv(DATA_DIR / "judicial_caseload.csv")
    ma = df[df["court_id"] == "MA-RI"].sort_values("report_year").copy()
    years = ma["report_year"].values

    # Chart 1: caseload-trend.png
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.2, 6.2), gridspec_kw={"height_ratios": [2.2, 1]}, sharex=True, dpi=220)
    fig.patch.set_facecolor("white")

    ax1.plot(years, ma["total_caseload"], marker="o", color=NAVY, linewidth=2.2, label="Total Caseload (Beban Perkara)")
    ax1.plot(years, ma["resolved_cases"], marker="s", color=TEAL, linewidth=2.0, linestyle="--", label="Resolved Cases (Perkara Putus)")
    in_mask = ma["incoming_cases"].notna()
    ax1.plot(years[in_mask], ma.loc[in_mask, "incoming_cases"], marker="^", color=BLUE, linewidth=1.6, linestyle=":", label="Incoming Cases (Perkara Masuk, 2016-2025)")

    ax1.annotate("38,148\ncaseload", xy=(2025, 38148), xytext=(2022.2, 34500),
                 arrowprops=dict(arrowstyle="->", color=NAVY, lw=1), fontsize=8.5, fontweight="bold", color=NAVY)
    ax1.annotate("18,402\ncaseload", xy=(2015, 18402), xytext=(2015.3, 22800),
                 arrowprops=dict(arrowstyle="->", color=NAVY, lw=1), fontsize=8.5, color=NAVY)

    ax1.set_ylabel("Number of Cases", fontweight="bold", color=SLATE)
    ax1.set_ylim(12000, 42000)
    ax1.yaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
    ax1.grid(axis="y", linestyle="--", alpha=0.4)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="#e2e8f0", fontsize=8.5)
    ax1.set_title("Supreme Court of Indonesia (MA-RI): Caseload & Pending Cases (2015–2025)",
                  fontsize=11, fontweight="bold", color=NAVY, pad=10, loc="left")

    bars = ax2.bar(years, ma["pending_cases"], color=AMBER, width=0.58, alpha=0.88, label="Year-End Pending Cases (Sisa Perkara)")
    for b, val in zip(bars, ma["pending_cases"]):
        ax2.text(b.get_x() + b.get_width()/2, val + 120, f"{int(val):,}", ha="center", va="bottom", fontsize=8, color=SLATE, fontweight="bold")
    ax2.set_ylabel("Pending Cases", fontweight="bold", color=SLATE)
    ax2.set_ylim(0, 4700)
    ax2.yaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
    ax2.grid(axis="y", linestyle="--", alpha=0.4)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.set_xticks(years)
    ax2.set_xlabel("Reporting Year (2018 incoming/resolved derived from official YoY %; 2015 incoming not verified)", fontsize=8.5, color=SLATE)

    fig.text(0.01, 0.005, "Source: Mahkamah Agung RI Annual Reports & Kepaniteraan Official Releases (2015-2025). Unit: Cases.", fontsize=8, color="#64748b")
    plt.tight_layout(rect=[0, 0.025, 1, 1])
    fig.savefig(ASSETS_DIR / "caseload-trend.png", dpi=220)
    plt.close(fig)

    # Chart 2: clearance-trend.png
    fig, ax = plt.subplots(figsize=(8.2, 4.4), dpi=220)
    fig.patch.set_facecolor("white")
    ax.plot(years, ma["deciding_productivity_rate"], marker="o", color=NAVY, linewidth=2.4, label="Deciding Productivity Rate (Resolved / Total Caseload, %)")
    std_mask = ma["standard_clearance_rate"].notna()
    ax.plot(years[std_mask], ma.loc[std_mask, "standard_clearance_rate"], marker="D", color=TEAL, linewidth=2.0, linestyle="--", label="Standard Clearance Rate (Resolved / Incoming, %)")
    ax.axhline(100.0, color="#94a3b8", linestyle="-.", linewidth=1.1, label="100% Clearance Parity Benchmark")
    ax.axhline(90.0, color=AMBER, linestyle=":", linewidth=1.2, label="MA IKU Target (90% since 2022; previously 70%)")
    ax.annotate("99.54%\n(2025)", xy=(2025, 99.54), xytext=(2023.7, 94.5),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=1), fontsize=8.5, fontweight="bold", color=NAVY)
    ax.annotate("110.89%\n(2016 drawdown)", xy=(2016, 110.89), xytext=(2016.8, 108.5),
                arrowprops=dict(arrowstyle="->", color=TEAL, lw=1), fontsize=8.5, color=TEAL)
    ax.set_title("MA-RI: Deciding Productivity vs. Standard Clearance Rate (2015–2025)",
                 fontsize=11, fontweight="bold", color=NAVY, pad=10, loc="left")
    ax.set_ylabel("Percentage (%)", fontweight="bold", color=SLATE)
    ax.set_ylim(74, 115)
    ax.set_xticks(years)
    ax.grid(axis="y", linestyle="--", alpha=0.4)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="lower right", frameon=True, facecolor="white", edgecolor="#e2e8f0", fontsize=8)
    fig.text(0.01, 0.01, "Source: Mahkamah Agung RI Annual Reports (2015-2025). Note: Official MA 'Clearance Rate' measures minutated/sent cases vs. incoming.", fontsize=8, color="#64748b")
    plt.tight_layout(rect=[0, 0.035, 1, 1])
    fig.savefig(ASSETS_DIR / "clearance-trend.png", dpi=220)
    plt.close(fig)

    # Chart 3: data-verification-status.png
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.2, 3.6), dpi=220)
    fig.patch.set_facecolor("white")
    rec_counts = df["verification_status"].value_counts()
    colors_map = {"VERIFIED": TEAL, "PARTIALLY VERIFIED": BLUE, "DISCREPANCY IDENTIFIED": AMBER}
    c1 = [colors_map.get(k, SLATE) for k in rec_counts.index]
    b1 = ax1.barh(rec_counts.index, rec_counts.values, color=c1, height=0.55)
    for b, v in zip(b1, rec_counts.values):
        ax1.text(v + 0.25, b.get_y() + b.get_height()/2, str(int(v)), va="center", fontweight="bold", fontsize=9, color=SLATE)
    ax1.set_xlim(0, max(rec_counts.values) + 3)
    ax1.set_title("Dataset Records (n = 19)", fontsize=10.5, fontweight="bold", color=NAVY, loc="left")
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    tier_counts = df["court_level"].value_counts()
    b2 = ax2.barh(tier_counts.index, tier_counts.values, color=NAVY, alpha=0.85, height=0.55)
    for b, v in zip(b2, tier_counts.values):
        ax2.text(v + 0.2, b.get_y() + b.get_height()/2, str(int(v)), va="center", fontweight="bold", fontsize=9, color=SLATE)
    ax2.set_xlim(0, max(tier_counts.values) + 3)
    ax2.set_title("Coverage by Court Tier", fontsize=10.5, fontweight="bold", color=NAVY, loc="left")
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    fig.suptitle("PB-JUD-2026-001 Data Audit: Verification Status & Tier Coverage (2015–2025)", fontsize=11, fontweight="bold", color=NAVY, y=0.98)
    plt.tight_layout(rect=[0, 0.03, 1, 0.92])
    fig.savefig(ASSETS_DIR / "data-verification-status.png", dpi=220)
    plt.close(fig)

    # Chart 4: cover.png
    fig, ax = plt.subplots(figsize=(8.0, 4.5), dpi=220)
    fig.patch.set_facecolor(NAVY)
    ax.set_facecolor(NAVY)
    ax.axis("off")
    ax.text(0.06, 0.82, "INDONESIA JUDICIARY OPEN DATA INITIATIVE  |  PB-JUD-2026-001", color="#93c5fd", fontsize=10, fontweight="bold")
    ax.text(0.06, 0.58, "From Court Statistics to\nBetter Justice Policy", color="white", fontsize=24, fontweight="bold", linespacing=1.25)
    ax.text(0.06, 0.36, "Understanding Caseload, Case Clearance, and Pending Cases\nin Indonesia's Judiciary (2015–2025)", color="#e2e8f0", fontsize=12, linespacing=1.4)
    ax.plot([0.06, 0.94], [0.24, 0.24], color=AMBER, linewidth=2.5)
    ax.text(0.06, 0.13, "Author: Cecep Mustafa   •   GitHub: bsdkijc-dev   •   Kaggle: judicialcollege", color="#cbd5e1", fontsize=9.5)
    ax.text(0.06, 0.06, "Independent Judicial Policy Research  |  Reproducible Open Data & Methodology", color="#94a3b8", fontsize=8.5)
    fig.savefig(ASSETS_DIR / "cover.png", dpi=220, facecolor=NAVY)
    plt.close(fig)

    for png in ASSETS_DIR.glob("*.png"):
        shutil.copy2(png, DOCS_IMG_DIR / png.name)
    print("Regenerated charts and synced to docs/assets/images/")

if __name__ == "__main__":
    main()
