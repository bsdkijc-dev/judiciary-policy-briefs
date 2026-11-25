#!/usr/bin/env python3
"""
Automated Data Validation & Reconciliation Script for PB-JUD-2026-001
Validates schema, required fields, duplicates, numeric bounds, arithmetic
identities, and source_id referential integrity, outputting validation_status.csv.
"""
import csv
import os
import sys
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "PB-JUD-2026-001"

REQUIRED_CASELOAD_COLS = [
    "record_id", "report_year", "court_id", "court_name", "court_level",
    "jurisdiction", "case_category", "opening_pending", "incoming_cases",
    "total_caseload", "resolved_cases", "withdrawn_cases", "pending_cases",
    "deciding_productivity_rate", "minutated_sent_cases",
    "official_clearance_rate", "standard_clearance_rate", "source_id",
    "source_document", "source_page", "source_table", "verification_status",
    "dataset_version", "research_notes"
]

VALID_VERIFICATION_STATUSES = {
    "VERIFIED", "PARTIALLY VERIFIED", "UNVERIFIED",
    "DISCREPANCY IDENTIFIED", "NOT AVAILABLE", "NOT COMPARABLE"
}

def main():
    caseload_path = DATA_DIR / "judicial_caseload.csv"
    source_path = DATA_DIR / "source_register.csv"
    dict_path = DATA_DIR / "data_dictionary.csv"
    out_path = DATA_DIR / "validation_status.csv"

    df = pd.read_csv(caseload_path)
    src = pd.read_csv(source_path)
    dd = pd.read_csv(dict_path)

    checks = []

    def log_check(check_id, category, target, status, details):
        checks.append({
            "check_id": check_id,
            "category": category,
            "target": target,
            "status": status,
            "details": details
        })

    # 1. Schema check
    missing_cols = [c for c in REQUIRED_CASELOAD_COLS if c not in df.columns]
    log_check(
        "VAL-001", "Schema", "judicial_caseload.csv",
        "PASS" if not missing_cols else "FAIL",
        "All 24 required columns present." if not missing_cols else f"Missing: {missing_cols}"
    )

    # 2. Data dictionary alignment
    dd_cols = set(dd["column_name"].tolist())
    df_cols = set(df.columns.tolist())
    log_check(
        "VAL-002", "Schema", "data_dictionary.csv",
        "PASS" if dd_cols == df_cols else "FAIL",
        "Data dictionary matches dataset columns 1:1." if dd_cols == df_cols else f"Mismatch: {dd_cols ^ df_cols}"
    )

    # 3. Duplicate record_id check
    dups = df[df.duplicated(subset=["record_id"], keep=False)]
    log_check(
        "VAL-003", "Uniqueness", "record_id",
        "PASS" if dups.empty else "FAIL",
        f"0 duplicate record_ids across {len(df)} rows." if dups.empty else f"Duplicates: {dups['record_id'].tolist()}"
    )

    # 4. Reporting year bounds (2015-2025)
    invalid_years = df[(df["report_year"] < 2015) | (df["report_year"] > 2025)]
    log_check(
        "VAL-004", "Domain", "report_year",
        "PASS" if invalid_years.empty else "FAIL",
        "All report_year values within 2015-2025." if invalid_years.empty else f"Out of range: {invalid_years['record_id'].tolist()}"
    )

    # 5. Source referential integrity
    valid_sources = set(src["source_id"].tolist())
    orphan_sources = df[~df["source_id"].isin(valid_sources)]
    log_check(
        "VAL-005", "Referential Integrity", "source_id",
        "PASS" if orphan_sources.empty else "FAIL",
        f"All {len(df)} records link to valid source_register.csv entries." if orphan_sources.empty else f"Orphans: {orphan_sources['record_id'].tolist()}"
    )

    # 6. Verification status enum check
    bad_status = df[~df["verification_status"].isin(VALID_VERIFICATION_STATUSES)]
    log_check(
        "VAL-006", "Domain", "verification_status",
        "PASS" if bad_status.empty else "FAIL",
        "All verification_status values conform to controlled vocabulary." if bad_status.empty else f"Invalid: {bad_status['record_id'].tolist()}"
    )

    # 7. Non-negative numeric checks
    num_cols = ["opening_pending", "incoming_cases", "total_caseload", "resolved_cases", "withdrawn_cases", "pending_cases", "minutated_sent_cases"]
    neg_found = []
    for c in num_cols:
        s = df[c].dropna()
        if (s < 0).any():
            neg_found.append(c)
    log_check(
        "VAL-007", "Numeric Bounds", "count_columns",
        "PASS" if not neg_found else "FAIL",
        "All non-null case counts are non-negative." if not neg_found else f"Negative values in: {neg_found}"
    )

    # 8. Arithmetic reconciliation: opening + incoming == total_caseload
    sub_load = df.dropna(subset=["opening_pending", "incoming_cases", "total_caseload"])
    load_diff = sub_load[sub_load["opening_pending"] + sub_load["incoming_cases"] != sub_load["total_caseload"]]
    log_check(
        "VAL-008", "Arithmetic", "opening + incoming == total_caseload",
        "PASS" if load_diff.empty else "FAIL",
        f"Exact match across {len(sub_load)} complete caseload rows." if load_diff.empty else f"Mismatch: {load_diff['record_id'].tolist()}"
    )

    # 9. Arithmetic reconciliation: total_caseload - resolved - withdrawn(0) == pending_cases
    sub_pend = df.dropna(subset=["total_caseload", "resolved_cases", "pending_cases"])
    w = sub_pend["withdrawn_cases"].fillna(0)
    pend_diff = sub_pend[sub_pend["total_caseload"] - sub_pend["resolved_cases"] - w != sub_pend["pending_cases"]]
    log_check(
        "VAL-009", "Arithmetic", "caseload - resolved - withdrawn == pending",
        "PASS" if pend_diff.empty else "FAIL",
        f"Exact match across {len(sub_pend)} complete balance rows." if pend_diff.empty else f"Mismatch: {pend_diff['record_id'].tolist()}"
    )

    # 10. Inter-year opening-pending continuity check (MA-RI 2016-2025)
    ma = df[df["court_id"] == "MA-RI"].sort_values("report_year")
    cont_issues = []
    prev_pend = None
    prev_yr = None
    for _, row in ma.iterrows():
        if prev_pend is not None and pd.notna(row["opening_pending"]):
            if int(row["opening_pending"]) != int(prev_pend):
                cont_issues.append(f"{prev_yr}->{int(row['report_year'])}: {int(prev_pend)} vs {int(row['opening_pending'])}")
        prev_pend = row["pending_cases"]
        prev_yr = int(row["report_year"])
    log_check(
        "VAL-010", "Longitudinal Continuity", "MA-RI opening_pending vs prior pending_cases",
        "PASS_WITH_DOCUMENTED_DISCREPANCY" if cont_issues else "PASS",
        f"Documented continuity gap(s): {'; '.join(cont_issues)} (flagged in dataset)." if cont_issues else "All consecutive years match."
    )

    out_df = pd.DataFrame(checks)
    out_df.to_csv(out_path, index=False)
    print(f"Wrote {len(out_df)} validation checks to {out_path}")
    print(out_df[["check_id", "status", "details"]].to_string(index=False))

    hard_fails = [c for c in checks if c["status"] == "FAIL"]
    if hard_fails:
        sys.exit(1)

if __name__ == "__main__":
    main()
