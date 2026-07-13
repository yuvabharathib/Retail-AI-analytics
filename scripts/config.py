from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "data" / "raw"
CLEANED_DATA = BASE_DIR / "data" / "cleaned"
PROCESSED_DATA = BASE_DIR / "data" / "processed"

DATASET = RAW_DATA / "blinkit_dataset.csv"