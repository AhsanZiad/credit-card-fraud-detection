import streamlit as st

def show_landing():
    st.markdown("""
        <h1 style='text-align: center; color: #4CAF50; font-size: 40px;'>Credit Card Fraud Detection</h1>
        <h3 style='text-align: center;'>Worried about Fraud Transactions?</h3>
        <p style='text-align: center;'>Get Started to Protect Your Transactions</p>
        <hr style='border: 1px solid #f0f0f0;'>
    """, unsafe_allow_html=True)

    # Single Center Button
    st.write("\n")
    col1, col2, col3 = st.columns([2,1,2])
    with col2:
        if st.button("🚀 Get Started", use_container_width=True):
            st.session_state.page = "Login"
            st.experimental_rerun()

    st.markdown("""
        <hr style='border: 1px solid #f0f0f0;'>
        <p style='text-align: center; font-size: 12px;'>Secure Fraud Detection System | 2025</p>
    """, unsafe_allow_html=True)

# Note: In your Main.py, initially set st.session_state.page = "Landing"
# And add a case: if page == "Landing": from Pages.Landing import show_landing
