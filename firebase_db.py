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

    try:
        cred = credentials.Certificate(firebase_creds)
        firebase_admin.initialize_app(cred)
    except Exception as e:
        print(f"Firebase initialization failed: {e}")

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
    try:
        user_ref = db.collection('users').document(username)
        user = user_ref.get()
        if user.exists:
            return user.to_dict()
        return None
    except Exception as e:
        print(f"Error retrieving user: {e}")
        return None

def get_all_users():
    try:
        users_ref = db.collection('users')
        docs = users_ref.stream()
        return [doc.to_dict() for doc in docs]
    except Exception as e:
        print(f"Error fetching users: {e}")
        return []

# ---------------- PREDICTIONS COLLECTION ---------------- #

def save_prediction(username, time, amount, status):
    try:
        predictions_ref = db.collection('predictions')
        predictions_ref.add({
            'username': username,
            'time': time,
            'amount': amount,
            'status': status
        })
    except Exception as e:
        print(f"Error saving prediction: {e}")

def get_predictions(username):
    try:
        predictions_ref = db.collection('predictions').where('username', '==', username)
        docs = predictions_ref.stream()
        return [doc.to_dict() for doc in docs]
    except Exception as e:
        print(f"Error retrieving predictions: {e}")
        return []

def get_all_predictions():
    try:
        predictions_ref = db.collection('predictions')
        docs = predictions_ref.stream()
        return [doc.to_dict() for doc in docs]
    except Exception as e:
        print(f"Error retrieving all predictions: {e}")
        return []
