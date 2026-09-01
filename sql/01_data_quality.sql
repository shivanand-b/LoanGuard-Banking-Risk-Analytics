USE loanguard;

-- Total applications
SELECT COUNT(*) AS TotalApplications
FROM loan_applications;

-- Check NULL values in important columns
SELECT
    COUNT(*) AS TotalRows,
    SUM(ApplicationDate IS NULL) AS NullApplicationDate,
    SUM(CreditScore IS NULL) AS NullCreditScore,
    SUM(AnnualIncome IS NULL) AS NullAnnualIncome,
    SUM(LoanAmount IS NULL) AS NullLoanAmount,
    SUM(LoanApproved IS NULL) AS NullLoanApproved,
    SUM(RiskScore IS NULL) AS NullRiskScore
FROM loan_applications;

-- Basic dataset summary
SELECT
    COUNT(*) AS Applications,
    ROUND(AVG(Age), 2) AS AvgAge,
    ROUND(AVG(CreditScore), 2) AS AvgCreditScore,
    ROUND(AVG(LoanAmount), 2) AS AvgLoanAmount,
    ROUND(AVG(AnnualIncome), 2) AS AvgAnnualIncome,
    ROUND(AVG(RiskScore), 2) AS AvgRiskScore,
    ROUND(AVG(LoanApproved) * 100, 2) AS ApprovalRate
FROM loan_applications;