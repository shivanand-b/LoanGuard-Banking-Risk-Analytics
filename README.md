# LoanGuard — Banking Risk & Customer Analytics

LoanGuard is an end-to-end banking loan analytics project built to analyze loan applications, customer profiles, loan portfolios, approval patterns, credit risk, and business trends.

The project combines **Python, MySQL, Power BI, and DAX** to clean, validate, analyze, and visualize loan application data through an interactive **7-page Power BI dashboard**.

---

## 📌 Project Overview

Banks and financial institutions need to understand loan application patterns, customer financial profiles, approval behavior, credit risk, and portfolio performance.

LoanGuard transforms raw loan application data into actionable business insights through data cleaning, validation, exploratory analysis, risk analysis, and interactive Power BI reporting.

The final dashboard provides a centralized view of:

- Loan application performance
- Customer financial characteristics
- Loan portfolio distribution
- Loan approval patterns
- Credit and risk scores
- Interest rate trends
- Loan application trends
- Data quality and completeness

---

## 🎯 Business Objectives

The main objectives of this project are to:

- Analyze overall loan application performance
- Understand customer income and credit profiles
- Identify loan portfolio patterns by purpose
- Analyze loan approval and rejection behavior
- Examine credit score and risk score distributions
- Study loan amount and interest rate trends
- Analyze application trends over time
- Validate important fields for data quality
- Build an interactive dashboard for business decision-making

---

## 🗂️ Dataset

The project uses a structured loan application dataset containing customer, financial, loan, employment, approval, and risk-related information.

### Dataset Size

- **20,000+ loan applications**
- **40 columns after data preparation**

### Important Fields

- Application Date
- Application Year
- Loan Amount
- Loan Duration
- Interest Rate
- Loan Purpose
- Loan Approved
- Monthly Income
- Credit Score
- Risk Score
- Employment Status
- Marital Status
- Debt-related attributes
- Other customer and financial attributes

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data cleaning, validation and analysis |
| Pandas | Data manipulation |
| MySQL | Data storage and SQL analysis |
| Power BI | Interactive dashboard development |
| DAX | KPI and analytical measures |
| Excel/CSV | Dataset handling |

---

## 🔄 Project Workflow

