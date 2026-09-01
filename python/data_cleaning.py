import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_PATH = BASE_DIR / "data" / "raw" / "loan.csv"
OUTPUT_PATH = BASE_DIR / "data" / "cleaned" / "loan_cleaned.csv"

df = pd.read_csv(RAW_PATH)

df["ApplicationDate"] = pd.to_datetime(df["ApplicationDate"])

numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

df = df.drop_duplicates()

df = df.sort_values("ApplicationDate").reset_index(drop=True)

df["ApplicationYear"] = df["ApplicationDate"].dt.year
df["ApplicationMonth"] = df["ApplicationDate"].dt.month
df["ApplicationQuarter"] = df["ApplicationDate"].dt.quarter

df["LoanToIncomeRatio"] = (
    df["LoanAmount"] / df["AnnualIncome"]
)

df.to_csv(OUTPUT_PATH, index=False)

print("Data cleaning completed.")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns):,}")
print(f"Saved to: {OUTPUT_PATH}")