import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# ----------------------------
# Load Dataset
# ----------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dataset_path = os.path.join(BASE_DIR, "datasets", "diabetes.csv")

df = pd.read_csv(dataset_path)

print(df.head())

# ----------------------------
# Features & Target
# ----------------------------

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# ----------------------------
# Train/Test Split
# ----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# ----------------------------
# Model
# ----------------------------

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
)

model.fit(X_train, y_train)

# ----------------------------
# Evaluation
# ----------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nAccuracy:", accuracy)

print("\nClassification Report\n")

print(classification_report(y_test, predictions))

# ----------------------------
# Save Model
# ----------------------------

models_dir = os.path.join(BASE_DIR, "models")

os.makedirs(models_dir, exist_ok=True)

model_path = os.path.join(models_dir, "diabetes_model.pkl")

joblib.dump(model, model_path)

print("\nModel saved to:")

print(model_path)