import streamlit as st
import time
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

    # ---------------- Login Tab ---------------- #
    with tab1:
        with st.container(border=True):
            st.subheader("🔑 Login")
            username = st.text_input("Username", key="login_user_input")
            password = st.text_input("Password", type="password", key="login_pass_input")

            if st.button("Login", use_container_width=True, key="login_button"):
                user = get_user(username)
                if user:
                    if user.get('password') == password:
                        st.success("✅ Login successful!")
                        time.sleep(1)
                        st.session_state.logged_in = True
                        st.session_state.user = username
                        st.session_state.page = "Dashboard"
                        st.rerun()
                    else:
                        st.error("❌ Incorrect password.")
                else:
                    st.error("❌ Username not found.")

    # ---------------- Sign Up Tab ---------------- #
    with tab2:
        with st.container(border=True):
            st.subheader("🆕 Create Account")
            new_user = st.text_input("New Username", key="signup_user_input")
            new_pass = st.text_input("New Password", type="password", key="signup_pass_input")

            if st.button("Sign Up", use_container_width=True, key="signup_button"):
                if not new_user or not new_pass:
                    st.error("❗ Please fill in all fields.")
                elif get_user(new_user):
                    st.warning("⚠️ Username already exists! Try a different one.")
                else:
                    success = add_user(new_user, new_pass)
                    if success:
                        st.success("🎉 Account created successfully! Please login now.")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("❗ Failed to create account.")

    # ---------------- Footer and Back Button ---------------- #
    st.markdown("""
        <div class="footer">Secure Fraud Detection System | 2025</div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    if st.button("⬅️ Back to Home", key="back_button"):
        st.session_state.page = "Home"
        st.rerun()
