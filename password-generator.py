import streamlit as st
import random
import string
import pyperclip  # Import clipboard functionality

# Custom CSS for Styling
st.markdown(
    """
    <style>
    /* Pure Black Background */
    [data-testid="stAppViewContainer"] {
        background-color: black !important;
    }

    /* Sidebar Black (Optional) */
    [data-testid="stSidebar"] {
        background-color: black !important;
    }

    /* Change Text Color to White */
    [data-testid="stAppViewContainer"] * {
        color: white !important;
    }

    /* Password Box Styling */
    .password-box {
        background-color: #222;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #777;
        text-align: center;
        font-weight: bold;
        font-size: 18px;
        color: white;
    }

    /* Streamlit Button Customization */
    .stButton>button {
        background-color: #D32F2F !important;  /* Dark Red Button */
        color: white !important;
        font-size: 16px;
        padding: 10px;
        border-radius: 10px;
        width: 100%;
        border: none;
    }

    /* Button Hover Effect */
    .stButton>button:hover {
        background-color: #B71C1C !important; /* Even Darker Red */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display Title with Custom Styling
st.markdown('<h1 style="text-align:center; font-size: 50px; font-weight: bold; color: #ff5733;">🔒 Simple Password Generator</h1>', unsafe_allow_html=True)

# Function to Generate Password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Includes uppercase and lowercase letters
    if use_digits:
        characters += string.digits  # Adds numbers (0-9) if selected
    if use_special:
        characters += string.punctuation  # Adds special characters (!@#$%^&* etc.) if selected
    return "".join(random.choice(characters) for _ in range(length))

# User Inputs
length = st.slider("🔢 Select Password Length:", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("🔢 Include Numbers")
use_special = st.checkbox("✨ Include Special Characters")

# Button to Generate Password
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.markdown(f'<div class="password-box">{password}</div>', unsafe_allow_html=True)
    
    # Copy to Clipboard Button
    if st.button("Copy to Clipboard"):
        pyperclip.copy(password)
        st.success("✅ Password copied successfully!")









