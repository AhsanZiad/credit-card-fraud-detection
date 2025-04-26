import streamlit as st

def show_login():
    st.title("🔐 Login / Sign Up")

    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        st.subheader("Login")
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            # 🔒 Replace with real authentication logic
            if username == "admin" and password == "123":
                st.success("Login successful!")
                st.session_state["logged_in"] = True
            else:
                st.error("Invalid credentials.")

    with tab2:
        st.subheader("Create an Account")
        new_user = st.text_input("New Username", key="new_user")
        new_pass = st.text_input("New Password", type="password", key="new_pass")
        if st.button("Sign Up"):
            # ⚠️ This doesn't actually save users (for demo only)
            st.success(f"Account created for {new_user}. Now login from the Login tab.")
