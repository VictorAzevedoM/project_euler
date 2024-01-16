# There exists exactly one Pythagorean triplet for which a+b+c=1000.
# Find the product abc.
import math


def special_pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(a, n):
            c = math.sqrt(a**2 + b**2)
            if a + b + c == n:
                return a * b * c


print(special_pythagorean_triplet(1000))
