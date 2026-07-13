import pandas as pd
import joblib

# Load model
model = joblib.load("ml/models/sales_prediction_model.pkl")

# Load training columns
model_columns = joblib.load("ml/models/model_columns.pkl")

# New product
sample = {
    "category": "Snacks",
    "brand": "Lay's",
    "final_price": 85,
    "discount_pct": 10,
    "rating": 4.5,
    "delivery_time_min": 25,
    "stock": 300,
    "city": "Chennai",
    "offer_type": "FlatDiscount"
}

# Convert to DataFrame
sample_df = pd.DataFrame([sample])

# One-hot encode
sample_df = pd.get_dummies(sample_df)

# Add missing columns
for col in model_columns:
    if col not in sample_df.columns:
        sample_df[col] = 0

# Keep the same column order
sample_df = sample_df[model_columns]

# Predict
prediction = model.predict(sample_df)

print(f"Predicted Sold Quantity: {prediction[0]:.2f}")