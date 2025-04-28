import streamlit as st

# Set app layout
st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Home"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = ""

# Routing logic
def route():
    if st.session_state.page == "Home":
        from Pages.Home import show_home
        show_home()

    elif st.session_state.page == "Login":
        from Pages.Login import show_login
        show_login()

    elif st.session_state.page == "Upload":
        from Pages.Upload import show_upload
        from joblib import load

        # Load the trained ML model
        model = load("credit_card_fraud_detection.pkl")
        show_upload(model)

    elif st.session_state.page == "Dashboard":
        from Pages.Dashboard import show_dashboard
        show_dashboard()

    elif st.session_state.page == "Contact":
        from Pages.Contact import show_contact
        show_contact()

    elif st.session_state.page == "Admin":
        from Pages.Admin import show_admin
        show_admin()

# Run the router
if __name__ == "__main__":
    route()
