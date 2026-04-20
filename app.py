import streamlit as st
from model import predict_category
from llm_reply import generate_reply

st.title("🤖 AI Support System")

ticket = st.text_area("Enter Issue")

if st.button("Analyze"):

    if ticket.strip() == "":
        st.warning("Please enter text")
    else:
        category = predict_category(ticket)
        reply = generate_reply(ticket)

        st.subheader("📌 Category")
        st.success(category)

        st.subheader("🤖 AI Reply")
        st.info(reply)
