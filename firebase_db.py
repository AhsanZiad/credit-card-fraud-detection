import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase app
if not firebase_admin._apps:
    cred = credentials.Certificate("path/to/your/firebase-service-account.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# --- USERS Collection ---

def add_user(username, password):
    users_ref = db.collection('users')
    users_ref.document(username).set({
        'username': username,
        'password': password
    })

def get_user(username):
    user_ref = db.collection('users').document(username)
    user = user_ref.get()
    if user.exists:
        return user.to_dict()
    else:
        return None

# --- PREDICTIONS Collection ---

def save_prediction(username, time, amount, status):
    predictions_ref = db.collection('predictions')
    predictions_ref.add({
        'username': username,
        'time': time,
        'amount': amount,
        'status': status
    })

def get_predictions(username):
    predictions_ref = db.collection('predictions').where('username', '==', username)
    docs = predictions_ref.stream()
    return [doc.to_dict() for doc in docs]

def get_all_predictions():
    predictions_ref = db.collection('predictions')
    docs = predictions_ref.stream()
    return [doc.to_dict() for doc in docs]

def get_all_users():
    users_ref = db.collection('users')
    docs = users_ref.stream()
    return [doc.to_dict() for doc in docs]
