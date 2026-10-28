

# Factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Fibonacci using recursion
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Sum of digits using recursion
def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)


# Binary conversion using recursion
def binary(n):
    if n == 0:
        return ""
    return binary(n // 2) + str(n % 2)