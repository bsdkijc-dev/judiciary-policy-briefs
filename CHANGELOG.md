# Changelog

All notable changes to the Indonesia Judiciary Open Data Initiative (`judiciary-policy-briefs`) will be documented in this file.

## [1.0.0] - 2026-11-25
### Added
- Initial repository architecture for `judiciary-policy-briefs`.
- Flagship publication `PB-JUD-2026-001`: *From Court Statistics to Better Justice Policy: Understanding Caseload, Case Clearance, and Pending Cases in Indonesia's Judiciary*.
- Verified dataset `data/PB-JUD-2026-001/judicial_caseload.csv` (19 records, 2015–2025) and `source_register.csv` (18 official sources).
- Automated validation (`scripts/validate_data.py`), statistics (`scripts/generate_statistics.py`), chart generation (`scripts/generate_charts.py`), and 4 reproducible Jupyter notebooks (`analysis/PB-JUD-2026-001/`).
- Complete methodology documentation (`methodology/*.md`), GitHub Actions CI/CD workflows (`.github/workflows/`), GitHub Pages website (`docs/`), Kaggle upload package, and LinkedIn communications kit.
