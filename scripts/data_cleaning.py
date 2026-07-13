from data_loader import load_data
from validator import validate_data
from config import CLEANED_DATA

df = load_data()

validate_data(df)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
for col in df.select_dtypes(include="object"):
    df[col] = df[col].fillna(df[col].mode()[0])

for col in df.select_dtypes(include=["int64", "float64"]):
    df[col] = df[col].fillna(df[col].median())

output = CLEANED_DATA / "blinkit_cleaned.csv"

df.to_csv(output, index=False)

print("\nCleaning Completed")
print(output)