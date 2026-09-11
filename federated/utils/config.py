import os

# ======================================================
# Base Directory
# ======================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

PROJECT_DIR = os.path.dirname(BASE_DIR)

# ======================================================
# Dataset Paths
# ======================================================

DATASET_DIR = os.path.join(
    PROJECT_DIR,
    "datasets",
)

DIABETES_DATASET = os.path.join(
    DATASET_DIR,
    "diabetes.csv",
)

HEART_DATASET = os.path.join(
    DATASET_DIR,
    "heart.csv",
)

KIDNEY_DATASET = os.path.join(
    DATASET_DIR,
    "kidney.csv",
)

# ======================================================
# Global Models
# ======================================================

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models",
)

os.makedirs(MODEL_DIR, exist_ok=True)

DIABETES_MODEL = os.path.join(
    MODEL_DIR,
    "diabetes_global.keras",
)

HEART_MODEL = os.path.join(
    MODEL_DIR,
    "heart_global.keras",
)

KIDNEY_MODEL = os.path.join(
    MODEL_DIR,
    "kidney_global.keras",
)

# ======================================================
# Flower Configuration
# ======================================================

SERVER_ADDRESS = "127.0.0.1:8080"

NUM_CLIENTS = 3

NUM_ROUNDS = 3

LOCAL_EPOCHS = 5

BATCH_SIZE = 32