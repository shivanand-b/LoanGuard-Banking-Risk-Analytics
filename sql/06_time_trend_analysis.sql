SELECT
    ApplicationYear,
    ApplicationMonth,
    COUNT(*) AS Applications,
    SUM(LoanApproved) AS ApprovedLoans,
    ROUND(AVG(LoanApproved) * 100, 2) AS ApprovalRate,
    ROUND(AVG(LoanAmount), 2) AS AvgLoanAmount,
    ROUND(AVG(RiskScore), 2) AS AvgRiskScore
FROM loan_applications
GROUP BY
    ApplicationYear,
    ApplicationMonth
ORDER BY
    ApplicationYear,
    ApplicationMonth;


SELECT
    ApplicationYear,
    COUNT(*) AS Applications,
    SUM(LoanApproved) AS ApprovedLoans,
    ROUND(SUM(LoanApproved) * 100.0 / COUNT(*), 2) AS ApprovalRate,
    ROUND(AVG(LoanAmount), 2) AS AvgLoanAmount,
    ROUND(AVG(Age), 2) AS AvgAge
FROM loan_applications
GROUP BY ApplicationYear
ORDER BY ApplicationYear;    