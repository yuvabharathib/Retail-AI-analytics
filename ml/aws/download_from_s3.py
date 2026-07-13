import boto3

BUCKET_NAME = "yuva-retail-ai-analytics"
S3_FILE = "blinkit_cleaned.csv"
LOCAL_FILE = "data/processed/blinkit_cleaned.csv"

s3 = boto3.client("s3")

s3.download_file(BUCKET_NAME, S3_FILE, LOCAL_FILE)

print("✅ Latest dataset downloaded from S3")