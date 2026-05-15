from cryptography.fernet import Fernet
import os
from typing import Tuple

def generate_key() -> bytes:
    """
    Generate a new Fernet key.
    """
    return Fernet.generate_key()

def encrypt_text(plain_bytes: bytes, key: bytes) -> bytes:
    """
    Encrypt bytes using the provided Fernet key.
    """
    f = Fernet(key)
    return f.encrypt(plain_bytes)

def decrypt_text(cipher_bytes: bytes, key: bytes) -> bytes:
    """
    Decrypt bytes using the provided Fernet key.
    """
    f = Fernet(key)
    return f.decrypt(cipher_bytes)

def encrypt_file(file_path: str, key: bytes) -> Tuple[bytes, str]:
    """
    Encrypt a file and return the encrypted data and original filename.
    """
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
            encrypted_data = encrypt_text(file_data, key)
            return encrypted_data, os.path.basename(file_path)
    except Exception as e:
        raise Exception(f"Error encrypting file: {str(e)}")

def decrypt_file(encrypted_data: bytes, key: bytes, original_filename: str) -> bytes:
    """
    Decrypt file data and return the decrypted bytes.
    """
    try:
        decrypted_data = decrypt_text(encrypted_data, key)
        return decrypted_data
    except Exception as e:
        raise Exception(f"Error decrypting file: {str(e)}")

def save_encrypted_file(encrypted_data: bytes, output_path: str):
    """
    Save encrypted data to a file.
    """
    try:
        with open(output_path, 'wb') as file:
            file.write(encrypted_data)
    except Exception as e:
        raise Exception(f"Error saving encrypted file: {str(e)}")

def save_decrypted_file(decrypted_data: bytes, output_path: str):
    """
    Save decrypted data to a file.
    """
    try:
        with open(output_path, 'wb') as file:
            file.write(decrypted_data)
    except Exception as e:
        raise Exception(f"Error saving decrypted file: {str(e)}")
