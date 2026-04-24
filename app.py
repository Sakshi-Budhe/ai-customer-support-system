import streamlit as st
import re
from model import predict_category
from llm_reply import generate_reply

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Support System", page_icon="🤖", layout="centered")

# ---------------- CSS (UI IMPROVEMENT) ----------------
st.markdown("""
<style>

/* Background */
body {
    background-color: #f5f7fb;
}

/* Title */
h1 {
    text-align: center;
    color: #4CAF50;
}

/* Text area */
textarea {
    border-radius: 10px !important;
}

/* Button */
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    padding: 10px 25px;
    font-weight: bold;
    width: 100%;
}

.stButton>button:hover {
    background-color: #45a049;
}

/* Result card */
.result-box {
    padding: 18px;
    border-radius: 12px;
    background-color: #ffffff;
    border-left: 6px solid #4CAF50;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
    margin-top: 10px;
}

.small-text {
    color: gray;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1>🤖 AI Support System</h1>", unsafe_allow_html=True)
st.markdown("<p class='small-text'>Smart AI-powered customer support assistant</p>", unsafe_allow_html=True)


# ---------------- GIBBERISH CHECK ----------------
def is_gibberish(text):
    text = text.lower().strip()

    if len(text) < 4:
        return True

    if re.search(r"[^a-z\s]", text):
        return True

    vowels = "aeiou"
    vowel_count = sum(1 for c in text if c in vowels)

    if vowel_count <= 1:
        return True

    return False


# ---------------- INPUT ----------------
ticket = st.text_area("✍️ Enter your issue here", height=120, placeholder="e.g. My payment failed but money deducted")


# ---------------- BUTTON ----------------
if st.button("🚀 Analyze Issue"):

    text = ticket.lower().strip()

    # EMPTY
    if text == "":
        category = "Invalid"
        reply = "⚠️ Please enter your issue"

    # GIBBERISH
    elif is_gibberish(text):
        category = "Invalid"
        reply = "❌ Invalid input. Please describe your issue properly."

    # GREETING
    elif text in ["hi", "hello", "hey"]:
        category = "Greeting"
        reply = generate_reply(category)

    # ML MODEL
    else:
        category, confidence = predict_category(ticket)
        reply = generate_reply(category)

    # ---------------- OUTPUT ----------------
    st.markdown("## 📌 Result")

    st.success(f"Category: {category}")

    st.markdown(f"""
    <div class="result-box">
        🤖 <b>AI Reply:</b><br><br>
        {reply}
    </div>
    """, unsafe_allow_html=True)
