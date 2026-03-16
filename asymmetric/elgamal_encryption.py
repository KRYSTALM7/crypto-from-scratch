"""
ElGamal Asymmetric Encryption from scratch.
Based on discrete logarithm problem over a finite field.
"""
import random


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if a % b == 0:
        return b
    return gcd(b, a % b)


def gen_key(q):
    key = random.randint(10**20, q)
    while gcd(q, key) != 1:
        key = random.randint(10**20, q)
    return key


def power(a, b, c):
    """Fast modular exponentiation."""
    x, y = 1, a
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b //= 2
    return x % c


def encrypt(msg, q, h, g):
    k = gen_key(q)
    s = power(h, k, q)
    p = power(g, k, q)
    print("g^k  :", p)
    print("g^ak :", s)
    en_msg = [s * ord(c) for c in msg]
    return en_msg, p


def decrypt(en_msg, p, key, q):
    h = power(p, key, q)
    return ''.join(chr(int(c / h)) for c in en_msg)


if __name__ == "__main__":
    msg = 'Hello from ElGamal'
    print("Original Message :", msg)

    q   = random.randint(10**20, 10**50)
    g   = random.randint(2, q)
    key = gen_key(q)
    h   = power(g, key, q)

    print("g used   :", g)
    print("g^a used :", h)

    en_msg, p  = encrypt(msg, q, h, g)
    decrypted  = decrypt(en_msg, p, key, q)
    print("Decrypted Message:", decrypted)