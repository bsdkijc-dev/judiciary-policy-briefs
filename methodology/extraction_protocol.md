# Extraction Protocol

1. **Primary Source Priority**: Extract statistics exclusively from official Mahkamah Agung RI and Kepaniteraan MA-RI publications (`kepaniteraan.mahkamahagung.go.id`). Secondary institutional citations (e.g., LEIP) are permitted only when primary PDFs are unavailable and must be tagged `PARTIALLY VERIFIED`.
2. **Provenance Capture**: Every row in `judicial_caseload.csv` must link via `source_id` to `source_register.csv` with `source_document`, `source_page`, and `source_table` populated.
3. **Zero-Imputation Policy**: Missing fields (such as 2015 `incoming_cases` or 2025 First Instance `pending_cases`) are left empty (`NULL`) rather than estimated or interpolated, except where exact deterministic accounting identities hold (`total_caseload = opening_pending + incoming_cases`) and are documented in `research_notes`.
4. **No PII**: Only aggregate institutional/tier counts are extracted. No judge, staff, or litigant identifiers are collected.
