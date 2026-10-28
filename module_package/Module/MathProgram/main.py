

from Math.basic import add, subtract, multiply, divide
from Math.number import is_prime, is_armstrong, is_palindrome
from Math.stat import mean, maximum, minimum

# Arithmetic operations
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\n--- Arithmetic Operations ---")
print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))

# Number operations
n = int(input("\nEnter a number: "))

print("\n--- Number Operations ---")

if is_prime(n):
    print("Prime: Yes")
else:
    print("Prime: No")

if is_armstrong(n):
    print("Armstrong: Yes")
else:
    print("Armstrong: No")

if is_palindrome(n):
    print("Palindrome: Yes")
else:
    print("Palindrome: No")

# Statistics
numbers = [10, 20, 30, 40, 50]

print("\n--- Statistics ---")
print("Numbers:", numbers)
print("Mean:", mean(numbers))
print("Maximum:", maximum(numbers))
print("Minimum:", minimum(numbers))