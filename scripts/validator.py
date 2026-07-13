def validate_data(df):

    print("\nChecking Dataset...")

    print(f"Shape : {df.shape}")

    print("\nMissing Values")

    print(df.isnull().sum())

    print("\nDuplicate Rows")

    print(df.duplicated().sum())