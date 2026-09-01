USE loanguard;

-- Loan purpose analysis
SELECT
    LoanPurpose,
    COUNT(*) AS Applications,
    ROUND(AVG(LoanAmount), 2) AS AvgLoanAmount,
    ROUND(AVG(AnnualIncome), 2) AS AvgAnnualIncome,
    ROUND(AVG(CreditScore), 2) AS AvgCreditScore,
    ROUND(AVG(RiskScore), 2) AS AvgRiskScore,
    ROUND(AVG(LoanApproved) * 100, 2) AS ApprovalRate
FROM loan_applications
GROUP BY LoanPurpose
ORDER BY Applications DESC;

-- Loan duration analysis
SELECT
    LoanDuration,
    COUNT(*) AS Applications,
    ROUND(AVG(LoanAmount), 2) AS AvgLoanAmount,
    ROUND(AVG(InterestRate) * 100, 2) AS AvgInterestRate,
    ROUND(AVG(LoanApproved) * 100, 2) AS ApprovalRate
FROM loan_applications
GROUP BY LoanDuration
ORDER BY LoanDuration;

-- Loan approval analysis
SELECT
    LoanApproved,
    COUNT(*) AS Applications,
    ROUND(AVG(CreditScore), 2) AS AvgCreditScore,
    ROUND(AVG(LoanAmount), 2) AS AvgLoanAmount,
    ROUND(AVG(AnnualIncome), 2) AS AvgAnnualIncome,
    ROUND(AVG(RiskScore), 2) AS AvgRiskScore
FROM loan_applications
GROUP BY LoanApproved;

-- Monthly loan applications
SELECT
    ApplicationYear,
    ApplicationMonth,
    COUNT(*) AS Applications,
    ROUND(AVG(LoanApproved) * 100, 2) AS ApprovalRate
FROM loan_applications
GROUP BY ApplicationYear, ApplicationMonth
ORDER BY ApplicationYear, ApplicationMonth;