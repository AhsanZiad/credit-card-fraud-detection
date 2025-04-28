import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase app
cred = credentials.Certificate("firebase_key.json")  # Path to your downloaded JSON
firebase_admin.initialize_app(cred)

# Connect to Firestore
db = firestore.client()

# Function to create a new user
def add_user(username, password):
    user_ref = db.collection('users').document(username)
    user_ref.set({
        'username': username,
        'password': password
    })

# Function to get a user
def get_user(username):
    user_ref = db.collection('users').document(username)
    user = user_ref.get()
    if user.exists:
        return user.to_dict()
    else:
        return None
