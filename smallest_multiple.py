# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math


def smallest_multiple():
    # Find the smallest multiple by calculating the least common multiple (LCM)
    # of all numbers in the range from 1 to 20
    lcm = 1
    for i in range(1, 21):
        lcm = lcm * i // math.gcd(lcm, i)
    print(lcm)


smallest_multiple()