```text
Raw Loan Data
      ↓
Data Cleaning
      ↓
Data Validation
      ↓
Exploratory Data Analysis
      ↓
Risk & Business Analysis
      ↓
MySQL Analysis
      ↓
Power BI Data Model
      ↓
DAX Measures
      ↓
Interactive Dashboard
      ↓
Business Insights

📊 Power BI Dashboard

LoanGuard contains 7 interactive dashboard pages.

1️⃣ Executive Overview

Provides a high-level overview of the loan portfolio and application performance.

Key KPIs
Total Applications
Loan Approval Rate
Total Loan Amount
Average Loan Amount
Average Credit Score
Average Risk Score
Analysis
Applications by Loan Purpose
Overall portfolio performance
Approval performance
Customer credit and risk overview
2️⃣ Customer Analytics

Analyzes customer characteristics and financial profiles.

Key Analysis
Employment Status Distribution
Monthly Income vs Credit Score
Customer financial characteristics
Loan Purpose distribution
Customer risk indicators

This page helps understand how customer characteristics relate to lending behavior.

3️⃣ Loan Analysis

Focuses on loan characteristics and portfolio metrics.

Key KPIs
Total Loan Amount
Average Loan Amount
Average Interest Rate
Approved Loan Amount
Analysis
Average Loan Amount by Loan Duration
Loan portfolio characteristics
Interest rate behavior
Approved loan value
4️⃣ Risk Analysis

Provides a detailed view of credit risk and loan approval patterns.

Key KPIs
Average Risk Score
Average Credit Score
Loan Approval Rate
Analysis
Risk Score Distribution
Risk Score vs Loan Amount
Loan Approval Rate by Risk Level
Risk patterns by Loan Purpose

This page helps identify relationships between customer risk, loan size, and approval behavior.

5️⃣ Business Insights

Provides portfolio-level business insights.

Analysis
Loan Portfolio by Purpose
Loan Amount by Employment Status & Purpose
Loan Portfolio Contribution by Purpose
Application Trends by Loan Purpose

This page helps identify major loan segments and portfolio concentration.

6️⃣ Time Trends

Analyzes how loan activity changes over time.

Analysis
Loan Application Trend Over Time
Total Loan Amount Trend Over Time
Average Interest Rate Trend
Loan Approval Rate Trend

The page helps identify changes in lending activity, loan values, and interest rates across application years.

7️⃣ Data Quality

Validates the completeness of important loan application fields.

Data Quality Checks

The dashboard checks missing values in:

Loan Amount
Monthly Income
Credit Score
Risk Score
Interest Rate
Loan Purpose
Employment Status
Loan Duration
Application Date
Loan Approval Status
Result

The checked fields contain 0 missing values, resulting in:

Overall Data Quality: GOOD

📈 Key Dashboard KPIs
KPI	Value
Total Applications	20K
Total Loan Amount	497.66M
Average Loan Amount	24.88K
Average Credit Score	571.61
Average Risk Score	50.77
Loan Approval Rate  24% 

KPI values are based on the prepared dataset and Power BI calculations.

💡 Key Business Insights

The analysis provides insights into:

Loan application volume across different purposes
Distribution of customers across employment categories
Relationship between monthly income and credit score
Loan portfolio concentration by purpose
Relationship between risk score and loan amount
Approval patterns across different risk levels
Changes in application volume over time
Changes in loan amount and interest rates over time
Data completeness across important banking fields
📐 DAX & KPI Development

Custom DAX measures were created for important business metrics such as:

Total Applications
Loan Approval Rate
Total Loan Amount
Average Loan Amount
Average Credit Score
Average Risk Score
Approved Loan Amount
Average Interest Rate
Missing Value Checks
Overall Data Quality Status

Example:

Approved Loan Amount =
CALCULATE(
    SUM('LoanGuard loan_applications'[LoanAmount]),
    'LoanGuard loan_applications'[LoanApproved] = 1
)
🧹 Data Quality & Validation

The project includes data preparation and validation steps to improve analytical reliability.

Validation Areas
Missing values
Data types
Business-rule validation
Loan approval values
Financial field validation
Risk-related fields
Date and year fields

The Power BI Data Quality page provides an additional validation layer before business insights are presented.

📁 Project Structure
LoanGuard-Banking-Risk-Analytics/
│
├── README.md
│
├── data/
│   └── loan_data.csv
│
├── python/
│   ├── data_audit.py
│   ├── data_cleaning.py
│   ├── data_validation.py
│   ├── eda.py
│   └── risk_analysis.py
│
├── sql/
│   └── loan_analysis.sql
│
├── powerbi/
│   └── LoanGuard_Risk_Intelligence.pbix
│
└── screenshots/
    ├── executive-overview.png
    ├── customer-analytics.png
    ├── loan-analysis.png
    ├── risk-analysis.png
    ├── business-insights.png
    ├── time-trends.png
    └── data-quality.png
🚀 How to Use
1. Clone the repository
git clone https://github.com/shivanand-b/LoanGuard-Banking-Risk-Analytics.git
2. Navigate to the project
cd LoanGuard-Banking-Risk-Analytics
3. Explore the Python analysis

Open the files inside the python/ directory.

4. Explore SQL analysis

Open the SQL scripts inside the sql/ directory.

5. Open the Power BI Dashboard

Open:

powerbi/LoanGuard_Risk_Intelligence.pbix

using Microsoft Power BI Desktop.

🎨 Dashboard Design

The dashboard follows a modern banking analytics design with:

Consistent navigation
KPI cards
Interactive Power BI visuals
Risk-focused analysis
Consistent color palette
Rounded visual containers
Business-oriented page structure
Data quality monitoring

🔮 Future Improvements

Potential future enhancements include:

Machine learning based loan default prediction
Automated credit-risk scoring
Customer segmentation using clustering
Loan default probability prediction
Automated anomaly detection
Real-time banking data integration
Automated email alerts for high-risk applications
Deployment through Power BI Service


👨‍💻 Author

Shivanand Birajdar

Computer Science & Engineering

Interested in Data Analytics, Business Intelligence, Data Science, and Machine Learning.
