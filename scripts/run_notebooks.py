#!/usr/bin/env python3
"""
Lightweight Python notebook executor to verify and populate outputs in .ipynb files
when nbconvert is not installed.
"""
import contextlib
import io
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
NB_DIR = BASE_DIR / "analysis" / "PB-JUD-2026-001"

def run_nb(nb_path: Path):
    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    old_cwd = os.getcwd()
    os.chdir(nb_path.parent)
    ns = {}
    try:
        for idx, cell in enumerate(nb["cells"], 1):
            if cell["cell_type"] != "code":
                continue
            code = "".join(cell["source"])
            # Avoid blocking GUI in matplotlib
            code_exec = code.replace("plt.show()", "plt.close('all')")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                exec(compile(code_exec, f"{nb_path.name}#cell{idx}", "exec"), ns)
            out_text = buf.getvalue()
            cell["execution_count"] = idx
            cell["outputs"] = []
            if out_text:
                cell["outputs"].append({
                    "name": "stdout",
                    "output_type": "stream",
                    "text": [line + "\n" for line in out_text.rstrip("\n").split("\n")]
                })
    finally:
        os.chdir(old_cwd)
    with open(nb_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)
    print(f"Executed {nb_path.name} successfully.")

if __name__ == "__main__":
    for p in sorted(NB_DIR.glob("*.ipynb")):
        run_nb(p)
