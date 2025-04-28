import streamlit as st
from db import create_users_table, add_user, get_user

def show_login():
    # Set page title without gray placeholder
    st.markdown("""
        <h1 style='text-align: center; color: #4CAF50; font-size: 40px;'>Credit Card Fraud Detection</h1>
        <h3 style='text-align: center;'>Worried about Fraud Transactions?</h3>
        <p style='text-align: center;'>Please Sign In or Create a New Account</p>
        <hr style='border: 1px solid #f0f0f0;'>
    """, unsafe_allow_html=True)

    # Ensure the user table exists
    create_users_table()

    # Center the tabs
    tab1, tab2 = st.columns(2)

    with tab1:
        with st.container(border=True):
            st.subheader("🔑 Login")
            username = st.text_input("Username", key="login_user")
            password = st.text_input("Password", type="password", key="login_pass")
            
            if st.button("Login", use_container_width=True):
                user = get_user(username)
                if user and user[1] == password:
                    st.success("✅ Login successful")
                    st.session_state.logged_in = True
                    st.session_state.user = username
                    st.session_state.page = "Dashboard"  # 🚀 Move to Dashboard after login
                    st.experimental_rerun()  # Force rerun to change the page
                else:
                    st.error("❌ Invalid username or password.")

    with tab2:
        with st.container(border=True):
            st.subheader("🆕 Create Account")
            new_user = st.text_input("New Username", key="new_user")
            new_pass = st.text_input("New Password", type="password", key="new_pass")

            if st.button("Sign Up", use_container_width=True):
                if get_user(new_user):
                    st.warning("⚠️ Username already exists! Try a different one.")
                elif new_user and new_pass:
                    add_user(new_user, new_pass)
                    st.success("🎉 Account created successfully! Please login now.")
                else:
                    st.error("Please fill in both fields.")

    # Little Footer
    st.markdown("""
        <hr style='border: 1px solid #f0f0f0;'>
        <p style='text-align: center; font-size: 12px;'>Secure Fraud Detection System | 2025</p>
    """, unsafe_allow_html=True)
