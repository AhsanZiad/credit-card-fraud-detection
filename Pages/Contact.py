import streamlit as st

def show_contact():
    st.markdown("""
        <style>
        .contact-title {
            text-align: center;
            color: #4CAF50;
            font-size: 40px;
            margin-top: 30px;
            margin-bottom: 10px;
        }
        .contact-subtitle {
            text-align: center;
            font-size: 18px;
            color: #555;
            margin-bottom: 40px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='contact-title'>📬 Contact Us</div>", unsafe_allow_html=True)
    st.markdown("<div class='contact-subtitle'>We'd love to hear from you! Please fill out the form below.</div>", unsafe_allow_html=True)

    with st.form(key="contact_form", clear_on_submit=True):
        name = st.text_input("👤 Your Name")
        email = st.text_input("✉️ Your Email")
        message = st.text_area("📝 Your Message", height=200)

        submitted = st.form_submit_button("📨 Send Message")

        if submitted:
            if name.strip() and email.strip() and message.strip():
                st.success(f"✅ Thank you, {name}! We've received your message and will get back to you shortly.")
            else:
                st.error("❗ Please fill in all fields before submitting.")
