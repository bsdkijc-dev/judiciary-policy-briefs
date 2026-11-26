# Indonesia Judiciary Open Data Initiative — Policy Briefs (`judiciary-policy-briefs`)

[![Validate Judicial Data](https://github.com/bsdkijc-dev/judiciary-policy-briefs/actions/workflows/validate-data.yml/badge.svg)](https://github.com/bsdkijc-dev/judiciary-policy-briefs/actions/workflows/validate-data.yml)
[![Deploy GitHub Pages](https://github.com/bsdkijc-dev/judiciary-policy-briefs/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/bsdkijc-dev/judiciary-policy-briefs/actions/workflows/deploy-pages.yml)

**Evidence for Better Justice Policy.** An independent, reproducible judicial policy research and open government data portfolio connecting official institutional sources to verified datasets, reproducible Python analysis, policy briefs, and public-facing web documentation.

- **Research Lead**: Cecep Mustafa (`bsdkijc-dev` | Kaggle: [`judicialcollege`](https://www.kaggle.com/judicialcollege/datasets))
- **Live Website (GitHub Pages)**: [`https://bsdkijc-dev.github.io/judiciary-policy-briefs/`](https://bsdkijc-dev.github.io/judiciary-policy-briefs/)
- **Future Platform Integration**: Designed for modular interoperability with **JPAIS** (Judicial Policy Analyst AI Suite).

---

## Published Policy Briefs & Live Kaggle Datasets (2026 Series)

| Publication ID | Title | Policy Brief PDF | Live Kaggle Dataset |
| :--- | :--- | :--- | :--- |
| **`PB-JUD-2026-001`** | *From Court Statistics to Better Justice Policy: Caseload, Clearance & Pending Cases* | [`policy-brief.pdf`](briefs/PB-JUD-2026-001-caseload/policy-brief.pdf) | [`indonesia-judiciary-caseload-2015-2025`](https://www.kaggle.com/datasets/judicialcollege/indonesia-judiciary-caseload-2015-2025) ([Notebook](https://www.kaggle.com/code/judicialcollege/judicial-caseload-indonesia-exploratory-analysis)) |
| **`PB-JUD-2026-002`** | *Measuring Access to Justice and Legal Aid (Posbakum, Prodeo & BPHN)* | [`policy-brief.pdf`](briefs/PB-JUD-2026-002-legal-aid/policy-brief.pdf) | [`indonesia-access-to-justice-and-legal-aid`](https://www.kaggle.com/datasets/judicialcollege/indonesia-access-to-justice-and-legal-aid) |
| **`PB-JUD-2026-003`** | *Judicial Resources and Institutional Capacity (Staffing, Budget & 3-Panel Density)* | [`policy-brief.pdf`](briefs/PB-JUD-2026-003-resources/policy-brief.pdf) | [`indonesia-judicial-resources-and-capacity`](https://www.kaggle.com/datasets/judicialcollege/indonesia-judicial-resources-and-capacity) |
| **`PB-JUD-2026-004`** | *Court Efficiency, Timeliness, and Case Management (Deciding vs. Minutation)* | [`policy-brief.pdf`](briefs/PB-JUD-2026-004-timeliness/policy-brief.pdf) | [`indonesia-court-timeliness-benchmarks`](https://www.kaggle.com/datasets/judicialcollege/indonesia-court-timeliness-benchmarks) |
| **`PB-JUD-2026-005`** | *Judicial Transparency and Public Accountability (Direktori Putusan & SMAP)* | [`policy-brief.pdf`](briefs/PB-JUD-2026-005-transparency/policy-brief.pdf) | [`indonesia-judicial-transparency-accountability`](https://www.kaggle.com/datasets/judicialcollege/indonesia-judicial-transparency-accountability) |
| **`PB-JUD-2026-006`** | *Digital Justice and Institutional Transformation (e-Court, e-Berpadu & e-Kasasi)* | [`policy-brief.pdf`](briefs/PB-JUD-2026-006-digital-justice/policy-brief.pdf) | [`indonesia-digital-justice-transformation`](https://www.kaggle.com/datasets/judicialcollege/indonesia-digital-justice-transformation) |

---

## Reproducibility
```bash
python3 scripts/validate_data.py
python3 scripts/generate_statistics.py
python3 scripts/generate_charts.py
python3 scripts/run_notebooks.py
```

## Independent Research Disclaimer
This repository is an independent open-data research initiative. It is not officially endorsed by, nor an official publication of, the Supreme Court of the Republic of Indonesia (*Mahkamah Agung RI*), BSDK, IJC, or BPHN.
