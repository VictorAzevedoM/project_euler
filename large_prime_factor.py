import math
#What is the largest prime factor of the number 600851475143 ?

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 

def largest_prime_factor(n):
  if n % 2 == 0:
    return 2

  for i in range(int(math.sqrt(n)), 1, -1):
    if n % i == 0 and is_prime(i):
      return i
        
print(largest_prime_factor(600851475143))