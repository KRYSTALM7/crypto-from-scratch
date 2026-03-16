"""
Fermat's Primality Test
Uses Fermat's Little Theorem: if p is prime, then a^(p-1) ≡ 1 (mod p)
Higher k = more accurate (probabilistic test)
"""
import random


def power(a, n, p):
    """Fast modular exponentiation O(log n)."""
    res, a = 1, a % p
    while n > 0:
        if n % 2:
            res = (res * a) % p
            n -= 1
        else:
            a = (a**2) % p
            n //= 2
    return res % p


def is_prime(n, k=5):
    """
    Fermat primality test.
    Returns True if n is probably prime, False if definitely composite.
    """
    if n in (1, 4):
        return False
    if n in (2, 3):
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if power(a, n - 1, n) != 1:
            return False
    return True


if __name__ == "__main__":
    test_cases = [2, 3, 11, 13, 15, 17, 25, 97]
    for n in test_cases:
        result = is_prime(n, k=5)
        print(f"is_prime({n:3d}) = {result}")