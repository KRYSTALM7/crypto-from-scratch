# Cryptography

> Implementations of classic and modern cryptographic algorithms in Python — symmetric ciphers, asymmetric encryption, and number-theoretic foundations.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## Structure
```
crypto-from-scratch/
├── symmetric/          # AES, DES, Feistel Cipher
├── asymmetric/         # RSA, ElGamal, ECC
└── math_foundations/   # Fermat test, Euler's totient, CRT
```

---

## 🗂Algorithms

### Symmetric Encryption
| File | Algorithm | Description |
|------|-----------|-------------|
| `aes_encryption.py` | AES (EAX mode) | Encrypt/decrypt using pycryptodome |
| `des_encryption.py` | DES from scratch | Full 16-round Feistel + S-boxes + permutations |
| `feistel_cipher.py` | Feistel Cipher | 2-round Feistel structure on text |

### Asymmetric Encryption
| File | Algorithm | Description |
|------|-----------|-------------|
| `rsa_encryption.py` | RSA | Key generation, encrypt/decrypt from scratch |
| `elgamal_encryption.py` | ElGamal | Discrete log based encryption |
| `ecc_points.py` | ECC | Point generation on elliptic curve over finite field |

### Math Foundations
| File | Concept | Used In |
|------|---------|---------|
| `fermat_primality_test.py` | Fermat's Little Theorem | Primality testing for RSA |
| `eulers_totient.py` | Euler's φ(n) | RSA key generation |
| `chinese_remainder_theorem.py` | CRT | RSA decryption optimization |

---

## ⚙Installation
```bash
git clone https://github.com/KRYSTALM7/crypto-from-scratch.git
cd crypto-from-scratch
pip install -r requirements.txt
```

---

## Usage
```bash
# Symmetric
python symmetric/aes_encryption.py
python symmetric/des_encryption.py
python symmetric/feistel_cipher.py

# Asymmetric
python asymmetric/rsa_encryption.py
python asymmetric/elgamal_encryption.py
python asymmetric/ecc_points.py

# Math foundations
python math_foundations/fermat_primality_test.py
python math_foundations/eulers_totient.py
python math_foundations/chinese_remainder_theorem.py
```

---

## How They Connect
```
Math Foundations
  └── Fermat Test      → checks primes used in RSA/ElGamal
  └── Euler's Totient  → φ(n) used in RSA key generation
  └── CRT              → speeds up RSA decryption

Symmetric
  └── Feistel Cipher   → building block used inside DES
  └── DES              → classic 16-round Feistel cipher
  └── AES              → modern standard (replaces DES)

Asymmetric
  └── RSA              → uses Euler totient + modular inverse
  └── ElGamal          → uses discrete log problem
  └── ECC              → elliptic curve over finite fields
```

---

## License

MIT License — Copyright (c) 2024 Sujan