import streamlit as st
import pandas as pd
from firebase_db import get_predictions

def show_dashboard():
    st.markdown("""
        <style>
        .dashboard-title {
            text-align: center;
            color: #4CAF50;
            font-size: 40px;
            margin-top: 30px;
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='dashboard-title'>📊 Dashboard</div>", unsafe_allow_html=True)

    # Log Out Button
    if st.button("🔓 Log Out"):
        st.session_state.logged_in = False
        st.session_state.user = ""
        st.session_state.page = "Home"
        st.rerun()

    # Navigation Buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("📤 Upload Transactions"):
            st.session_state.page = "Upload"
            st.rerun()

    with col2:
        if st.button("📬 Contact Us"):
            st.session_state.page = "Contact"
            st.rerun()

    if st.session_state.user == "admin":
        st.markdown("---")
        if st.button("🛡️ Admin Panel"):
            st.session_state.page = "Admin"
            st.rerun()

    st.divider()

    # 📥 Fetch user-specific predictions from Firebase
    st.subheader("📑 Your Previous Predictions")

    user_predictions = get_predictions(st.session_state.user)

    if user_predictions:
        df = pd.DataFrame(user_predictions)
        st.dataframe(df[["time", "amount", "status"]])

        frauds = df[df["status"] == "🚨 Fraud"]
        if not frauds.empty:
            st.warning(f"🚨 {len(frauds)} fraudulent transactions detected.")
        else:
            st.success("✅ No frauds detected in your transactions.")

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Your Prediction History", csv, "your_predictions.csv", "text/csv")
    else:
        st.info("ℹ️ No previous uploads found yet.")
