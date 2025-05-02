import streamlit as st
from firebase_db import add_user, get_user

def show_login():
    st.markdown("""
        <style>
        .title {
            text-align: center;
            color: #4CAF50;
            font-size: 40px;
            margin-top: 30px;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            margin-bottom: 30px;
        }
        .footer {
            text-align: center;
            font-size: 12px;
            margin-top: 50px;
            color: #aaa;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="title">Credit Card Fraud Detection</div>
        <div class="subtitle">Worried about Fraud Transactions? Please Sign In or Create a New Account</div>
        <hr>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🔑 Login", "🆕 Sign Up"])

    with tab1:
        with st.container(border=True):
            st.subheader("🔑 Login")
            username = st.text_input("Username", key="login_user")
            password = st.text_input("Password", type="password", key="login_pass")

            if st.button("Login", use_container_width=True, key="login_btn"):
                user = get_user(username)
                if user:
                    if user.get('password') == password:
                        st.success("✅ Login successful!")
                        st.session_state.logged_in = True
                        st.session_state.user = username
                        st.session_state.page = "Dashboard"
                        st.rerun()
                    else:
                        st.error("❌ Incorrect password.")
                else:
                    st.error("❌ Username not found.")

    with tab2:
        with st.container(border=True):
            st.subheader("🆕 Create Account")
            new_user = st.text_input("New Username", key="new_user")
            new_pass = st.text_input("New Password", type="password", key="new_pass")

            if st.button("Sign Up", use_container_width=True, key="signup_btn"):
                if get_user(new_user):
                    st.warning("⚠️ Username already exists! Try a different one.")
                elif new_user and new_pass:
                    success = add_user(new_user, new_pass)
                    if success:
                        st.success("🎉 Account created successfully! Please login now.")
                        st.rerun()
                    else:
                        st.error("❗ Failed to create account.")
                else:
                    st.error("❗ Please fill in all fields.")

    st.markdown("""
        <div class="footer">Secure Fraud Detection System | 2025</div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    if st.button("⬅️ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()
