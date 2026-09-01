import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "cleaned" / "loan_cleaned.csv"

df = pd.read_csv(DATA_PATH)

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

print("LoanGuard - Risk Analysis")
print("-" * 35)

risk_summary = (
    df.groupby("LoanApproved")
    .agg(
        Applications=("LoanApproved", "count"),
        AvgCreditScore=("CreditScore", "mean"),
        AvgRiskScore=("RiskScore", "mean"),
        AvgLoanAmount=("LoanAmount", "mean"),
        AvgAnnualIncome=("AnnualIncome", "mean"),
        PreviousDefaults=("PreviousLoanDefaults", "sum"),
        BankruptcyCases=("BankruptcyHistory", "sum")
    )
)

print("\nRisk Summary:")
print(risk_summary.round(2))

print("\nPrevious Default Rate by Approval:")
default_rate = (
    df.groupby("LoanApproved")["PreviousLoanDefaults"]
    .mean()
    .mul(100)
    .round(2)
)

print(default_rate)

print("\nBankruptcy Rate by Approval:")
bankruptcy_rate = (
    df.groupby("LoanApproved")["BankruptcyHistory"]
    .mean()
    .mul(100)
    .round(2)
)

print(bankruptcy_rate)

print("\nCredit Score Bands:")

df["CreditScoreBand"] = pd.cut(
    df["CreditScore"],
    bins=[0, 579, 669, 739, 799, 850],
    labels=[
        "Poor",
        "Fair",
        "Good",
        "Very Good",
        "Excellent"
    ]
)

credit_analysis = (
    df.groupby("CreditScoreBand", observed=True)
    .agg(
        Applications=("LoanApproved", "count"),
        ApprovalRate=("LoanApproved", "mean"),
        AvgLoanAmount=("LoanAmount", "mean"),
        AvgRiskScore=("RiskScore", "mean")
    )
)

credit_analysis["ApprovalRate"] *= 100

print(credit_analysis.round(2))

print("\nRisk Factor Distribution:")

risk_factors = [
    "CreditScore",
    "DebtToIncomeRatio",
    "TotalDebtToIncomeRatio",
    "CreditCardUtilizationRate",
    "NumberOfCreditInquiries",
    "LoanToIncomeRatio",
    "RiskScore"
]

print(
    df[risk_factors]
    .describe()
    .T
    .round(3)
)

print("\nRisk Factor Percentiles:")

print(
    df[risk_factors]
    .quantile([0.25, 0.50, 0.75, 0.90])
    .T
    .round(3)
)

print("\nPrevious Defaults and Bankruptcy:")
print(
    df[
        ["PreviousLoanDefaults", "BankruptcyHistory"]
    ].mean().mul(100).round(2)
)

print("\nRisk Indicator Analysis:")

df["LowCreditScore"] = (df["CreditScore"] < 540).astype(int)
df["HighDebtRatio"] = (df["TotalDebtToIncomeRatio"] > 0.509).astype(int)
df["HighCreditUtilization"] = (
    df["CreditCardUtilizationRate"] > 0.510
).astype(int)
df["HighLoanToIncome"] = (
    df["LoanToIncomeRatio"] > 1.250
).astype(int)
df["FrequentCreditInquiries"] = (
    df["NumberOfCreditInquiries"] >= 3
).astype(int)

df["RiskPoints"] = (
    df["LowCreditScore"]
    + df["HighDebtRatio"]
    + df["HighCreditUtilization"]
    + df["HighLoanToIncome"]
    + df["FrequentCreditInquiries"]
    + df["PreviousLoanDefaults"]
    + df["BankruptcyHistory"]
)

df["RiskCategory"] = pd.cut(
    df["RiskPoints"],
    bins=[-1, 1, 3, 7],
    labels=["Low Risk", "Medium Risk", "High Risk"]
)

risk_categories = (
    df.groupby("RiskCategory", observed=True)
    .agg(
        Applications=("RiskPoints", "count"),
        AvgCreditScore=("CreditScore", "mean"),
        AvgRiskScore=("RiskScore", "mean"),
        AvgLoanAmount=("LoanAmount", "mean"),
        AvgAnnualIncome=("AnnualIncome", "mean"),
        ApprovalRate=("LoanApproved", "mean")
    )
)

risk_categories["ApprovalRate"] *= 100

print("\nRisk Category Summary:")
print(risk_categories.round(2))

print("\nRisk Category Distribution:")
print(
    df["RiskCategory"]
    .value_counts()
    .sort_index()
)

print("\nHigh Risk Applications:")
print(
    df[df["RiskCategory"] == "High Risk"][
        [
            "CreditScore",
            "RiskScore",
            "TotalDebtToIncomeRatio",
            "CreditCardUtilizationRate",
            "LoanToIncomeRatio",
            "PreviousLoanDefaults",
            "BankruptcyHistory",
            "RiskPoints"
        ]
    ].head(10)
)

print("\nRisk analysis completed.")