import sqlite3
import hashlib
import os
from typing import Optional, Tuple

# Resolve database path relative to project root (works after folder moves)
_PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
_DB_PATH = os.path.join(_PROJECT_DIR, 'users.db')

def init_db():
    """Initialize the SQLite database with users table"""
    conn = sqlite3.connect(_DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT, salt TEXT)''')
    conn.commit()
    conn.close()

def hash_password(password: str, salt: Optional[bytes] = None) -> Tuple[bytes, bytes]:
    """Hash a password with a salt"""
    if salt is None:
        salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )
    return key, salt

def register_user(username: str, password: str) -> bool:
    """Register a new user"""
    try:
        conn = sqlite3.connect(_DB_PATH)
        c = conn.cursor()
        
        # Check if username already exists
        c.execute('SELECT username FROM users WHERE username = ?', (username,))
        if c.fetchone():
            return False
        
        # Hash password and store user
        key, salt = hash_password(password)
        c.execute('INSERT INTO users (username, password, salt) VALUES (?, ?, ?)',
                 (username, key.hex(), salt.hex()))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error registering user: {e}")
        return False
    finally:
        conn.close()

def verify_user(username: str, password: str) -> bool:
    """Verify user credentials"""
    try:
        conn = sqlite3.connect(_DB_PATH)
        c = conn.cursor()
        
        # Get user's stored password and salt
        c.execute('SELECT password, salt FROM users WHERE username = ?', (username,))
        result = c.fetchone()
        
        if not result:
            return False
            
        stored_key, stored_salt = result
        stored_key = bytes.fromhex(stored_key)
        stored_salt = bytes.fromhex(stored_salt)
        
        # Verify password
        key, _ = hash_password(password, stored_salt)
        return key == stored_key
    except Exception as e:
        print(f"Error verifying user: {e}")
        return False
    finally:
        conn.close()

# Initialize database when module is imported
init_db() 