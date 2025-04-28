import streamlit as st

def show_home():
    st.markdown("""
        <style>
        .landing-container {
            text-align: center;
            padding-top: 10vh;
            padding-bottom: 5vh;
            background-image: url('https://images.unsplash.com/photo-1605902711622-cfb43c44367f');
            background-size: cover;
            background-position: center;
        }
        .title {
            font-size: 50px;
            font-weight: bold;
            color: #4CAF50;
            margin-bottom: 20px;
            text-shadow: 2px 2px 5px #000;
        }
        .subtext {
            font-size: 24px;
            color: #ffffff;
            margin-bottom: 40px;
            text-shadow: 1px 1px 3px #000;
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
            box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
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

    # Centered "Get Started" Button
    col1, col2, col3 = st.columns([2, 1, 2])

    with col2:
        if st.button("🚀 Get Started", use_container_width=True):
            st.session_state.page = "Login"
            st.rerun()
# Little Footer
    st.markdown("""
        <hr style='border: 1px solid #f0f0f0;'>
        <p style='text-align: center; font-size: 12px;'>Secure Fraud Detection System By Ahsan Ziad| 2025</p>
    """, unsafe_allow_html=True)