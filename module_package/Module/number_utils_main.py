# main.py

from number_utils import is_prime, is_palindrome, is_armstrong, is_perfect

num = int(input("Enter a number: "))

if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

if is_perfect(num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")