import streamlit as st
import secrets
import string
import base64

def password_generator():
    """Advanced Password Generator"""
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown('<span class="feature-icon">🔐</span>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #4ECDC4;">Password Generator</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        length = st.slider("Password Length", 8, 128, 16)
        include_uppercase = st.checkbox("Include Uppercase", True)
        include_lowercase = st.checkbox("Include Lowercase", True)
        include_numbers = st.checkbox("Include Numbers", True)
        include_symbols = st.checkbox("Include Symbols", True)
    
    with col2:
        exclude_ambiguous = st.checkbox("Exclude Ambiguous Characters (0, O, l, I)")
        custom_chars = st.text_input("Custom Characters (optional)")
        password_count = st.number_input("Number of Passwords", 1, 10, 1)
    
    if st.button("Generate Passwords", key="gen_pass"):
        chars = ""
        if include_lowercase:
            chars += string.ascii_lowercase
        if include_uppercase:
            chars += string.ascii_uppercase
        if include_numbers:
            chars += string.digits
        if include_symbols:
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if custom_chars:
            chars += custom_chars
        
        if exclude_ambiguous:
            chars = chars.replace('0', '').replace('O', '').replace('l', '').replace('I', '')
        
        if chars:
            passwords = []
            for _ in range(password_count):
                password = ''.join(secrets.choice(chars) for _ in range(length))
                passwords.append(password)
            
            st.success("Passwords generated successfully!")
            for i, pwd in enumerate(passwords, 1):
                st.code(f"Password {i}: {pwd}")
                
                # Password strength indicator
                strength = calculate_password_strength(pwd)
                st.progress(strength / 100)
                st.write(f"Strength: {get_strength_label(strength)}")
        else:
            st.error("Please select at least one character type!")
    
    st.markdown('</div>', unsafe_allow_html=True)

def calculate_password_strength(password):
    """Calculate password strength score"""
    score = 0
    if len(password) >= 8:
        score += 20
    if len(password) >= 12:
        score += 20
    if any(c.islower() for c in password):
        score += 15
    if any(c.isupper() for c in password):
        score += 15
    if any(c.isdigit() for c in password):
        score += 15
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 15
    return min(score, 100)

def get_strength_label(score):
    """Get password strength label"""
    if score < 30:
        return "🔴 Weak"
    elif score < 60:
        return "🟡 Medium"
    elif score < 80:
        return "🟢 Strong"
    else:
        return "🟢 Very Strong"





def base64_encoder_decoder():
    """Base64 Encoder/Decoder"""
    st.markdown('<div class="feature-card">', unsafe_allow_html=True)
    st.markdown('<span class="feature-icon">🔄</span>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #4ECDC4;">Base64 Encoder/Decoder</h2>', unsafe_allow_html=True)
    
    operation = st.radio("Select Operation", ["Encode", "Decode"], horizontal=True)
    
    if operation == "Encode":
        text_to_encode = st.text_area("Enter text to encode")
        if st.button("Encode to Base64", key="encode_b64"):
            if text_to_encode:
                encoded = base64.b64encode(text_to_encode.encode()).decode()
                st.success("Text encoded successfully!")
                st.code(encoded)
                st.download_button(
                    label="Download Encoded Text",
                    data=encoded,
                    file_name="encoded_text.txt",
                    mime="text/plain"
                )
            else:
                st.error("Please enter text to encode!")
    else:
        text_to_decode = st.text_area("Enter Base64 text to decode")
        if st.button("Decode from Base64", key="decode_b64"):
            if text_to_decode:
                try:
                    decoded = base64.b64decode(text_to_decode).decode()
                    st.success("Text decoded successfully!")
                    st.code(decoded)
                    st.download_button(
                        label="Download Decoded Text",
                        data=decoded,
                        file_name="decoded_text.txt",
                        mime="text/plain"
                    )
                except Exception as e:
                    st.error("Invalid Base64 text!")
            else:
                st.error("Please enter Base64 text to decode!")
    
    st.markdown('</div>', unsafe_allow_html=True) 