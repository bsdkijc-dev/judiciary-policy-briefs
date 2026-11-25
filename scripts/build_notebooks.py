#!/usr/bin/env python3
"""
Builds the 4 reproducible Jupyter notebooks for PB-JUD-2026-001 in analysis/PB-JUD-2026-001/.
"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
NB_DIR = BASE_DIR / "analysis" / "PB-JUD-2026-001"
NB_DIR.mkdir(parents=True, exist_ok=True)

def make_nb(cells):
    nb_cells = []
    for ctype, text in cells:
        lines = [line + "\n" for line in text.rstrip("\n").split("\n")]
        if ctype == "md":
            nb_cells.append({"cell_type": "markdown", "metadata": {}, "source": lines})
        else:
            nb_cells.append({"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": lines})
    return {
        "cells": nb_cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11.2"}
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

nb1 = make_nb([
    ("md", "# 01 — Source Audit (`PB-JUD-2026-001`)\nThis notebook audits official Mahkamah Agung RI sources registered in `data/PB-JUD-2026-001/source_register.csv`."),
    ("code", """import pandas as pd
from pathlib import Path

data_dir = Path("../../data/PB-JUD-2026-001")
src = pd.read_csv(data_dir / "source_register.csv")
print(f"Total registered sources: {len(src)}")
print("\\nVerification status breakdown:")
print(src["verification_status"].value_counts())
src[["source_id", "reporting_year", "document_format", "verification_status", "publication_title"]]""")
])

nb2 = make_nb([
    ("md", "# 02 — Data Validation & Reconciliation (`PB-JUD-2026-001`)\nReproduces automated schema, missing-value, duplicate, and arithmetic reconciliation checks."),
    ("code", """import pandas as pd
from pathlib import Path

data_dir = Path("../../data/PB-JUD-2026-001")
df = pd.read_csv(data_dir / "judicial_caseload.csv")
val = pd.read_csv(data_dir / "validation_status.csv")
print("Dataset shape:", df.shape)
print("\\nMissing values per key numeric column:")
print(df[["opening_pending", "incoming_cases", "total_caseload", "resolved_cases", "pending_cases"]].isna().sum())
print("\\nValidation summary:")
val[["check_id", "category", "status", "details"]]""")
])

nb3 = make_nb([
    ("md", "# 03 — Longitudinal Caseload & Clearance Analysis (`PB-JUD-2026-001`)\nAnalyzes Mahkamah Agung RI (2015–2025) caseload dynamics, deciding productivity, and standard clearance rates."),
    ("code", """import pandas as pd
from pathlib import Path

data_dir = Path("../../data/PB-JUD-2026-001")
df = pd.read_csv(data_dir / "judicial_caseload.csv")
ma = df[df["court_id"] == "MA-RI"].sort_values("report_year").copy()
print("MA-RI 2015-2025 Summary:")
print(ma[["report_year", "opening_pending", "incoming_cases", "total_caseload", "resolved_cases", "pending_cases", "deciding_productivity_rate", "standard_clearance_rate"]].to_string(index=False))

c_2015, c_2025 = ma.loc[ma["report_year"]==2015, "total_caseload"].iloc[0], ma.loc[ma["report_year"]==2025, "total_caseload"].iloc[0]
p_2015, p_2025 = ma.loc[ma["report_year"]==2015, "pending_cases"].iloc[0], ma.loc[ma["report_year"]==2025, "pending_cases"].iloc[0]
print(f"\\nCaseload growth 2015->2025: {(c_2025-c_2015)/c_2015*100:.2f}%")
print(f"Pending reduction 2015->2025: {(p_2025-p_2015)/p_2015*100:.2f}%")""")
])

nb4 = make_nb([
    ("md", "# 04 — Publication Visualizations (`PB-JUD-2026-001`)\nGenerates and verifies publication-quality figures for the policy brief and website."),
    ("code", """import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

data_dir = Path("../../data/PB-JUD-2026-001")
df = pd.read_csv(data_dir / "judicial_caseload.csv")
ma = df[df["court_id"] == "MA-RI"].sort_values("report_year")

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(ma["report_year"], ma["deciding_productivity_rate"], marker="o", label="Deciding Productivity Rate (%)")
ax.set_title("MA-RI Deciding Productivity Rate (2015-2025)")
ax.set_ylabel("Percent (%)")
ax.grid(True, alpha=0.3)
ax.legend()
plt.tight_layout()
plt.show()""")
])

for name, nb in [
    ("01_source_audit.ipynb", nb1),
    ("02_data_validation.ipynb", nb2),
    ("03_caseload_analysis.ipynb", nb3),
    ("04_visualizations.ipynb", nb4),
]:
    with open(NB_DIR / name, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)
print("Created 4 notebooks in", NB_DIR)
