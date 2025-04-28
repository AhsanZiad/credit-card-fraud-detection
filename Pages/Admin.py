import streamlit as st
import sqlite3
import pandas as pd

def show_admin():
    st.title("🛡️ Admin Panel - User & Fraud Overview")

    # Only allow admin access
    if st.session_state.get("user") != "admin":
        st.error("🚫 Access denied. Admins Only.")
        return

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    st.subheader("👤 Registered Users")
    cursor.execute("SELECT username FROM users")
    users = cursor.fetchall()
    st.write([u[0] for u in users])

    st.subheader("📑 All Fraud Reports")
    cursor.execute("SELECT username, time, amount, status FROM predictions")
    reports = cursor.fetchall()

    if reports:
        df = pd.DataFrame(reports, columns=["Username", "Time", "Amount", "Status"])
        st.dataframe(df)
    else:
        st.info("No reports found.")

    conn.close()
