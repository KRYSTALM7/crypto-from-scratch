"""
Chinese Remainder Theorem (CRT)
Finds the smallest x such that:
  x ≡ rem[0] (mod num[0])
  x ≡ rem[1] (mod num[1])
  ...
Used in RSA to speed up decryption.
"""


def find_min_x(num, rem):
    """Brute-force CRT solution."""
    x = 1
    while True:
        if all(x % num[j] == rem[j] for j in range(len(num))):
            return x
        x += 1


if __name__ == "__main__":
    # Example: x ≡ 2 (mod 3), x ≡ 3 (mod 4), x ≡ 1 (mod 5)
    num = [3, 4, 5]
    rem = [2, 3, 1]
    print(f"num = {num}")
    print(f"rem = {rem}")
    print(f"Smallest x = {find_min_x(num, rem)}")

    # Second example
    num2 = [5, 7]
    rem2 = [1, 3]
    print(f"\nnum = {num2}")
    print(f"rem = {rem2}")
    print(f"Smallest x = {find_min_x(num2, rem2)}")
