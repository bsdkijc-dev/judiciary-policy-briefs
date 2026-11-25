# Contributing to `judiciary-policy-briefs`

We welcome independent verification, methodological critique, and primary-source additions from judicial researchers, legal scholars, and open-data practitioners.

## Non-Negotiable Standards
1. **Verification Before Publication**: Never submit unverified statistics. Every observation must link to a primary institutional source in `source_register.csv`.
2. **Zero Imputation**: Missing values must remain `NULL` (empty CSV cells) with explicit status tags (`VERIFIED`, `PARTIALLY VERIFIED`, `UNVERIFIED`, `DISCREPANCY IDENTIFIED`, `NOT AVAILABLE`, `NOT COMPARABLE`).
3. **No Silent Reconciliation**: Flag arithmetic or narrative-table discrepancies in `research_notes` and `validation_status.csv` rather than altering reported figures.
4. **No PII**: Submit only court-level or tier-level aggregates. Never include personal identifying information of judges, staff, or litigants.
5. **Run Validation Before Pull Requests**:
   ```bash
   python3 scripts/validate_data.py
   ```
