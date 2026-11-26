#!/usr/bin/env bash
set -euo pipefail

# Automated Workstation Publisher for judiciary-policy-briefs (PB-JUD-2026-001)
# Run this script from inside the unzipped `judiciary-policy-briefs/` directory.

REPO_OWNER="bsdkijc-dev"
REPO_NAME="judiciary-policy-briefs"
KAGGLE_DIR="kaggle_package/PB-JUD-2026-001"

echo "=== [1/4] Verifying local data validation ==="
python3 scripts/validate_data.py

echo "=== [2/4] Pushing repository to GitHub (${REPO_OWNER}/${REPO_NAME}) ==="
if command -v gh >/dev/null 2>&1; then
  gh repo view "${REPO_OWNER}/${REPO_NAME}" >/dev/null 2>&1 || \
    gh repo create "${REPO_OWNER}/${REPO_NAME}" --public \
      --description "Indonesia Judiciary Open Data Initiative: reproducible policy briefs, verified caseload datasets, and methodology."
fi
git branch -M main
git remote set-url origin "git@github.com:${REPO_OWNER}/${REPO_NAME}.git"
git push -u origin main

echo "=== [3/4] Enabling GitHub Pages (GitHub Actions workflow) ==="
if command -v gh >/dev/null 2>&1; then
  gh api -X POST "repos/${REPO_OWNER}/${REPO_NAME}/pages" \
    -f build_type="workflow" 2>/dev/null || \
  gh api -X PUT "repos/${REPO_OWNER}/${REPO_NAME}/pages" \
    -f build_type="workflow" 2>/dev/null || \
    echo "Enable Pages manually: GitHub Repo -> Settings -> Pages -> Source: GitHub Actions"
else
  echo "gh CLI not found; enable Pages at: https://github.com/${REPO_OWNER}/${REPO_NAME}/settings/pages (Source: GitHub Actions)"
fi

echo "=== [4/4] Publishing Kaggle dataset and notebook ==="
if command -v kaggle >/dev/null 2>&1; then
  kaggle datasets create -p "${KAGGLE_DIR}" --dir-mode zip || \
    kaggle datasets version -p "${KAGGLE_DIR}" -m "Release v1.0.0 (PB-JUD-2026-001)" --dir-mode zip
  kaggle kernels push -p "${KAGGLE_DIR}"
else
  echo "ERROR: kaggle CLI not found. Install/activate your venv and run:"
  echo "  kaggle datasets create -p ${KAGGLE_DIR} --dir-mode zip"
  echo "  kaggle kernels push -p ${KAGGLE_DIR}"
  exit 1
fi

echo "Done! Verify live links:"
echo "  GitHub:       https://github.com/${REPO_OWNER}/${REPO_NAME}"
echo "  GitHub Pages: https://${REPO_OWNER}.github.io/${REPO_NAME}/"
echo "  Kaggle:       https://www.kaggle.com/judicialcollege/datasets"
