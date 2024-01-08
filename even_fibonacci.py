#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def even_fibonacci(n):
    sum = 0
    a = 1
    b = 1
    while a < n:
        if a%2 == 0:
            sum += a
        a,b = b, a+b
    return sum

print(even_fibonacci(4000000))