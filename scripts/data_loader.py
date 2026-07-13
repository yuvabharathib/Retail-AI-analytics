import pandas as pd
from config import DATASET

def load_data():
    """
    Load the Blinkit dataset.
    """

    df = pd.read_csv(DATASET)

    print(f"Dataset Loaded Successfully")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    return df