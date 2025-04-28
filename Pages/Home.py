import streamlit as st

def show_home():
    st.markdown("""
        <style>
        .landing-container {
            text-align: center;
            padding-top: 10vh;
            padding-bottom: 5vh;
        }
        .title {
            font-size: 50px;
            font-weight: bold;
            color: #4CAF50;
            margin-bottom: 20px;
        }
        .subtext {
            font-size: 24px;
            color: #555;
            margin-bottom: 40px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 30px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 20px;
            padding: 12px 30px;
            border-radius: 8px;
            border: none;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        </style>
    """, unsafe_allow_html=True)

    # Landing content
    st.markdown("""
        <div class="landing-container">
            <div class="title">Credit Card Fraud Detection</div>
            <div class="subtext">Are you worried about Fraud Transactions?</div>
        </div>
    """, unsafe_allow_html=True)

    # Buttons
    col1, col2, col3 = st.columns([2,1,2])

    with col1:
        pass  # empty space
    with col2:
        if st.button("🚀 Get Started", use_container_width=True):
            st.session_state.page = "Login"
            st.rerun()
    with col3:
        pass  # empty space
