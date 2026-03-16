"""
Euler's Totient Function φ(n)
Counts integers from 1 to n that are coprime with n.
Used in RSA key generation.
"""


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def phi(n):
    """Returns Euler's totient φ(n)."""
    return sum(1 for i in range(1, n) if gcd(i, n) == 1)


if __name__ == "__main__":
    print("Euler's Totient Function φ(n):\n")
    for n in range(1, 21):
        print(f"  φ({n:2d}) = {phi(n)}")