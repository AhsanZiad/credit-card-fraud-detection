import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase app
if not firebase_admin._apps:
    firebase_creds = {
        "type": st.secrets["firebase"]["type"],
        "project_id": st.secrets["firebase"]["project_id"],
        "private_key_id": st.secrets["firebase"]["private_key_id"],
        "private_key": st.secrets["firebase"]["private_key"].replace("\\n", "\n"),
        "client_email": st.secrets["firebase"]["client_email"],
        "client_id": st.secrets["firebase"]["client_id"],
        "auth_uri": st.secrets["firebase"]["auth_uri"],
        "token_uri": st.secrets["firebase"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"]
    }

    cred = credentials.Certificate(firebase_creds)
    firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# ---------------- USERS COLLECTION ---------------- #

def add_user(username, password):
    try:
        users_ref = db.collection('users')
        users_ref.document(username).set({
            'username': username,
            'password': password
        })
        return True
    except Exception as e:
        print(f"Error adding user: {e}")
        return False


def get_user(username):
    """Get user data by username."""
    user_ref = db.collection('users').document(username)
    user = user_ref.get()
    if user.exists:
        return user.to_dict()
    else:
        return None

def get_all_users():
    """Fetch all users."""
    users_ref = db.collection('users')
    docs = users_ref.stream()
    return [doc.to_dict() for doc in docs]

# ---------------- PREDICTIONS COLLECTION ---------------- #

def save_prediction(username, time, amount, status):
    """Save a transaction prediction."""
    predictions_ref = db.collection('predictions')
    predictions_ref.add({
        'username': username,
        'time': time,         # 🛠 fixed quotation
        'amount': amount,
        'status': status
    })

def get_predictions(username):
    """Get all predictions for a specific user."""
    predictions_ref = db.collection('predictions').where('username', '==', username)
    docs = predictions_ref.stream()
    return [doc.to_dict() for doc in docs]

def get_all_predictions():
    """Fetch all predictions (for Admin panel)."""
    predictions_ref = db.collection('predictions')
    docs = predictions_ref.stream()
    return [doc.to_dict() for doc in docs]
