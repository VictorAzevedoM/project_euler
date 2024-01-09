#Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    return str(n) == str(n)[::-1] # [::-1] reverses a string

def largest_palindrome():
    largest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if is_palindrome(product) and product > largest:
                largest = product
    return largest

print(largest_palindrome())