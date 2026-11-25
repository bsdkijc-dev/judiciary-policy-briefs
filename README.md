# Indonesia Judiciary Open Data Initiative — Policy Briefs (`judiciary-policy-briefs`)

[![Validate Judicial Data](https://github.com/bsdkijc-dev/judiciary-policy-briefs/actions/workflows/validate-data.yml/badge.svg)](https://github.com/bsdkijc-dev/judiciary-policy-briefs/actions/workflows/validate-data.yml)
[![Deploy GitHub Pages](https://github.com/bsdkijc-dev/judiciary-policy-briefs/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/bsdkijc-dev/judiciary-policy-briefs/actions/workflows/deploy-pages.yml)

**Evidence for Better Justice Policy.** An independent, reproducible judicial policy research and open government data portfolio connecting official institutional sources to verified datasets, reproducible Python analysis, policy briefs, and public-facing web documentation.

- **Research Lead**: Cecep Mustafa (`bsdkijc-dev` | Kaggle: [`judicialcollege`](https://www.kaggle.com/judicialcollege/datasets))
- **Website (GitHub Pages)**: [`https://bsdkijc-dev.github.io/judiciary-policy-briefs/`](https://bsdkijc-dev.github.io/judiciary-policy-briefs/) *(staged in `docs/`, pending remote deployment)*
- **Future Platform Integration**: Designed for modular interoperability with **JPAIS** (Judicial Policy Analyst AI Suite).

---

## Featured Flagship Publication: `PB-JUD-2026-001`
**From Court Statistics to Better Justice Policy: Understanding Caseload, Case Clearance, and Pending Cases in Indonesia's Judiciary (2015–2025)**

- **Policy Brief PDF**: [`briefs/PB-JUD-2026-001-caseload/policy-brief.pdf`](briefs/PB-JUD-2026-001-caseload/policy-brief.pdf)
- **Executive Summary**: [`briefs/PB-JUD-2026-001-caseload/executive-summary.md`](briefs/PB-JUD-2026-001-caseload/executive-summary.md)
- **Dataset (`v1.0.0`)**: [`data/PB-JUD-2026-001/judicial_caseload.csv`](data/PB-JUD-2026-001/judicial_caseload.csv) (19 audited records across 18 official sources)
- **Reproducible Notebooks**: [`analysis/PB-JUD-2026-001/`](analysis/PB-JUD-2026-001/)

### Key Verified Highlights (2015–2025)
- **+107.30% Supreme Court Caseload Growth**: Active caseload at *Mahkamah Agung RI* rose from `18,402` (2015) to `38,148` (2025), handled by `48` Supreme Court Justices in 2025.
- **-95.57% Pending Case Reduction**: Year-end pending cases at `MA-RI` fell from `3,950` (2015) to `175` (2025).
- **Metric Divergence**: Indonesian *Rasio Produktivitas Memutus* (`Resolved / Total Caseload`, averaging `99.25%` across 2020–2025) differs systematically from international Clearance Rate (`Resolved / Incoming`, averaging `102.36%` across 2016–2025) and Kepaniteraan's Minutation Clearance (`Dispatched / Incoming`).
- **Transparent Discrepancy Logging**: 3 source discrepancies (including a 10,000-case tier-sum gap in a 2025 national release) are flagged in `validation_status.csv` rather than silently adjusted.

---

## Repository Structure
- `briefs/PB-JUD-2026-001-caseload/` — Policy brief PDF, executive summary, recommendations, references.
- `data/PB-JUD-2026-001/` — Normalized CSVs (`judicial_caseload.csv`, `source_register.csv`, `data_dictionary.csv`, `validation_status.csv`).
- `methodology/` — Source audit, extraction, normalization, verification, reconciliation, and limitations protocols.
- `analysis/PB-JUD-2026-001/` — 4 reproducible Jupyter notebooks (`01` through `04`).
- `scripts/` — Automated validation, statistics, chart generation, and publication build scripts.
- `docs/` — Jekyll/GitHub Pages public website.
- `.github/workflows/` — Automated CI data validation and GitHub Pages deployment.

## Reproducibility
```bash
python3 scripts/validate_data.py
python3 scripts/generate_statistics.py
python3 scripts/generate_charts.py
python3 scripts/run_notebooks.py
```

## Independent Research Disclaimer
This repository is an independent open-data research initiative. It is not officially endorsed by, nor an official publication of, the Supreme Court of the Republic of Indonesia (*Mahkamah Agung RI*), BSDK, or IJC.
