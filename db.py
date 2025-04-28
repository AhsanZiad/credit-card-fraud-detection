import sqlite3

# 🔵 Function to create 'users' table if it doesn't exist
def create_users_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

# 🔵 Function to create 'predictions' table if it doesn't exist
def create_predictions_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            time REAL,
            amount REAL,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

# 🔵 Function to add a new user
def add_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

# 🔵 Function to get user details
def get_user(username):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = c.fetchone()
    conn.close()
    return user

# 🏁 If running this file directly, create tables
if __name__ == "__main__":
    create_users_table()
    create_predictions_table()
    print("✅ users.db created with users and predictions tables!")
