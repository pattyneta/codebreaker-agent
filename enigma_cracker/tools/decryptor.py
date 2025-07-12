def decrypt_message(encrypted_message: str, key: int) -> str:
    """Decrypts a message using a simple letter-shift cipher."""
    decrypted = ""
    for char in encrypted_message.upper():
        if 'A' <= char <= 'Z':
            decrypted_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
            decrypted += decrypted_char
        else:
            decrypted += char
    return decrypted