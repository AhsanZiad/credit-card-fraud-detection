import streamlit as st

def show_about():
    st.title("ℹ️ About Us")

    st.write("""
    Welcome to Credit Card Fraud Detection System!

    Our mission is to help protect individuals and businesses from financial fraud using AI-powered technology.

    - 📈 Real-time transaction analysis
    - 🛡️ Secure and private predictions
    - 🤝 Trusted by users worldwide

    Developed with ❤️ by Ahsan Ziad | University of Westminster 2025
    """)

    if st.button("⬅️ Back to Dashboard"):
        st.session_state.page = "Dashboard"
        st.rerun()
