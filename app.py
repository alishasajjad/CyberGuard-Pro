import streamlit as st
import base64
import time
import os
from datetime import datetime
from crypto import generate_key, encrypt_text, decrypt_text, encrypt_file, decrypt_file, save_encrypted_file, save_decrypted_file
from cryptography.fernet import InvalidToken
from auth import register_user, verify_user
import streamlit.components.v1 as components

st.set_page_config(
    page_title="🔐 CyberGuard Pro - Advanced Security Suite",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced CSS with cyberpunk theme and advanced animations
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp { 
        background: linear-gradient(135deg, #0F0F23 0%, #1A1A2E 25%, #16213E 50%, #0F3460 75%, #533A7B 100%); 
        color: #FAFAFA; 
    }
    
    .feature-card { 
        background: rgba(26, 26, 46, 0.9); 
        padding: 2.5rem; 
        border-radius: 20px; 
        margin-bottom: 2rem; 
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4); 
        border: 2px solid rgba(78, 205, 196, 0.3);
        backdrop-filter: blur(20px);
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .feature-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.5);
        border-color: #4ECDC4;
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        display: block;
        text-align: center;
        animation: bounce 2s infinite;
    }
    
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .stButton>button { 
        background: linear-gradient(90deg, #FF4E50 0%, #F9D423 100%); 
        color: #FFFFFF; 
        font-weight: 600; 
        border: none; 
        border-radius: 8px; 
        padding: 0.6rem 1.2rem; 
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton>button:hover { 
        transform: translateY(-3px) scale(1.02); 
        box-shadow: 0 7px 14px rgba(255, 78, 80, 0.3); 
    }
    
    .stButton>button:active {
        transform: translateY(1px);
    }
    
    .card { 
        background: rgba(32, 33, 36, 0.8); 
        padding: 2rem; 
        border-radius: 16px; 
        margin-bottom: 2rem; 
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3); 
        border: 1px solid rgba(255, 255, 255, 0.1); 
        backdrop-filter: blur(10px);
        animation: fadeIn 0.6s ease-out;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes glow {
        0% { box-shadow: 0 0 5px rgba(249, 212, 35, 0.5); }
        50% { box-shadow: 0 0 20px rgba(249, 212, 35, 0.8); }
        100% { box-shadow: 0 0 5px rgba(249, 212, 35, 0.5); }
    }
    
    .keybox { 
        background: rgba(22, 23, 26, 0.9); 
        padding: 1.5rem; 
        border-radius: 12px; 
        font-family: 'Courier New', monospace; 
        border: 1px solid rgba(255, 78, 80, 0.3); 
        animation: glow 2s infinite;
    }
    
    textarea { 
        background: rgba(22, 23, 26, 0.9); 
        color: #FAFAFA; 
        border: 1px solid rgba(255, 255, 255, 0.2); 
        border-radius: 8px; 
        padding: 1rem; 
        width: 100%; 
        font-family: 'Courier New', monospace;
        transition: border 0.3s ease;
    }
    
    textarea:focus {
        border: 1px solid rgba(255, 78, 80, 0.5);
        box-shadow: 0 0 10px rgba(255, 78, 80, 0.3);
    }
    
    .stTextInput>div>div>input {
        background: rgba(22, 23, 26, 0.9);
        color: #FAFAFA;
        border: 1px solid rgba(255, 78, 80, 0.3);
        border-radius: 8px;
        padding: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput>div>div>input:focus {
        border: 1px solid rgba(255, 78, 80, 0.7);
        box-shadow: 0 0 10px rgba(255, 78, 80, 0.3);
    }
    
    .stRadio>div {
        background: rgba(32, 33, 36, 0.7);
        padding: 0.8rem;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .stRadio>div:hover {
        border: 1px solid rgba(255, 78, 80, 0.3);
    }
    
    .stFileUploader>div>button {
        background: linear-gradient(90deg, #3A7BD5 0%, #00D2FF 100%);
        color: white;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stFileUploader>div>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0, 210, 255, 0.3);
    }
    
    .main-title {
        text-align: center;
        font-size: 3.2rem;
        margin-bottom: 1.5rem;
        background: linear-gradient(90deg, #FF4E50 0%, #F9D423 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        letter-spacing: -0.5px;
        animation: fadeIn 1s ease-out;
    }
    
    .subtitle {
        text-align: center;
        margin-bottom: 2.5rem;
        opacity: 0.9;
        font-size: 1.2rem;
        font-weight: 300;
        animation: fadeIn 1.2s ease-out;
    }
    
    .mode-container {
        display: flex;
        justify-content: center;
        margin-bottom: 2.5rem;
        animation: fadeIn 1.4s ease-out;
    }
    
    .stSuccess, .stInfo, .stWarning, .stError {
        border-radius: 8px;
        padding: 1rem;
        animation: fadeIn 0.5s ease-out;
    }
    
    .stSuccess {
        background: rgba(25, 135, 84, 0.2);
        border: 1px solid rgba(25, 135, 84, 0.5);
    }
    
    .stWarning {
        background: rgba(255, 193, 7, 0.2);
        border: 1px solid rgba(255, 193, 7, 0.5);
    }
    
    .stError {
        background: rgba(220, 53, 69, 0.2);
        border: 1px solid rgba(220, 53, 69, 0.5);
    }
    
    .stInfo {
        background: rgba(13, 202, 240, 0.2);
        border: 1px solid rgba(13, 202, 240, 0.5);
    }
    
    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #F9D423;
        display: flex;
        align-items: center;
    }
    
    .section-title svg {
        margin-right: 0.5rem;
    }
    
    code {
        border-radius: 8px;
        padding: 1rem !important;
        background-color: rgba(22, 23, 26, 0.9) !important;
        color: #F9D423 !important;
        font-family: 'Courier New', monospace !important;
        font-size: 0.9rem !important;
        border: 1px solid rgba(249, 212, 35, 0.3) !important;
        transition: all 0.3s ease;
    }
    
    code:hover {
        border-color: rgba(249, 212, 35, 0.7) !important;
        box-shadow: 0 0 15px rgba(249, 212, 35, 0.3);
    }
    
    /* Animated background */
    .bg-animation {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        opacity: 0.15;
        background: linear-gradient(125deg, #FF4E50, #F9D423, #3A7BD5, #00D2FF);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Balloon animation */
    .balloon {
        position: fixed;
        width: 30px;
        height: 40px;
        background: #FF4E50;
        border-radius: 50%;
        animation: float 4s ease-in-out infinite;
        opacity: 0;
        z-index: 1000;
    }

    @keyframes float {
        0% {
            transform: translateY(100vh) scale(0);
            opacity: 0;
        }
        50% {
            opacity: 1;
        }
        100% {
            transform: translateY(-100vh) scale(1);
            opacity: 0;
        }
    }

    .auth-card {
        background: rgba(32, 33, 36, 0.9);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }

    .auth-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
    }

    .auth-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
        background: linear-gradient(90deg, #FF4E50 0%, #F9D423 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .auth-input {
        margin-bottom: 1.5rem;
    }

    .auth-button {
        width: 100%;
        padding: 1rem;
        font-size: 1.1rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    </style>
    
    <!-- Animated background div -->
    <div class="bg-animation"></div>
""", unsafe_allow_html=True)

def create_balloons():
    """Create working balloon animation"""
    return """
    <div id="balloon-container">
        <style>
        #balloon-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 9999;
        }
        
        .celebration-balloon {
            position: absolute;
            border-radius: 50%;
            animation: balloonFloat 4s ease-out forwards;
        }
        
        @keyframes balloonFloat {
            0% {
                transform: translateY(100vh) scale(0.5);
                opacity: 0;
            }
            20% {
                opacity: 1;
            }
            80% {
                opacity: 1;
            }
            100% {
                transform: translateY(-20vh) scale(1.2);
                opacity: 0;
            }
        }
        
        .balloon-1 { background: #FF6B6B; width: 30px; height: 35px; left: 10%; animation-delay: 0s; }
        .balloon-2 { background: #4ECDC4; width: 25px; height: 30px; left: 20%; animation-delay: 0.2s; }
        .balloon-3 { background: #45B7D1; width: 35px; height: 40px; left: 30%; animation-delay: 0.4s; }
        .balloon-4 { background: #96CEB4; width: 28px; height: 33px; left: 40%; animation-delay: 0.6s; }
        .balloon-5 { background: #FFEAA7; width: 32px; height: 37px; left: 50%; animation-delay: 0.8s; }
        .balloon-6 { background: #A8E6CF; width: 26px; height: 31px; left: 60%; animation-delay: 1.0s; }
        .balloon-7 { background: #FFD93D; width: 34px; height: 39px; left: 70%; animation-delay: 1.2s; }
        .balloon-8 { background: #6BCF7F; width: 29px; height: 34px; left: 80%; animation-delay: 1.4s; }
        .balloon-9 { background: #4D96FF; width: 31px; height: 36px; left: 90%; animation-delay: 1.6s; }
        .balloon-10 { background: #9B59B6; width: 27px; height: 32px; left: 15%; animation-delay: 1.8s; }
        .balloon-11 { background: #FF6B6B; width: 33px; height: 38px; left: 25%; animation-delay: 2.0s; }
        .balloon-12 { background: #4ECDC4; width: 30px; height: 35px; left: 35%; animation-delay: 2.2s; }
        .balloon-13 { background: #45B7D1; width: 28px; height: 33px; left: 45%; animation-delay: 2.4s; }
        .balloon-14 { background: #96CEB4; width: 32px; height: 37px; left: 55%; animation-delay: 2.6s; }
        .balloon-15 { background: #FFEAA7; width: 29px; height: 34px; left: 65%; animation-delay: 2.8s; }
        </style>
        
        <div class="celebration-balloon balloon-1"></div>
        <div class="celebration-balloon balloon-2"></div>
        <div class="celebration-balloon balloon-3"></div>
        <div class="celebration-balloon balloon-4"></div>
        <div class="celebration-balloon balloon-5"></div>
        <div class="celebration-balloon balloon-6"></div>
        <div class="celebration-balloon balloon-7"></div>
        <div class="celebration-balloon balloon-8"></div>
        <div class="celebration-balloon balloon-9"></div>
        <div class="celebration-balloon balloon-10"></div>
        <div class="celebration-balloon balloon-11"></div>
        <div class="celebration-balloon balloon-12"></div>
        <div class="celebration-balloon balloon-13"></div>
        <div class="celebration-balloon balloon-14"></div>
        <div class="celebration-balloon balloon-15"></div>
    </div>
    
    <script>
    setTimeout(function() {
        var container = document.getElementById('balloon-container');
        if (container) {
            container.remove();
        }
    }, 6000);
    </script>
    """

def login_page():
    """Enhanced Login Page"""
    st.markdown('<h1 style="font-family: Orbitron; text-align: center; font-size: 4rem; color: #FFFFFF; text-shadow: 0 0 20px #4ECDC4, 0 0 40px #4ECDC4, 0 0 60px #4ECDC4; font-weight: 900; margin-bottom: 1rem;">🛡️ CYBERGUARD PRO</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.5rem; color: #4ECDC4; font-weight: 300; letter-spacing: 2px;">Advanced Security & Encryption Suite</p>', unsafe_allow_html=True)
    
    # Initialize form clear state
    if 'clear_signup_form' not in st.session_state:
        st.session_state['clear_signup_form'] = False
    
    # Security stats
    st.markdown("""
    <div style="display: flex; justify-content: space-around; margin: 2rem 0; flex-wrap: wrap;">
        <div style="text-align: center; padding: 1rem; background: rgba(78, 205, 196, 0.1); border-radius: 15px; margin: 0.5rem; min-width: 150px; border: 1px solid rgba(78, 205, 196, 0.3);">
            <div style="font-size: 2rem; font-weight: 700; color: #4ECDC4; font-family: Orbitron;">256</div>
            <div>Bit Encryption</div>
        </div>
        <div style="text-align: center; padding: 1rem; background: rgba(78, 205, 196, 0.1); border-radius: 15px; margin: 0.5rem; min-width: 150px; border: 1px solid rgba(78, 205, 196, 0.3);">
            <div style="font-size: 2rem; font-weight: 700; color: #4ECDC4; font-family: Orbitron;">99.9%</div>
            <div>Security Rate</div>
        </div>
        <div style="text-align: center; padding: 1rem; background: rgba(78, 205, 196, 0.1); border-radius: 15px; margin: 0.5rem; min-width: 150px; border: 1px solid rgba(78, 205, 196, 0.3);">
            <div style="font-size: 2rem; font-weight: 700; color: #4ECDC4; font-family: Orbitron;">24/7</div>
            <div>Protection</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: rgba(15, 15, 35, 0.95); padding: 3rem; border-radius: 25px; box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5); border: 1px solid rgba(78, 205, 196, 0.3); backdrop-filter: blur(20px);">
        <h2 style="text-align: center; color: #4ECDC4; font-family: Orbitron;">🔐 LOGIN</h2>
        """, unsafe_allow_html=True)
        
        username = st.text_input("👤 Username", key="login_username")
        password = st.text_input("🔒 Password", type="password", key="login_password")
        
        if st.button("🚀 LOGIN", key="login_button"):
            if verify_user(username, password):
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.session_state['login_time'] = datetime.now()
                
                # Use Streamlit's built-in balloon animation
                st.balloons()
                
                time.sleep(1)  # Brief pause to see the balloons
                st.rerun()
            else:
                st.error("❌ Invalid credentials!")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: rgba(15, 15, 35, 0.95); padding: 3rem; border-radius: 25px; box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5); border: 1px solid rgba(78, 205, 196, 0.3); backdrop-filter: blur(20px);">
        <h2 style="text-align: center; color: #4ECDC4; font-family: Orbitron;">📝 SIGN UP</h2>
        """, unsafe_allow_html=True)
        
        # Clear form values if signup was successful
        signup_username_value = "" if st.session_state.get('clear_signup_form', False) else None
        signup_password_value = "" if st.session_state.get('clear_signup_form', False) else None
        confirm_password_value = "" if st.session_state.get('clear_signup_form', False) else None
        
        new_username = st.text_input("👤 New Username", key="signup_username", value=signup_username_value)
        new_password = st.text_input("🔒 New Password", type="password", key="signup_password", value=signup_password_value)
        confirm_password = st.text_input("🔒 Confirm Password", type="password", key="confirm_password", value=confirm_password_value)
        
        if st.button("✨ CREATE ACCOUNT", key="signup_button"):
            if new_password != confirm_password:
                st.error("❌ Passwords do not match!")
            elif new_password and len(new_password) < 8:
                st.error("❌ Password must be at least 8 characters!")
            elif register_user(new_username or "", new_password or ""):
                st.balloons()
                st.success("🎉 Account created successfully! Please login.")
                # Set flag to clear form and rerun
                st.session_state['clear_signup_form'] = True
                time.sleep(2)
                st.rerun()
            else:
                st.error("❌ Username already exists!")
        
        # Reset the clear flag after form is displayed
        if st.session_state.get('clear_signup_form', False):
            st.session_state['clear_signup_form'] = False
            
        st.markdown('</div>', unsafe_allow_html=True)

def main_app():
    """Enhanced Main Application"""
    st.markdown('<h1 style="font-family: Orbitron; text-align: center; font-size: 3.5rem; color: #FFFFFF; text-shadow: 0 0 15px #4ECDC4, 0 0 30px #4ECDC4; font-weight: 900; margin-bottom: 1rem;">🛡️ CYBERGUARD PRO</h1>', unsafe_allow_html=True)
    
    # Sidebar with user info and navigation
    with st.sidebar:
        st.markdown(f"### 👋 Welcome, {st.session_state['username']}!")
        if 'login_time' in st.session_state:
            st.write(f"🕐 Login: {st.session_state['login_time'].strftime('%H:%M:%S')}")
        
        st.markdown("---")
        st.markdown("### 🛠️ Security Tools")
        tool = st.selectbox("Select Tool", [
            "🔐 Text Encryption",
            "📁 File Encryption", 
            "🔑 Password Generator",
            "🔄 Base64 Encoder/Decoder"
        ])
        
        st.markdown("---")
        if st.button("🚪 Logout"):
            st.session_state['logged_in'] = False
            st.session_state['username'] = None
            st.rerun()
    
    # Import enhanced features
    from enhanced_features import password_generator, base64_encoder_decoder
    
    # Main content based on selected tool
    if tool == "🔐 Text Encryption":
        text_encryption()
    elif tool == "📁 File Encryption":
        file_encryption()
    elif tool == "🔑 Password Generator":
        password_generator()
    elif tool == "🔄 Base64 Encoder/Decoder":
        base64_encoder_decoder()

def text_encryption():
    """Enhanced Text Encryption"""
    st.markdown("""
    <div style="background: rgba(26, 26, 46, 0.9); padding: 2.5rem; border-radius: 20px; margin-bottom: 2rem; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4); border: 2px solid rgba(78, 205, 196, 0.3); backdrop-filter: blur(20px);">
    <div style="text-align: center; font-size: 3rem; margin-bottom: 1rem;">🔐</div>
    <h2 style="text-align: center; color: #4ECDC4;">Text Encryption/Decryption</h2>
    """, unsafe_allow_html=True)
    
    # Initialize session state for text encryption
    if 'text_encrypted_data' not in st.session_state:
        st.session_state['text_encrypted_data'] = None
    if 'text_encryption_key' not in st.session_state:
        st.session_state['text_encryption_key'] = None
    if 'text_decrypted_data' not in st.session_state:
        st.session_state['text_decrypted_data'] = None
    
    operation = st.radio("🔄 Select Operation", ["🔒 Encrypt", "🔓 Decrypt"], horizontal=True)
    
    if operation == "🔒 Encrypt":
        st.markdown("### 📝 Input Method")
        input_method = st.radio("Choose input method:", ["✍️ Type Text", "📄 Upload .txt File"], horizontal=True)
        
        text_input = ""
        
        if input_method == "✍️ Type Text":
            text_input = st.text_area("📝 Enter text to encrypt", height=150)
        else:
            uploaded_text_file = st.file_uploader("📎 Choose a .txt file to encrypt", type=['txt'])
            if uploaded_text_file is not None:
                try:
                    # Read the uploaded text file
                    text_input = uploaded_text_file.read().decode('utf-8')
                    st.info(f"📄 File loaded: {uploaded_text_file.name} ({len(text_input)} characters)")
                    st.text_area("📝 File content preview:", text_input[:500] + "..." if len(text_input) > 500 else text_input, height=150, disabled=True)
                except UnicodeDecodeError:
                    st.error("❌ Error reading file. Please ensure it's a valid text file with UTF-8 encoding.")
                    text_input = ""
                except Exception as e:
                    st.error(f"❌ Error reading file: {str(e)}")
                    text_input = ""
        
        if st.button("🔒 ENCRYPT TEXT", key="encrypt_text"):
            if text_input:
                with st.spinner("🔄 Encrypting..."):
                    key = generate_key()
                    encrypted_text = encrypt_text(text_input.encode(), key)
                    # Store in session state
                    st.session_state['text_encrypted_data'] = encrypted_text
                    st.session_state['text_encryption_key'] = key
                    
                st.success("✅ Text encrypted successfully!")
        
        # Display results if available in session state
        if st.session_state['text_encrypted_data'] is not None:
            st.text_area("🔒 Encrypted Text", st.session_state['text_encrypted_data'].decode(), height=100)
            st.text_area("🔑 Private Key (SAVE THIS!)", st.session_state['text_encryption_key'].decode(), height=50)
            
            # Download options
            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    "📥 Download Encrypted Text",
                    st.session_state['text_encrypted_data'],
                    "encrypted_text.txt",
                    "text/plain",
                    key="download_encrypted_text"
                )
            with col2:
                st.download_button(
                    "🔑 Download Private Key",
                    st.session_state['text_encryption_key'],
                    "private_key.txt",
                    "text/plain",
                    key="download_private_key"
                )
            
            # Clear results button
            if st.button("🗑️ Clear Results", key="clear_text_results"):
                st.session_state['text_encrypted_data'] = None
                st.session_state['text_encryption_key'] = None
                st.rerun()
        
        if text_input and st.session_state['text_encrypted_data'] is None:
            st.info("👆 Click 'ENCRYPT TEXT' to encrypt your message")
        elif not text_input and input_method == "✍️ Type Text":
            st.error("❌ Please enter text to encrypt!")
            
    else:
        st.markdown("### 📝 Input Method")
        input_method = st.radio("Choose input method:", ["✍️ Type Text", "📄 Upload .txt File"], horizontal=True, key="decrypt_input_method")
        
        encrypted_text = ""
        
        if input_method == "✍️ Type Text":
            encrypted_text = st.text_area("🔒 Enter encrypted text", height=100)
        else:
            uploaded_encrypted_file = st.file_uploader("📎 Choose encrypted .txt file", type=['txt'], key="decrypt_file_upload")
            if uploaded_encrypted_file is not None:
                try:
                    # Read the uploaded encrypted text file
                    encrypted_text = uploaded_encrypted_file.read().decode('utf-8')
                    st.info(f"📄 File loaded: {uploaded_encrypted_file.name}")
                    st.text_area("🔒 Encrypted content preview:", encrypted_text[:300] + "..." if len(encrypted_text) > 300 else encrypted_text, height=100, disabled=True)
                except UnicodeDecodeError:
                    st.error("❌ Error reading file. Please ensure it's a valid text file with UTF-8 encoding.")
                    encrypted_text = ""
                except Exception as e:
                    st.error(f"❌ Error reading file: {str(e)}")
                    encrypted_text = ""
        
        key = st.text_input("🔑 Enter private key")
        
        if st.button("🔓 DECRYPT TEXT", key="decrypt_text"):
            if encrypted_text and key:
                try:
                    with st.spinner("🔄 Decrypting..."):
                        decrypted_text = decrypt_text(encrypted_text.encode(), key.encode())
                        # Store in session state
                        st.session_state['text_decrypted_data'] = decrypted_text
                    st.success("✅ Text decrypted successfully!")
                except InvalidToken:
                    st.error("❌ Invalid private key or corrupted text!")
            else:
                st.error("❌ Please enter both encrypted text and private key!")
        
        # Display decrypted result if available
        if st.session_state['text_decrypted_data'] is not None:
            st.text_area("📝 Decrypted Text", st.session_state['text_decrypted_data'].decode(), height=150)
            
            st.download_button(
                "📥 Download Decrypted Text",
                st.session_state['text_decrypted_data'],
                "decrypted_text.txt",
                "text/plain",
                key="download_decrypted_text"
            )
            
            # Clear results button
            if st.button("🗑️ Clear Results", key="clear_decrypt_results"):
                st.session_state['text_decrypted_data'] = None
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def file_encryption():
    """Enhanced File Encryption"""
    st.markdown("""
    <div style="background: rgba(26, 26, 46, 0.9); padding: 2.5rem; border-radius: 20px; margin-bottom: 2rem; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4); border: 2px solid rgba(78, 205, 196, 0.3); backdrop-filter: blur(20px);">
    <div style="text-align: center; font-size: 3rem; margin-bottom: 1rem;">📁</div>
    <h2 style="text-align: center; color: #4ECDC4;">File Encryption/Decryption</h2>
    """, unsafe_allow_html=True)
    
    # Initialize session state for file encryption
    if 'file_encrypted_data' not in st.session_state:
        st.session_state['file_encrypted_data'] = None
    if 'file_encryption_key' not in st.session_state:
        st.session_state['file_encryption_key'] = None
    if 'file_original_name' not in st.session_state:
        st.session_state['file_original_name'] = None
    if 'file_decrypted_data' not in st.session_state:
        st.session_state['file_decrypted_data'] = None
    if 'file_decrypted_name' not in st.session_state:
        st.session_state['file_decrypted_name'] = None
    
    operation = st.radio("🔄 Select Operation", ["🔒 Encrypt File", "🔓 Decrypt File"], horizontal=True)
    
    if operation == "🔒 Encrypt File":
        uploaded_file = st.file_uploader(
            "📎 Choose file to encrypt", 
            type=['txt', 'pdf', 'docx', 'doc', 'bat', 'py', 'js', 'html', 'css', 'json', 'xml']
        )
        
        if uploaded_file is not None:
            st.info(f"📄 File: {uploaded_file.name} ({uploaded_file.size} bytes)")
            
            if st.button("🔒 ENCRYPT FILE", key="encrypt_file"):
                try:
                    with st.spinner("🔄 Encrypting file..."):
                        # Save uploaded file temporarily
                        temp_path = f"temp_{uploaded_file.name}"
                        with open(temp_path, "wb") as f:
                            f.write(uploaded_file.getvalue())
                        
                        # Encrypt file
                        key = generate_key()
                        encrypted_data, original_filename = encrypt_file(temp_path, key)
                        
                        # Store in session state
                        st.session_state['file_encrypted_data'] = encrypted_data
                        st.session_state['file_encryption_key'] = key
                        st.session_state['file_original_name'] = original_filename
                        
                        # Progress bar
                        progress_bar = st.progress(0)
                        for i in range(100):
                            time.sleep(0.01)
                            progress_bar.progress(i + 1)
                        
                        # Cleanup temp file
                        os.remove(temp_path)
                        
                    st.success("✅ File encrypted successfully!")
                except Exception as e:
                    st.error(f"❌ Error encrypting file: {str(e)}")
        
        # Display results if available in session state
        if st.session_state['file_encrypted_data'] is not None:
            st.text_area("🔑 Private Key (SAVE THIS!)", st.session_state['file_encryption_key'].decode(), height=50)
            
            # Download options
            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    "📥 Download Encrypted File",
                    st.session_state['file_encrypted_data'],
                    f"encrypted_{st.session_state['file_original_name']}.enc",
                    "application/octet-stream",
                    key="download_encrypted_file"
                )
            
            with col2:
                st.download_button(
                    "🔑 Download Private Key",
                    st.session_state['file_encryption_key'],
                    f"private_key_{st.session_state['file_original_name']}.txt",
                    "text/plain",
                    key="download_file_private_key"
                )
            
            # Clear results button
            if st.button("🗑️ Clear Results", key="clear_file_results"):
                st.session_state['file_encrypted_data'] = None
                st.session_state['file_encryption_key'] = None
                st.session_state['file_original_name'] = None
                st.rerun()
                        
    else:
        uploaded_file = st.file_uploader("📎 Choose encrypted file", type=['enc', 'encrypted'])
        key = st.text_input("🔑 Enter private key")
        
        if uploaded_file is not None and key:
            st.info(f"📄 File: {uploaded_file.name} ({uploaded_file.size} bytes)")
            
            if st.button("🔓 DECRYPT FILE", key="decrypt_file"):
                try:
                    with st.spinner("🔄 Decrypting file..."):
                        # Save uploaded file temporarily
                        temp_path = f"temp_{uploaded_file.name}"
                        with open(temp_path, "wb") as f:
                            f.write(uploaded_file.getvalue())
                        
                        # Read encrypted data
                        with open(temp_path, "rb") as f:
                            encrypted_data = f.read()
                        
                        # Decrypt file
                        decrypted_data = decrypt_file(encrypted_data, key.encode(), uploaded_file.name)
                        
                        # Store in session state
                        decrypted_filename = uploaded_file.name.replace('encrypted_', '').replace('.enc', '')
                        st.session_state['file_decrypted_data'] = decrypted_data
                        st.session_state['file_decrypted_name'] = decrypted_filename
                        
                        # Progress bar
                        progress_bar = st.progress(0)
                        for i in range(100):
                            time.sleep(0.01)
                            progress_bar.progress(i + 1)
                        
                        # Cleanup temp file
                        os.remove(temp_path)
                        
                    st.success("✅ File decrypted successfully!")
                except Exception as e:
                    st.error(f"❌ Error decrypting file: {str(e)}")
        
        # Display decrypted result if available
        if st.session_state['file_decrypted_data'] is not None:
            st.download_button(
                "📥 Download Decrypted File",
                st.session_state['file_decrypted_data'],
                st.session_state['file_decrypted_name'],
                "application/octet-stream",
                key="download_decrypted_file"
            )
            
            # Clear results button
            if st.button("🗑️ Clear Decrypted Results", key="clear_file_decrypt_results"):
                st.session_state['file_decrypted_data'] = None
                st.session_state['file_decrypted_name'] = None
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = None

# Main app logic
if not st.session_state['logged_in']:
    login_page()
else:
    main_app()
