# Executive Summary (`PB-JUD-2026-001`)

**From Court Statistics to Better Justice Policy: Understanding Caseload, Case Clearance, and Pending Cases in Indonesia's Judiciary**

- **Publication ID**: `PB-JUD-2026-001` | **Version**: `1.0.0` | **Date**: November 25, 2026
- **Author**: Cecep Mustafa | **Initiative**: Indonesia Judiciary Open Data Initiative
- **Disclaimer**: Independent research; not an official publication of, nor endorsed by, the Supreme Court of the Republic of Indonesia (*Mahkamah Agung RI*).

## Policy Problem & Research Question
Judicial statistics are frequently cited as headline performance scores—most notably Indonesia's Supreme Court achieving a deciding productivity rate above 99% for six consecutive years (2020–2025). Yet headline ratios can mask structural pressures when indicator definitions diverge, administrative dispatch (*minutasi*) lags behind judicial decision-making (*memutus*), or subordinate court tiers face uneven bottlenecks. This brief asks: *How can consistently defined and verifiable court statistics help judicial policymakers understand workload, identify operational pressures, and improve access to timely justice?*

## Data & Methodology
We audited 18 official publications of the Supreme Court of Indonesia (*Laporan Tahunan MA-RI*, *Laporan Tahunan Kepaniteraan*, *LKjIP*, and official *Kepaniteraan* releases) spanning **2015–2025**, compiling 19 structured records in `data/PB-JUD-2026-001/judicial_caseload.csv`. Every record is classified under a six-tier verification taxonomy (`12 VERIFIED`, `4 PARTIALLY VERIFIED`, `3 DISCREPANCY IDENTIFIED`) and subjected to automated schema and arithmetic reconciliation (`scripts/validate_data.py`).

## Key Verified Findings
1. **Sustained Caseload Expansion**: Supreme Court (`MA-RI`) total active caseload more than doubled (+107.30%), rising from **18,402 cases** in 2015 to **38,148 cases** in 2025, driven by a +159.18% surge in incoming filings (14,630 in 2016 to 37,918 in 2025) handled by **48 Supreme Court Justices** in 2025.
2. **Backlog Compression at the Apex**: Year-end pending cases at `MA-RI` fell **95.57%**, from **3,950 cases** in 2015 (21.47% of caseload) to **175 cases** in 2025 (0.46% of caseload).
3. **Indicator Divergence**: `MA-RI`'s *Rasio Produktivitas Memutus* (`Resolved / Total Caseload`) rose from **78.53%** (2015) to **99.54%** (2025), averaging **99.25%** over 2020–2025. By contrast, the international standard clearance rate (`Resolved / Incoming`) averaged **102.36%** (2016–2025), and Kepaniteraan's *Clearance Rate* (`Minutated & Dispatched / Incoming`) was **96.71%** in 2024 and **105.31%** in 2025 (39,931 dispatched vs. 37,918 incoming).
4. **Subordinate Court Bottlenecks & Data Discrepancies**: In 2025, first-instance courts carried **2,922,627** cases across **7,032 judges**, while appellate courts recorded an **89.25%** productivity rate (4,407 pending). Three source discrepancies were flagged without silent alteration, including a **10,000-case** gap between the reported 2025 national total (3,035,152) and its tier sum (3,025,152).
