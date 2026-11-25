# Verification Framework

Every record in `judicial_caseload.csv` and source in `source_register.csv` is assigned one of six controlled verification statuses:

- **VERIFIED**: Directly supported by an identifiable official institutional source and passes arithmetic checks.
- **PARTIALLY VERIFIED**: Supported by official YoY growth rates or secondary institutional citations, with one or more sub-components unconfirmed in primary tables.
- **UNVERIFIED**: Evidence is insufficient to confirm the figure.
- **DISCREPANCY IDENTIFIED**: Official sources conflict with each other, internal narrative conflicts with tables, or component sums do not match reported totals.
- **NOT AVAILABLE**: Required information was not located in public releases.
- **NOT COMPARABLE**: Definitions or reporting structures prevent reliable cross-year or cross-tier comparison.
