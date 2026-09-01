USE loanguard;

-- Employment status analysis
SELECT
    EmploymentStatus,
    COUNT(*) AS Applications,
    ROUND(AVG(AnnualIncome), 2) AS AvgAnnualIncome,
    ROUND(AVG(CreditScore), 2) AS AvgCreditScore,
    ROUND(AVG(RiskScore), 2) AS AvgRiskScore,
    ROUND(AVG(LoanApproved) * 100, 2) AS ApprovalRate
FROM loan_applications
GROUP BY EmploymentStatus
ORDER BY Applications DESC;

-- Home ownership analysis
SELECT
    HomeOwnershipStatus,
    COUNT(*) AS Applications,
    ROUND(AVG(AnnualIncome), 2) AS AvgAnnualIncome,
    ROUND(AVG(LoanAmount), 2) AS AvgLoanAmount,
    ROUND(AVG(CreditScore), 2) AS AvgCreditScore,
    ROUND(AVG(LoanApproved) * 100, 2) AS ApprovalRate
FROM loan_applications
GROUP BY HomeOwnershipStatus
ORDER BY Applications DESC;

-- Education analysis
SELECT
    EducationLevel,
    COUNT(*) AS Applications,
    ROUND(AVG(AnnualIncome), 2) AS AvgAnnualIncome,
    ROUND(AVG(CreditScore), 2) AS AvgCreditScore,
    ROUND(AVG(RiskScore), 2) AS AvgRiskScore,
    ROUND(AVG(LoanApproved) * 100, 2) AS ApprovalRate
FROM loan_applications
GROUP BY EducationLevel
ORDER BY Applications DESC;

-- Marital status analysis
SELECT
    MaritalStatus,
    COUNT(*) AS Applications,
    ROUND(AVG(AnnualIncome), 2) AS AvgAnnualIncome,
    ROUND(AVG(CreditScore), 2) AS AvgCreditScore,
    ROUND(AVG(RiskScore), 2) AS AvgRiskScore,
    ROUND(AVG(LoanApproved) * 100, 2) AS ApprovalRate
FROM loan_applications
GROUP BY MaritalStatus
ORDER BY Applications DESC;