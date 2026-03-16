"""
AES Encryption and Decryption using EAX mode (pycryptodome)
Key must be 16, 24, or 32 bytes long.
"""
from Crypto.Cipher import AES

KEY  = b'C&F)H@McQfTjWnZr'  # 16-byte key
DATA = "CSGO Is Better Than Valorant".encode()

# Encrypt
cipher    = AES.new(KEY, AES.MODE_EAX)
nonce     = cipher.nonce
ciphertext = cipher.encrypt(DATA)
print("Cipher text :", ciphertext)

# Decrypt
cipher    = AES.new(KEY, AES.MODE_EAX, nonce=nonce)
plaintext = cipher.decrypt(ciphertext)
print("Plain text  :", plaintext.decode())