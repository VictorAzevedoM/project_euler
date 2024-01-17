# Find the sum of all the primes below two million.

import math


def summation_of_primes(n):
    primes = [2]
    for i in range(3, n, 2):
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return sum(primes)


print(summation_of_primes(2000000))
