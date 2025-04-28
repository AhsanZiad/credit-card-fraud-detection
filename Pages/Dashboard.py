import streamlit as st
import pandas as pd
from firebase_db import get_predictions

def show_dashboard():
    st.markdown("""
        <style>
        .top-buttons {
            display: flex;
            justify-content: flex-end;
            margin-bottom: 20px;
        }
        .top-buttons button {
            margin-left: 10px;
            background-color: #4CAF50;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

    # Buttons at the top
    top1, top2, top3 = st.columns(3)

    with top1:
        if st.button("📤 Upload Transactions"):
            st.session_state.page = "Upload"
            st.rerun()

    with top2:
        if st.button("ℹ️ About Us"):
            st.session_state.page = "About"
            st.rerun()

    with top3:
        if st.button("🔓 Log Out"):
            st.session_state.logged_in = False
            st.session_state.user = ""
            st.session_state.page = "Home"
            st.rerun()

    st.title("📊 Dashboard")
    st.divider()

    st.subheader("📑 Your Previous Predictions")

    user_predictions = get_predictions(st.session_state.user)

    if user_predictions:
        df = pd.DataFrame(user_predictions)
        if not df.empty:
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
    else:
        st.info("ℹ️ No previous uploads found yet.")
