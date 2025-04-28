import streamlit as st
import pandas as pd
from firebase_db import get_predictions

def show_dashboard():
    st.markdown("""
        <style>
        .navbar {
            display: flex;
            justify-content: flex-end;
            gap: 10px;
            margin-bottom: 20px;
        }
        .navbar button {
            background-color: #4CAF50;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
        }
        .navbar button:hover {
            background-color: #45a049;
        }
        .dashboard-title {
            text-align: center;
            color: #4CAF50;
            font-size: 40px;
            margin-top: 10px;
            margin-bottom: 30px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Navbar Top Right
    st.markdown("""
        <div class="navbar">
            <form action="?nav=upload" method="post"><button type="submit">Upload Transactions</button></form>
            <form action="?nav=about" method="post"><button type="submit">About Us</button></form>
            <form action="?nav=logout" method="post"><button type="submit">Log Out</button></form>
        </div>
    """, unsafe_allow_html=True)

    # Navigation Button Handling
    nav = st.query_params.get("nav")

    if nav == ["upload"]:
        st.session_state.page = "Upload"
        st.experimental_rerun()
    if nav == ["about"]:
        st.session_state.page = "About"
        st.experimental_rerun()
    if nav == ["logout"]:
        st.session_state.logged_in = False
        st.session_state.user = ""
        st.session_state.page = "Home"
        st.experimental_rerun()

    # Dashboard Title
    st.markdown("<div class='dashboard-title'>📊 Dashboard</div>", unsafe_allow_html=True)
    st.divider()

    # Predictions Section
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

