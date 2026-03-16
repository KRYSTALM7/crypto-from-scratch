"""
RSA Encryption and Decryption from scratch.
Implements key generation, modular inverse, encrypt and decrypt.
"""
import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, phi):
    """Extended Euclidean Algorithm to find modular inverse."""
    d, x1, x2, y1 = 0, 0, 1, 1
    temp_phi = phi
    while e > 0:
        temp1  = temp_phi // e
        temp2  = temp_phi - temp1 * e
        temp_phi, e = e, temp2
        x = x2 - temp1 * x1
        y = d  - temp1 * y1
        x2, x1 = x1, x
        d,  y1 = y1, y
    if temp_phi == 1:
        return d + phi


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


def generate_key_pair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    if p == q:
        raise ValueError('p and q cannot be equal.')

    n   = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    d = multiplicative_inverse(e, phi)
    return (e, n), (d, n)


def encrypt(pk, plaintext):
    key, n = pk
    return [pow(ord(char), key, n) for char in plaintext]


def decrypt(pk, ciphertext):
    key, n = pk
    return ''.join(chr(pow(char, key, n)) for char in ciphertext)


if __name__ == "__main__":
    print("=== RSA Encryptor / Decryptor ===\n")
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))

    public, private = generate_key_pair(p, q)
    print(f"\nPublic key : {public}")
    print(f"Private key: {private}")

    message = input("\nEnter a message to encrypt: ")
    encrypted = encrypt(public, message)
    print("Encrypted  :", ''.join(map(str, encrypted)))

    decrypted = decrypt(private, encrypted)
    print("Decrypted  :", decrypted)