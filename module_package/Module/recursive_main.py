

from recursive_main import factorial, fibonacci, sum_digits, binary

n = int(input("Enter a number: "))

print("\n----- Results -----")

# Factorial
print("Factorial:", factorial(n))

# Fibonacci Series
print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")

# Sum of digits
print("\nSum of digits:", sum_digits(n))

# Binary conversion
if n == 0:
    print("Binary:", 0)
else:
    print("Binary:", binary(n))