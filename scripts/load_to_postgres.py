import pandas as pd
from sqlalchemy import create_engine

# Read CSV
df = pd.read_csv("data/processed/blinkit_cleaned.csv")

# PostgreSQL connection
engine = create_engine(
    "postgresql://postgres:yuva1212@localhost:5432/retail_ai"
)

# Load data
df.to_sql(
    "products",
    engine,
    if_exists="append",
    index=False
)

print("✅ Data Imported Successfully!")