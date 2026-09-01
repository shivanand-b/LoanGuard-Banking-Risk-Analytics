import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "cleaned" / "loan_cleaned.csv"

df = pd.read_csv(DATA_PATH)

print("LoanGuard - Exploratory Data Analysis")
print("-" * 45)

print("\nLoan Approval Overview:")
print(df["LoanApproved"].value_counts())
print(df["LoanApproved"].value_counts(normalize=True).round(4) * 100)

print("\nEmployment Status:")
print(df["EmploymentStatus"].value_counts())

print("\nLoan Purpose:")
print(df["LoanPurpose"].value_counts())

print("\nEducation Level:")
print(df["EducationLevel"].value_counts())

print("\nHome Ownership:")
print(df["HomeOwnershipStatus"].value_counts())

print("\nKey Numeric Metrics:")
metrics = [
    "AnnualIncome",
    "CreditScore",
    "LoanAmount",
    "InterestRate",
    "DebtToIncomeRatio",
    "TotalDebtToIncomeRatio",
    "RiskScore"
]

print(df[metrics].describe().T)

print("\nAverage Metrics by Loan Approval:")
print(
    df.groupby("LoanApproved")[metrics]
    .mean()
    .round(2)
)

print("\nAverage Metrics by Employment Status:")
print(
    df.groupby("EmploymentStatus")[metrics]
    .mean()
    .round(2)
)

print("\nAverage Metrics by Loan Purpose:")
print(
    df.groupby("LoanPurpose")[metrics]
    .mean()
    .round(2)
)

print("\nLoan Approval Rate by Employment Status:")
approval_by_employment = (
    df.groupby("EmploymentStatus")["LoanApproved"]
    .mean()
    .mul(100)
    .round(2)
)

print(approval_by_employment)

print("\nLoan Approval Rate by Loan Purpose:")
approval_by_purpose = (
    df.groupby("LoanPurpose")["LoanApproved"]
    .mean()
    .mul(100)
    .round(2)
)

print(approval_by_purpose)

print("\nLoan Approval Rate by Education Level:")
approval_by_education = (
    df.groupby("EducationLevel")["LoanApproved"]
    .mean()
    .mul(100)
    .round(2)
)

print(approval_by_education)

print("\nAverage Credit Score by Loan Approval:")
print(
    df.groupby("LoanApproved")["CreditScore"]
    .mean()
    .round(2)
)

print("\nAverage Loan Amount by Loan Approval:")
print(
    df.groupby("LoanApproved")["LoanAmount"]
    .mean()
    .round(2)
)

print("\nAverage Debt-to-Income Ratio by Loan Approval:")
print(
    df.groupby("LoanApproved")["DebtToIncomeRatio"]
    .mean()
    .round(4)
)

print("\nAverage Interest Rate by Loan Approval:")
print(
    df.groupby("LoanApproved")["InterestRate"]
    .mean()
    .round(4)
)

print("\nRisk Score Distribution:")
print(df["RiskScore"].describe().round(2))

print("\nRisk Score Percentiles:")
print(
    df["RiskScore"]
    .quantile([0.25, 0.50, 0.75, 0.90])
    .round(2)
)

print("\nPrevious Loan Defaults:")
print(df["PreviousLoanDefaults"].value_counts())

print("\nBankruptcy History:")
print(df["BankruptcyHistory"].value_counts())

print("\nAverage Risk Score by Loan Approval:")
print(
    df.groupby("LoanApproved")["RiskScore"]
    .agg(["count", "mean", "min", "max"])
    .round(2)
)

print("\nEDA completed.")