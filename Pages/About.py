import streamlit as st

def show_about():
    st.markdown("""
        <style>
        .about-title {
            text-align: center;
            color: #4CAF50;
            font-size: 40px;
            margin-top: 30px;
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='about-title'>ℹ️ About Us</div>", unsafe_allow_html=True)

    st.write("""
    Welcome to the **Credit Card Fraud Detection System**! 

    Our mission is to protect individuals and businesses from financial fraud using AI-powered technology.

    **Key Features:**
    - 📈 Real-time transaction analysis
    - 🛡️ Secure and private predictions


    **Developed with ❤️ by Ahsan Ziad**  
    University of Westminster | 2025
    """)

    st.markdown("---")

    if st.button("⬅️ Back to Dashboard"):
        st.session_state.page = "Dashboard"
        st.rerun()
