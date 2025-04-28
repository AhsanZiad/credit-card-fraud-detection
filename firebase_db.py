import requests
import json
import streamlit as st

# Read credentials from Streamlit secrets
FIREBASE_API_KEY = st.secrets["firebase"]["api_key"]
FIREBASE_PROJECT_ID = st.secrets["firebase"]["project_id"]

# Firebase REST API URLs
FIREBASE_SIGNUP_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={FIREBASE_API_KEY}"
FIRESTORE_BASE_URL = f"https://firestore.googleapis.com/v1/projects/{FIREBASE_PROJECT_ID}/databases/(default)/documents"

# --- USERS Collection ---

def add_user(username, password):
    """Add a new user into Firestore."""
    user_data = {
        "fields": {
            "username": {"stringValue": username},
            "password": {"stringValue": password}
        }
    }
    url = f"{FIRESTORE_BASE_URL}/users/{username}"
    response = requests.patch(url, json=user_data)

    if response.status_code == 200:
        return True
    else:
        st.error(f"Failed to create user: {response.text}")
        return False

def get_user(username):
    """Get user data by username from Firestore."""
    url = f"{FIRESTORE_BASE_URL}/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        doc = response.json()
        return {
            "username": doc["fields"]["username"]["stringValue"],
            "password": doc["fields"]["password"]["stringValue"]
        }
    else:
        return None

def get_all_users():
    """Fetch all users from Firestore."""
    url = f"{FIRESTORE_BASE_URL}/users"
    response = requests.get(url)

    users = []
    if response.status_code == 200:
        docs = response.json().get("documents", [])
        for doc in docs:
            fields = doc["fields"]
            users.append({
                "username": fields["username"]["stringValue"],
                "password": fields["password"]["stringValue"]
            })
    return users

# --- PREDICTIONS Collection ---

def save_prediction(username, time, amount, status):
    """Save a fraud prediction into Firestore."""
    prediction_data = {
        "fields": {
            "username": {"stringValue": username},
            "time": {"doubleValue": float(time)},
            "amount": {"doubleValue": float(amount)},
            "status": {"stringValue": status}
        }
    }
    url = f"{FIRESTORE_BASE_URL}/predictions"
    requests.post(url, json=prediction_data)

def get_predictions(username):
    """Get all predictions for a specific user."""
    query = {
        "structuredQuery": {
            "from": [{"collectionId": "predictions"}],
            "where": {
                "fieldFilter": {
                    "field": {"fieldPath": "username"},
                    "op": "EQUAL",
                    "value": {"stringValue": username}
                }
            }
        }
    }
    url = f"https://firestore.googleapis.com/v1/projects/{FIREBASE_PROJECT_ID}/databases/(default)/documents:runQuery"
    response = requests.post(url, json=query)

    predictions = []
    if response.status_code == 200:
        for doc in response.json():
            if 'document' in doc:
                fields = doc['document']['fields']
                predictions.append({
                    "time": fields["time"]["doubleValue"],
                    "amount": fields["amount"]["doubleValue"],
                    "status": fields["status"]["stringValue"]
                })
    return predictions

def get_all_predictions():
    """Fetch all predictions for Admin."""
    url = f"{FIRESTORE_BASE_URL}/predictions"
    response = requests.get(url)

    predictions = []
    if response.status_code == 200:
        docs = response.json().get("documents", [])
        for doc in docs:
            fields = doc["fields"]
            predictions.append({
                "username": fields["username"]["stringValue"],
                "time": fields["time"]["doubleValue"],
                "amount": fields["amount"]["doubleValue"],
                "status": fields["status"]["stringValue"]
            })
    return predictions
