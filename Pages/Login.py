import streamlit as st
from db import create_users_table, add_user, get_user

def show_login():
    st.title("🔐 Login / Sign Up")

    # Ensure the user table exists
    create_users_table()

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        st.subheader("Login")
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        
        if st.button("Login"):
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
        st.subheader("Create an Account")
        new_user = st.text_input("New Username", key="new_user")
        new_pass = st.text_input("New Password", type="password", key="new_pass")
        
        if st.button("Sign Up"):
            if get_user(new_user):
                st.warning("⚠️ Username already exists! Try a different one.")
            elif new_user and new_pass:
                add_user(new_user, new_pass)
                st.success("🎉 Account created successfully! Please login now.")
            else:
                st.error("Please fill in both fields.")
