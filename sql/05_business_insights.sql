USE loanguard;

-- Highest risk applicants
SELECT
    ApplicationDate,
    CreditScore,
    AnnualIncome,
    LoanAmount,
    DebtToIncomeRatio,
    CreditCardUtilizationRate,
    RiskPoints,
    RiskScore,
    RiskCategory,
    LoanApproved
FROM loan_applications
WHERE RiskCategory = 'High Risk'
ORDER BY RiskScore DESC
LIMIT 20;

-- High loan-to-income applicants
SELECT
    ApplicationDate,
    AnnualIncome,
    LoanAmount,
    LoanToIncomeRatio,
    CreditScore,
    RiskCategory
FROM loan_applications
WHERE HighLoanToIncome = 1
ORDER BY LoanToIncomeRatio DESC
LIMIT 20;

-- Low credit score applicants
SELECT
    ApplicationDate,
    CreditScore,
    AnnualIncome,
    LoanAmount,
    RiskScore,
    RiskCategory
FROM loan_applications
WHERE LowCreditScore = 1
ORDER BY CreditScore ASC
LIMIT 20;

-- High debt ratio applicants
SELECT
    ApplicationDate,
    AnnualIncome,
    MonthlyDebtPayments,
    DebtToIncomeRatio,
    LoanAmount,
    RiskCategory
FROM loan_applications
WHERE HighDebtRatio = 1
ORDER BY DebtToIncomeRatio DESC
LIMIT 20;

-- Overall portfolio summary
SELECT
    COUNT(*) AS TotalApplications,
    SUM(LoanApproved) AS ApprovedLoans,
    COUNT(*) - SUM(LoanApproved) AS RejectedLoans,
    ROUND(AVG(LoanApproved) * 100, 2) AS ApprovalRate,
    ROUND(AVG(LoanAmount), 2) AS AvgLoanAmount,
    ROUND(AVG(AnnualIncome), 2) AS AvgAnnualIncome,
    ROUND(AVG(CreditScore), 2) AS AvgCreditScore,
    ROUND(AVG(RiskScore), 2) AS AvgRiskScore
FROM loan_applications;