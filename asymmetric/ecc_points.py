"""
Elliptic Curve Cryptography (ECC) — Point generation over a finite field Z_p.
Finds all points (x, y) satisfying: y^2 ≡ x^3 + ax + b (mod z)
"""


def find_curve_points(a, b, z):
    """
    Returns all points on elliptic curve y^2 = x^3 + ax + b over Z_z
    """
    rhs = [(i**3 + a*i + b) % z for i in range(z)]
    lhs = [(i**2) % z           for i in range(z)]

    print("LHS (y^2 mod z)       :", lhs)
    print("RHS (x^3+ax+b mod z)  :", rhs)

    points = [(i, j) for i in range(z) for j in range(z) if lhs[i] == rhs[j]]
    return points


if __name__ == "__main__":
    a = int(input("Enter coefficient a (x term): "))
    b = int(input("Enter constant b: "))
    z = int(input("Enter field size z (prime): "))

    points = find_curve_points(a, b, z)
    print(f"\nPoints on curve E over Z_{z} :", points)
    print(f"Total points: {len(points)}")