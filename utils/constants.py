"""
Application Constants
Early Detection of Chronic Diseases
"""

# ===========================
# Firestore Collections
# ===========================

USERS_COLLECTION = "users"

PREDICTIONS_COLLECTION = "predictions"

MEDICAL_HISTORY_COLLECTION = "medical_history"

APPOINTMENTS_COLLECTION = "appointments"

REPORTS_COLLECTION = "reports"


# ===========================
# User Roles
# ===========================

PATIENT_ROLE = "patient"

DOCTOR_ROLE = "doctor"

ADMIN_ROLE = "admin"


# ===========================
# Disease Names
# ===========================

DIABETES = "diabetes"

HEART_DISEASE = "heart"

KIDNEY_DISEASE = "kidney"

LIVER_DISEASE = "liver"


# ===========================
# Prediction Status
# ===========================

LOW_RISK = "Low"

MEDIUM_RISK = "Medium"

HIGH_RISK = "High"


# ===========================
# API Messages
# ===========================

USER_REGISTERED = "User registered successfully."

LOGIN_SUCCESS = "Login successful."

TOKEN_VERIFIED = "Token verified successfully."

PROFILE_UPDATED = "Profile updated successfully."

FIREBASE_CONNECTED = "Firebase connected successfully."