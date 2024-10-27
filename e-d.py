from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# Generate a random key
key = os.urandom(16)  # AES key should be either 16, 24, or 32 bytes long

# Function to encrypt the plaintext
def encrypt(plaintext):
    cipher = AES.new(key, AES.MODE_CBC)  # Create a new AES cipher in CBC mode
    iv = cipher.iv  # Initialization vector
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))  # Pad plaintext and encrypt
    return iv + ciphertext  # Return IV + Ciphertext

# Function to decrypt the ciphertext
def decrypt(ciphertext):
    iv = ciphertext[:16]  # Extract the first 16 bytes as IV
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Create a new AES cipher with the IV
    decrypted = unpad(cipher.decrypt(ciphertext[16:]), AES.block_size)  # Decrypt and unpad
    return decrypted.decode()  # Return the decrypted plaintext

# Example usage
if __name__ == "__main__":
    original_text = input("Enter message to encrypt and decrypt: ")
    print("Original:", original_text)
    
    encrypted_text = encrypt(original_text)
    print("Encrypted:", encrypted_text.hex())  # Print encrypted text in hex format

    decrypted_text = decrypt(encrypted_text)
    print("Decrypted:", decrypted_text)
