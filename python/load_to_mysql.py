import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
from urllib.parse import quote_plus

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "cleaned" / "loan_cleaned.csv"

df = pd.read_csv(DATA_PATH)

print("LoanGuard - MySQL Data Load")
print("-" * 35)

print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns):,}")

password = input("Enter MySQL password: ")

encoded_password = quote_plus(password)

engine = create_engine(
    f"mysql+pymysql://root:{encoded_password}@localhost:3306/loanguard"
)

df.to_sql(
    "loan_applications",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=1000
)

print("\nData loaded successfully.")