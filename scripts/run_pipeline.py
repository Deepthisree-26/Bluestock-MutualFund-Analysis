"""
Master Pipeline Script
Bluestock Mutual Fund Analysis
"""

import os

scripts = [
    "data_ingestion.py",
    "clean_nav_history.py",
    "clean_transactions.py",
    "clean_performance.py",
    "create_database.py"
]

for script in scripts:
    print(f"Running {script}")
    os.system(f"python scripts/{script}")

print("Pipeline Completed Successfully")