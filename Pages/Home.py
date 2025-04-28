import streamlit as st

def show_home():
    st.markdown("""
        <style>
        .landing {
            background-image: url('');
            background-size: cover;
            background-position: center;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
     
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #c3ffad;
            margin-bottom: 20px;
        }
        .subtext {
            font-size: 22px;
            margin-bottom: 30px;
        }
        .stButton>button {
            font-size: 18px;
            padding: 10px 25px;
            margin: 10px;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    
    st.markdown('<div class="title">Credit Card Fraud Detection</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtext">Are you worried about Fraud Transactions?</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Sign In"):
            st.session_state.page = "Login"
    with col2:
        if st.button("Sign Up"):
            st.session_state.page = "Login"  # You can route this to a separate signup page if needed

