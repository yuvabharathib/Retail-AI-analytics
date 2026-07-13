import subprocess
import sys

print("Downloading latest dataset...")
subprocess.run([sys.executable, "aws/download_from_s3.py"])

print("Cleaning data...")
subprocess.run([sys.executable, "scripts/data_cleaning.py"])

print("Loading into PostgreSQL...")
subprocess.run([sys.executable, "scripts/load_to_postgres.py"])

print("Pipeline completed successfully!")