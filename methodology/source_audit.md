# Source Audit Report (`PB-JUD-2026-001`)

## 1. Research Scope
This audit covers official statistical publications of the **Supreme Court of the Republic of Indonesia (Mahkamah Agung Republik Indonesia / MA-RI)** and its Registrar's Office (**Kepaniteraan MA-RI**) for the reporting window **2015–2025**. The primary objective is to establish a verifiable, source-traceable longitudinal baseline for caseload, case disposition, clearance, and year-end pending cases.

## 2. Sources Located and Audited
Eighteen (18) institutional sources were catalogued in `data/PB-JUD-2026-001/source_register.csv`:
- **VERIFIED (16 sources)**: Official Mahkamah Agung RI Annual Reports (*Laporan Tahunan* 2016, 2021, 2023, 2024, 2025), Executive Summaries (2018, 2025), Kepaniteraan Annual Reports (2024, 2025), Government Agency Performance Accountability Reports (*LKjIP Kepaniteraan* 2019, 2024), Official Kepaniteraan Newsletters (No. 8 Jan 2017; No. 16 Jan 2022), *Kinerja MA 2024 dalam Angka*, and official Kepaniteraan Registry News releases (2020, 2022, 2025).
- **PARTIALLY VERIFIED (1 source)**: `SRC-MA-2015-LEIP` (LEIP 2017 analysis citing *Laporan Tahunan MA RI 2015* pp. 20–21), used for 2015 MA-RI total caseload (18,402), resolved (14,452), and pending (3,950), corroborated by Kepaniteraan Newsletter No. 8 (78.53% rate, 3,950 pending, 14,172 minutated).
- **DISCREPANCY IDENTIFIED (1 source)**: `SRC-MA-2025-NEWS-NAT` (Kepaniteraan Registry News 2871, Feb 10, 2026), which reports 2025 national total caseload as 3,035,152 while its listed tier components (38,148 + 40,985 + 2,922,627 + 23,392) sum to 3,025,152.

## 3. Reporting-Period Coverage & Missing Publications
- **Supreme Court (MA-RI) Annual Series**: Complete 11-year coverage (2015–2025) for total caseload, resolved cases, year-end pending cases, and deciding productivity rate. Incoming cases are directly verified for 2016–2025 (with 2018 derived from official YoY growth +10.65% and 2015 incoming left `NULL` under our zero-imputation rule).
- **Subordinate Courts (4 Judicial Environments + Tax Court)**: Verified snapshots exist for 2017 (4-jurisdiction incoming/resolved/pending), 2020 (Appellate+Tax and First Instance), 2024 (national aggregate), and 2025 (national aggregate + Appellate + First Instance + Tax Court). Full 2015–2025 chamber-by-chamber and court-by-court annual tables remain an outstanding extraction task for future releases.

## 4. Comparability Limitations
1. **Metric Definition Divergence**: Indonesian judicial reports emphasize *Rasio Produktivitas Memutus* (`Resolved / Total Caseload`), whereas international benchmarks (CEPEJ, NCSC) define **Clearance Rate** as `Resolved / Incoming`. Meanwhile, Kepaniteraan MA defines its *Clearance Rate* (`Rasio Penyelesaian Perkara`) as `Minutated & Dispatched / Incoming`.
2. **Withdrawn Cases Treatment**: First-instance and appellate totals include withdrawn cases (*Perkara Dicabut*) in the disposition numerator, whereas Supreme Court totals typically report `0` withdrawals.
3. **Tax Court Inclusion**: National aggregates in 2020 and 2025 explicitly include the Tax Court (*Pengadilan Pajak*) alongside the four core judicial environments; earlier 2017 summaries report only the four environments.
