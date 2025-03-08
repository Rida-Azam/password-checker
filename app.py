import random
import string
import streamlit as st
import re

# Set page configuration with a lock icon
st.set_page_config(page_title="🔐 Password Strength Checker", page_icon="🔐", layout="centered")

# Apply Custom Styling
st.markdown(
    """
    <style>
        .stTextInput>label {
            font-size: 18px;
            font-weight: bold;
            color: #ffffff;
        }
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            font-size: 18px;
            padding: 10px;
        }
        .password-feedback {
            font-size: 16px;
            font-weight: bold;
            color: #FF4B4B;
        }
        .strong-password {
            color: #4CAF50;
            font-weight: bold;
            font-size: 18px;
        }
        .medium-password {
            color: #FFC107;
            font-weight: bold;
            font-size: 18px;
        }
        .weak-password {
            color: #FF4B4B;
            font-weight: bold;
            font-size: 18px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with Subtitle
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔐 Password Strength Checker 🔐</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #ffffff;'>Check the security level of your password and get suggestions to make it stronger! 🔑</h3>", unsafe_allow_html=True)

# Password Input
password = st.text_input("Enter Your Password:", type="password")

# Initialize feedback and score
feedback = []
score = 0

# Function to Generate Strong Password
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# Check password strength
if password:
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ **Password should be at least 8 characters long.**")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ **Include both uppercase and lowercase letters.**")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ **Add at least one number (0-9).**")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ **Include at least one special character (!@#$%^&*).**")

    # Display Strength Level with Progress Bar
    if score == 4:
        st.markdown("<p class='strong-password'>✅ Your Password is Strong! 🎉</p>", unsafe_allow_html=True)
        st.progress(1.0)
    elif score == 3:
        st.markdown("<p class='medium-password'>⚠️ Your Password is Moderate. Consider improving it.</p>", unsafe_allow_html=True)
        st.progress(0.7)
    else:
        st.markdown("<p class='weak-password'>🚨 Your Password is Weak! Please make it stronger.</p>", unsafe_allow_html=True)
        st.progress(0.3)

    # Display Improvement Suggestions
    if feedback:
        st.markdown("### 🔧 Suggestions to Improve Your Password:")
        for tip in feedback:
            st.markdown(f"- {tip}")

else:
    st.info("🔑 Please enter your password to check its strength.")

# Generate a strong password
if st.button("🔄 Generate Strong Password"):
    strong_password = generate_strong_password()
    st.success(f"💡 Suggested Strong Password: `{strong_password}`")
