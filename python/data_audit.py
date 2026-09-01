import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "loan.csv"

df = pd.read_csv(DATA_PATH)

print("LoanGuard - Banking Risk & Customer Analytics")
print("-" * 50)

print("\nDataset Shape:")
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]:,}")

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
missing = df.isnull().sum()
missing_df = pd.DataFrame({
    "Missing Values": missing,
    "Missing %": (missing / len(df) * 100).round(2)
})

print(missing_df[missing_df["Missing Values"] > 0])

print("\nDuplicate Records:")
print(f"Duplicate rows: {df.duplicated().sum():,}")

print("\nNumerical Summary:")
print(df.describe().T)

categorical_columns = df.select_dtypes(
    include=["object", "str", "category"]
).columns

print("\nCategorical Columns:")
for column in categorical_columns:
    print(f"\n{column}")
    print(df[column].value_counts(dropna=False).head(10))

print("\nUnique Values:")
for column in df.columns:
    print(f"{column}: {df[column].nunique():,}")

print("\nDataset Preview:")
print(df.head())

print("\nData audit completed.")