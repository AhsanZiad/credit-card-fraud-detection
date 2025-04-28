import streamlit as st
import sqlite3
import pandas as pd

def show_dashboard():
    st.title("📊 Dashboard Page")

    # Connect to database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # 🛡️ Create predictions table if it doesn't exist (important fix)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            time REAL,
            amount REAL,
            status TEXT
        )
    ''')

    # 🔓 Log Out Button
    if st.button("🔓 Log Out"):
        st.session_state.logged_in = False
        st.session_state.user = ""
        st.session_state.page = "Home"
        st.rerun()

    # 📬 Contact Button
    if st.button("📬 Contact Us"):
        st.session_state.page = "Contact"
        st.rerun()

    # 🛡️ Admin Panel Button
    if st.session_state.user == "admin":
        if st.button("🛡️ Go to Admin Panel"):
            st.session_state.page = "Admin"
            st.rerun()

    # Fetch user-specific uploads
    query = "SELECT time, amount, status FROM predictions WHERE username=?"
    cursor.execute(query, (st.session_state.user,))
    rows = cursor.fetchall()

    if rows:
        df = pd.DataFrame(rows, columns=["Time", "Amount", "Status"])

        st.subheader("📑 Your Previous Predictions")
        st.dataframe(df)

        frauds = df[df["Status"] == "🚨 Fraud"]
        if not frauds.empty:
            st.warning(f"🚨 {len(frauds)} fraudulent transactions found.")
        else:
            st.success("✅ No frauds detected!")

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Full History", csv, "your_predictions_history.csv", "text/csv")

    else:
        st.info("No previous uploads found.")

    conn.close()
