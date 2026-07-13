import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Load Dataset

df = pd.read_csv("data/processed/blinkit_cleaned.csv")

print("Dataset Loaded Successfully!")
print("Dataset Shape:", df.shape)
print(df.head())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Select Features and Target

features = [
    "category",
    "brand",
    "final_price",
    "discount_pct",
    "rating",
    "delivery_time_min",
    "stock",
    "city",
    "offer_type"
]

target = "sold_quantity"

X = df[features]
y = df[target]

# Convert Categorical Columns

X = pd.get_dummies(
    X,
    columns=[
        "category",
        "brand",
        "city",
        "offer_type"
    ],
    drop_first=True
)

print("\nFeature Matrix Shape:", X.shape)

# Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# Train Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel Training Completed!")
# Predictions
predictions = model.predict(X_test)
# Model Evaluation
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n========== MODEL PERFORMANCE ==========")
print(f"Mean Absolute Error : {mae:.2f}")
print(f"Mean Squared Error  : {mse:.2f}")
print(f"R² Score            : {r2:.4f}")

# ------------------------------------
# Feature Importance
# ------------------------------------
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n========== TOP 10 IMPORTANT FEATURES ==========")
print(importance.head(10))

# Save Model

joblib.dump(model, "ml/models/sales_prediction_model.pkl")

print("\nModel saved successfully!")
print("Location: ml/models/sales_prediction_model.pkl")

print(df["sold_quantity"].describe())
joblib.dump(X.columns.tolist(), "ml/models/model_columns.pkl")

print("Model columns saved successfully!")