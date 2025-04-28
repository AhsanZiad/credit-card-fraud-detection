import streamlit as st
import sqlite3
import pandas as pd

def show_admin():
    st.markdown("""
        <style>
        .admin-title {
            text-align: center;
            color: #4CAF50;
            font-size: 40px;
            margin-top: 30px;
            margin-bottom: 10px;
        }
        .admin-subtitle {
            font-size: 24px;
            margin-top: 30px;
            color: #555;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='admin-title'>🛡️ Admin Panel - User & Fraud Overview</div>", unsafe_allow_html=True)

    # Only allow admin access
    if st.session_state.get("user") != "admin":
        st.error("🚫 Access Denied: Admins Only.")
        return

    # Connect to database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # 📋 Show Registered Users
    st.markdown("<div class='admin-subtitle'>👤 Registered Users</div>", unsafe_allow_html=True)
    cursor.execute("SELECT username FROM users")
    users = cursor.fetchall()

    if users:
        user_list = [u[0] for u in users]
        st.success(f"✅ Total Users: {len(user_list)}")
        st.dataframe(pd.DataFrame(user_list, columns=["Username"]))
    else:
        st.info("ℹ️ No registered users found.")

    st.markdown("<div class='admin-subtitle'>📑 All Fraud Reports</div>", unsafe_allow_html=True)

    # 📑 Show Fraud Reports
    cursor.execute("SELECT username, time, amount, status FROM predictions")
    reports = cursor.fetchall()

    if reports:
        df = pd.DataFrame(reports, columns=["Username", "Time", "Amount", "Status"])
        st.dataframe(df)

        # 📥 Download Button for Admin
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Full Fraud Reports", csv, "fraud_reports.csv", "text/csv")
    else:
        st.info("ℹ️ No fraud reports available.")

    # Close database
    conn.close()
