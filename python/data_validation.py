import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "cleaned" / "loan_cleaned.csv"

df = pd.read_csv(DATA_PATH)

print("LoanGuard - Data Validation")
print("-" * 40)

print("\nDataset:")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns):,}")

print("\nMissing Values:")
missing = df.isnull().sum()
print(f"Total missing values: {missing.sum():,}")

print("\nDuplicate Records:")
print(f"Duplicate rows: {df.duplicated().sum():,}")

print("\nDate Range:")
print(f"Start: {df['ApplicationDate'].min()}")
print(f"End:   {df['ApplicationDate'].max()}")

print("\nBusiness Rule Checks:")

checks = {
    "Age outside 18-80": ((df["Age"] < 18) | (df["Age"] > 80)).sum(),
    "Credit score outside 300-850": (
        (df["CreditScore"] < 300) | (df["CreditScore"] > 850)
    ).sum(),
    "Negative annual income": (df["AnnualIncome"] < 0).sum(),
    "Negative loan amount": (df["LoanAmount"] < 0).sum(),
    "Invalid loan approval value": (
        ~df["LoanApproved"].isin([0, 1])
    ).sum(),
    "Invalid bankruptcy value": (
        ~df["BankruptcyHistory"].isin([0, 1])
    ).sum(),
    "Invalid previous defaults value": (
        ~df["PreviousLoanDefaults"].isin([0, 1])
    ).sum(),
    "Credit utilization outside 0-1": (
        (df["CreditCardUtilizationRate"] < 0) |
        (df["CreditCardUtilizationRate"] > 1)
    ).sum(),
    "Debt-to-income outside 0-1": (
        (df["DebtToIncomeRatio"] < 0) |
        (df["DebtToIncomeRatio"] > 1)
    ).sum(),
    "Negative net worth": (df["NetWorth"] < 0).sum(),
    "Invalid loan-to-income ratio": (
        df["LoanToIncomeRatio"] < 0
    ).sum()
}

for check, count in checks.items():
    status = "PASS" if count == 0 else "CHECK"
    print(f"{status:<6} {check}: {count:,}")

print("\nDerived Metrics:")
print(
    f"LoanToIncomeRatio range: "
    f"{df['LoanToIncomeRatio'].min():.2f} - "
    f"{df['LoanToIncomeRatio'].max():.2f}"
)

print(
    f"Application years: "
    f"{df['ApplicationYear'].min()} - "
    f"{df['ApplicationYear'].max()}"
)

print("\nValidation completed.")