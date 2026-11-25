#!/usr/bin/env python3
"""
Repeatable Publication Pipeline Runner for judiciary-policy-briefs.
Validates data, generates statistics and charts, and executes notebooks.
"""
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def run_step(script_name):
    path = BASE_DIR / "scripts" / script_name
    print(f"=== Running {script_name} ===")
    res = subprocess.run([sys.executable, str(path)], check=False)
    if res.returncode != 0:
        print(f"FAILED: {script_name} exited with {res.returncode}")
        sys.exit(res.returncode)

def main():
    run_step("validate_data.py")
    run_step("generate_statistics.py")
    run_step("generate_charts.py")
    run_step("run_notebooks.py")
    print("Publication build pipeline completed successfully.")

if __name__ == "__main__":
    main()
