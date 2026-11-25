# Reconciliation Protocol

Automated checks in `scripts/validate_data.py` enforce:
1. **Within-Year Caseload Identity**: `opening_pending + incoming_cases == total_caseload`.
2. **Year-End Balance Identity**: `total_caseload - resolved_cases - withdrawn_cases == pending_cases`.
3. **Cross-Year Continuity**: `opening_pending(t) == pending_cases(t-1)`.

## Documented Discrepancies (Not Silently Altered)
1. **2016 MA-RI Resolved Cases (`REC-MA-2016`)**: Narrative text in Kepaniteraan Newsletter No. 8 (Jan 2017, p. 1) states `16.233`, whereas the chamber and authority breakdowns in the same issue sum to `16,223`, and `18,580 - 2,357 = 16,223` (`87.31%`). We record `16223` and tag `DISCREPANCY IDENTIFIED`.
2. **2021→2022 MA-RI Opening Balance (`REC-MA-2022`)**: 2021 ended with `175` pending cases, while 2022 total caseload (`28,264`) minus incoming (`28,109`) implies an opening balance of `155` (`-20` case administrative adjustment). Tagged `DISCREPANCY IDENTIFIED`.
3. **2025 National Aggregate (`REC-NAT-2025`)**: Kepaniteraan Registry News 2871 reports total national caseload as `3,035,152`, whereas its four listed components (`38,148 + 40,985 + 2,922,627 + 23,392`) sum to `3,025,152` (`-10,000` difference). Tagged `DISCREPANCY IDENTIFIED`.
