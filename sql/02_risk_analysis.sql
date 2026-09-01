USE loanguard;

-- Risk point range
SELECT
    MIN(RiskPoints) AS MinRiskPoints,
    MAX(RiskPoints) AS MaxRiskPoints,
    COUNT(*) AS TotalApplications
FROM loan_applications;

-- Risk category distribution
SELECT
    RiskCategory,
    COUNT(*) AS Applications
FROM loan_applications
GROUP BY RiskCategory
ORDER BY
    CASE RiskCategory
        WHEN 'Low Risk' THEN 1
        WHEN 'Medium Risk' THEN 2
        WHEN 'High Risk' THEN 3
    END;

-- Risk category summary
SELECT
    RiskCategory,
    COUNT(*) AS Applications,
    ROUND(AVG(CreditScore), 2) AS AvgCreditScore,
    ROUND(AVG(RiskScore), 2) AS AvgRiskScore,
    ROUND(AVG(LoanAmount), 2) AS AvgLoanAmount,
    ROUND(AVG(AnnualIncome), 2) AS AvgAnnualIncome,
    ROUND(AVG(LoanApproved) * 100, 2) AS ApprovalRate
FROM loan_applications
GROUP BY RiskCategory
ORDER BY
    CASE RiskCategory
        WHEN 'Low Risk' THEN 1
        WHEN 'Medium Risk' THEN 2
        WHEN 'High Risk' THEN 3
    END;

-- Risk factors distribution
SELECT
    SUM(LowCreditScore) AS LowCreditScoreCases,
    SUM(HighDebtRatio) AS HighDebtRatioCases,
    SUM(HighCreditUtilization) AS HighCreditUtilizationCases,
    SUM(HighLoanToIncome) AS HighLoanToIncomeCases,
    SUM(FrequentCreditInquiries) AS FrequentInquiryCases
FROM loan_applications;

-- Risk Drivers
SELECT
    LowCreditScore,
    HighDebtRatio,
    HighCreditUtilization,
    HighLoanToIncome,
    FrequentCreditInquiries,
    COUNT(*) AS Applications,
    ROUND(AVG(RiskScore), 2) AS AvgRiskScore,
    ROUND(AVG(LoanApproved) * 100, 2) AS ApprovalRate
FROM loan_applications
GROUP BY
    LowCreditScore,
    HighDebtRatio,
    HighCreditUtilization,
    HighLoanToIncome,
    FrequentCreditInquiries
ORDER BY Applications DESC;

-- Individual Risk Factor Impact

SELECT
    'Low Credit Score' AS RiskFactor,
    SUM(LowCreditScore) AS FlaggedApplications,
    ROUND(
        AVG(CASE WHEN LowCreditScore = 1 THEN LoanApproved END) * 100,
        2
    ) AS ApprovalRate
FROM loan_applications

UNION ALL

SELECT
    'High Debt Ratio',
    SUM(HighDebtRatio),
    ROUND(AVG(CASE WHEN HighDebtRatio = 1 THEN LoanApproved END) * 100, 2)
FROM loan_applications

UNION ALL

SELECT
    'High Credit Utilization',
    SUM(HighCreditUtilization),
    ROUND(AVG(CASE WHEN HighCreditUtilization = 1 THEN LoanApproved END) * 100, 2)
FROM loan_applications

UNION ALL

SELECT
    'High Loan-to-Income',
    SUM(HighLoanToIncome),
    ROUND(AVG(CASE WHEN HighLoanToIncome = 1 THEN LoanApproved END) * 100, 2)
FROM loan_applications

UNION ALL

SELECT
    'Frequent Credit Inquiries',
    SUM(FrequentCreditInquiries),
    ROUND(AVG(CASE WHEN FrequentCreditInquiries = 1 THEN LoanApproved END) * 100, 2)
FROM loan_applications;

-- Populate risk flags
UPDATE loan_applications
SET
    LowCreditScore = CASE WHEN CreditScore < 600 THEN 1 ELSE 0 END,
    HighDebtRatio = CASE WHEN DebtToIncomeRatio > 0.40 THEN 1 ELSE 0 END,
    HighCreditUtilization = CASE WHEN CreditCardUtilizationRate > 0.30 THEN 1 ELSE 0 END,
    HighLoanToIncome = CASE WHEN LoanToIncomeRatio > 0.50 THEN 1 ELSE 0 END,
    FrequentCreditInquiries = CASE
        WHEN NumberOfCreditInquiries >= 3 THEN 1 ELSE 0
    END;

-- Calculate risk points
UPDATE loan_applications
SET RiskPoints =
    LowCreditScore
    + HighDebtRatio
    + HighCreditUtilization
    + HighLoanToIncome
    + FrequentCreditInquiries;

-- Assign risk category
UPDATE loan_applications
SET RiskCategory =
    CASE
        WHEN RiskPoints BETWEEN 0 AND 1 THEN 'Low Risk'
        WHEN RiskPoints BETWEEN 2 AND 3 THEN 'Medium Risk'
        WHEN RiskPoints BETWEEN 4 AND 5 THEN 'High Risk'
    END;