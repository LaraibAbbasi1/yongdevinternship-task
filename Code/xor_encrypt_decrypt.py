def custom_encrypt(text, key):
    encrypted = ''.join(chr(ord(char) ^ key) for char in text)
    return encrypted

def custom_decrypt(encrypted_text, key):
    decrypted = ''.join(chr(ord(char) ^ key) for char in encrypted_text)
    return decrypted

# Example usage
key = 123  # Simple numeric key
original = "ConfidentialMessage"
encrypted = custom_encrypt(original, key)
decrypted = custom_decrypt(encrypted, key)

print("Original:", original)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
