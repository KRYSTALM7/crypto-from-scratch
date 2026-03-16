"""
Feistel Cipher implementation on a text message.
Two rounds of encryption and decryption using random binary keys.
"""
import random
import binascii

def rand_key(length):
    return ''.join(str(random.randint(0, 1)) for _ in range(length))

def xor(a, b):
    return ''.join('0' if a[i] == b[i] else '1' for i in range(len(a)))

def binary_to_decimal(binary):
    return int(binary, 2)

if __name__ == "__main__":
    PT = "Hello"
    print("Plain Text   :", PT)

    PT_bin = ''.join(format(ord(c), '08b') for c in PT)
    n  = len(PT_bin) // 2
    L1 = PT_bin[:n]
    R1 = PT_bin[n:]
    m  = len(R1)

    K1 = rand_key(m)
    K2 = rand_key(m)

    # Round 1
    f1 = xor(R1, K1)
    R2 = xor(f1, L1)
    L2 = R1

    # Round 2
    f2 = xor(R2, K2)
    R3 = xor(f2, L2)
    L3 = R2

    bin_data = L3 + R3
    cipher   = ''.join(chr(binary_to_decimal(bin_data[i:i+7]))
                       for i in range(0, len(bin_data), 7))
    print("Cipher Text  :", cipher)

    # Decryption
    L4, R4 = L3, R3
    f3 = xor(L4, K2)
    L5 = xor(R4, f3)
    R5 = L4

    f4 = xor(L5, K1)
    L6 = xor(R5, f4)
    R6 = L5

    PT1  = int(L6 + R6, 2)
    RPT  = binascii.unhexlify('%x' % PT1)
    print("Decrypted    :", RPT.decode())