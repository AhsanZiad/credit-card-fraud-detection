import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase app
if not firebase_admin._apps:
    cred = credentials.Certificate("credit-card-fraud-detect-775f4-firebase-adminsdk-fbsvc-e65ebd74c2.json")
    firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

# ------------------ USERS Collection ------------------ #

def add_user(username, password):
    """Add a new user to Firestore."""
    users_ref = db.collection('users')
    users_ref.document(username).set({
        'username': username,
        'password': password
    })

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

# ------------------ PREDICTIONS Collection ------------------ #

def save_prediction(username, time, amount, status):
    """Save a transaction prediction."""
    predictions_ref = db.collection('predictions')
    predictions_ref.add({
        'username': username,
        'time': time,
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
