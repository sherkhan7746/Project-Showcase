import streamlit as st
from send_email import send_email
st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

{raw_message}
From: {user_email}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message, user_email)
        st.info("Email sent successfully!")
