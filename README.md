# 🔐 CyberGuard Pro - Advanced Information Security Suite

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Security](https://img.shields.io/badge/Security-Advanced-orange.svg)

## 🛡️ Overview

**CyberGuard Pro** is a comprehensive, web-based information security application built with Streamlit. It provides a complete suite of cybersecurity tools including user authentication, advanced encryption/decryption capabilities, password generation, and Base64 encoding/decoding. The application features a modern cyberpunk-themed interface with advanced animations and professional UX design.

## ✨ Key Features

### 🔐 User Authentication System
- **Secure Registration & Login**: SQLite database with PBKDF2 password hashing
- **Salt-based Security**: Each password uses a unique 32-byte salt
- **Session Management**: Persistent login sessions with automatic timeout
- **Form Validation**: Real-time input validation and error handling
- **Celebration Animations**: Streamlit balloon effects on successful login

### 🔒 Advanced Encryption Suite
- **Text Encryption**: 
  - Manual text input encryption/decryption
  - .txt file upload support
  - Fernet symmetric encryption (AES 128)
  - Private key generation and download
- **Multi-Format File Encryption**:
  - PDF, Word Documents (.docx)
  - Code files (Python, JavaScript, HTML, CSS)
  - Data files (JSON, XML)
  - Batch files and executables
  - Secure file upload and download system

### 🛠️ Additional Security Tools
- **Advanced Password Generator**:
  - Customizable length (8-128 characters)
  - Character set selection (uppercase, lowercase, numbers, symbols)
  - Ambiguous character exclusion
  - Custom character support
  - Multiple password generation
  - Real-time strength indicators
- **Base64 Encoder/Decoder**:
  - Text encoding and decoding
  - File download capabilities
  - Error handling for invalid Base64

### 🎨 Professional UI/UX
- **Cyberpunk Theme**: Modern dark theme with neon accents
- **Advanced Animations**: CSS keyframes, hover effects, and transitions
- **Responsive Design**: Optimized for different screen sizes
- **Interactive Elements**: Floating cards, gradient backgrounds
- **Professional Typography**: Orbitron and Poppins font families

## 📁 Project Structure

```
Information_Security/
├── app.py                          # Main application (869 lines)
├── auth.py                         # Authentication module
├── crypto.py                       # Cryptography functions
├── enhanced_features.py            # Additional security tools
├── requirements.txt                # Python dependencies
├── users.db                        # SQLite user database
├── README.md                       # Project documentation
└── documentation_Information_Security.docx  # Additional docs
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd Information_Security
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.32.0 | Web application framework |
| cryptography | 42.0.2 | Encryption/decryption operations |
| python-docx | 1.1.0 | Word document processing |
| PyPDF2 | 3.0.1 | PDF file handling |

## 🔧 Usage Guide

### 1. User Registration & Login
1. **First Time Users**: Click "Create New Account" to register
2. **Existing Users**: Enter credentials and click "LOGIN"
3. **Security**: Passwords are hashed with PBKDF2 and unique salts

### 2. Text Encryption
1. Navigate to "Text Encryption" in the sidebar
2. Choose between manual text input or file upload
3. Enter/upload your content
4. Click "Encrypt Text" to generate encrypted content
5. Download the encrypted text and private key

### 3. File Encryption
1. Select "File Encryption" from the sidebar
2. Upload supported file formats (PDF, DOCX, code files, etc.)
3. Click "Encrypt File" to process
4. Download both encrypted file and private key

### 4. Password Generator
1. Access "Password Generator" tool
2. Customize settings:
   - Length (8-128 characters)
   - Character types (uppercase, lowercase, numbers, symbols)
   - Exclude ambiguous characters
   - Add custom characters
3. Generate single or multiple passwords
4. View real-time strength indicators

### 5. Base64 Encoder/Decoder
1. Select "Base64 Tools" from sidebar
2. Choose "Encode" or "Decode" operation
3. Input text and process
4. Download results as text files

## 🔒 Security Features

### Encryption Standards
- **Algorithm**: Fernet (AES 128 in CBC mode with HMAC-SHA256)
- **Key Generation**: Cryptographically secure random key generation
- **Key Management**: Separate private key download for each operation

### Authentication Security
- **Password Hashing**: PBKDF2-HMAC-SHA256 with 100,000 iterations
- **Salt Generation**: Unique 32-byte salt per password
- **Database**: SQLite with prepared statements (SQL injection protection)
- **Session Management**: Secure session state handling

### File Security
- **Upload Validation**: File type and size validation
- **Secure Processing**: In-memory file processing
- **Clean Downloads**: Proper file naming and MIME type handling

## 🎨 UI/UX Features

### Visual Design
- **Color Scheme**: Cyberpunk-inspired with cyan (#4ECDC4) accents
- **Typography**: Professional font combinations
- **Layout**: Wide layout with expandable sidebar
- **Responsive**: Optimized for various screen sizes

### Animations & Effects
- **Login Success**: Streamlit balloon animation
- **Hover Effects**: Card transformations and glow effects
- **Loading States**: Progress bars and spinners
- **Gradient Backgrounds**: Animated gradient shifts
- **Bounce Animations**: Interactive element feedback

### User Experience
- **Intuitive Navigation**: Clear sidebar menu structure
- **Form Validation**: Real-time input validation
- **Error Handling**: User-friendly error messages
- **Download Management**: Consistent file naming conventions
- **Session Persistence**: Maintains state during downloads

## 🔧 Technical Architecture

### Core Modules

#### `app.py` - Main Application
- Streamlit configuration and page setup
- UI components and styling
- Route handling and navigation
- Session state management
- Integration of all modules

#### `auth.py` - Authentication System
- SQLite database initialization
- User registration and verification
- Password hashing with PBKDF2
- Salt generation and management

#### `crypto.py` - Cryptography Engine
- Fernet key generation
- Text and file encryption/decryption
- Secure file I/O operations
- Error handling for crypto operations

#### `enhanced_features.py` - Additional Tools
- Password generation with customization
- Password strength calculation
- Base64 encoding/decoding
- Utility functions

### Database Schema
```sql
CREATE TABLE users (
    username TEXT PRIMARY KEY,
    password TEXT,  -- PBKDF2 hash (hex)
    salt TEXT       -- 32-byte salt (hex)
);
```

## 🚀 Advanced Features

### Session State Management
- Prevents data loss during file downloads
- Maintains encryption results across page interactions
- Handles multiple download operations
- Form state persistence

### File Processing Pipeline
1. **Upload**: Secure file upload with validation
2. **Processing**: In-memory encryption/decryption
3. **Storage**: Temporary secure storage
4. **Download**: Clean file delivery with proper headers

### Error Handling
- Comprehensive exception handling
- User-friendly error messages
- Graceful degradation
- Input validation and sanitization

## 🔍 Security Considerations

### Best Practices Implemented
- ✅ Secure password hashing (PBKDF2)
- ✅ Unique salt per password
- ✅ SQL injection prevention
- ✅ Input validation and sanitization
- ✅ Secure file handling
- ✅ Session management
- ✅ Error message sanitization

### Recommendations for Production
- Use HTTPS in production environment
- Implement rate limiting for login attempts
- Add password complexity requirements
- Consider implementing 2FA
- Regular security audits
- Database encryption at rest

## 🎯 Future Enhancements

### Planned Features
- [ ] Two-Factor Authentication (2FA)
- [ ] File integrity verification (checksums)
- [ ] Asymmetric encryption (RSA/ECC)
- [ ] Digital signatures
- [ ] Secure file sharing
- [ ] Audit logging
- [ ] Multi-language support
- [ ] Mobile-responsive improvements

### Technical Improvements
- [ ] Database connection pooling
- [ ] Caching mechanisms
- [ ] Performance optimization
- [ ] Unit test coverage
- [ ] CI/CD pipeline
- [ ] Docker containerization

## 🐛 Troubleshooting

### Common Issues

#### Installation Problems
```bash
# If cryptography installation fails:
pip install --upgrade pip
pip install cryptography

# For Windows users:
pip install --only-binary=cryptography cryptography
```

#### Database Issues
```bash
# If users.db is corrupted:
rm users.db
# Restart the application to recreate
```

#### Port Conflicts
```bash
# Run on different port:
streamlit run app.py --server.port 8502
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Alisha Sajjad**
- Project: 4th Semester Information Security
- Institution: [Your Institution Name]
- Contact: [Your Email]

## 🙏 Acknowledgments

- Streamlit team for the excellent web framework
- Cryptography library maintainers
- Open source community for inspiration and resources

## 📊 Project Statistics

- **Total Lines of Code**: ~1,200+
- **Main Application**: 869 lines
- **Modules**: 4 core modules
- **Dependencies**: 4 external packages
- **Features**: 6 major feature sets
- **UI Components**: 15+ interactive elements

---

**⚡ Built with passion for cybersecurity and modern web development**

*Last Updated: [Current Date]* 