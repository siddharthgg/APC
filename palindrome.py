def is_palindrome(integer):
    
    return str(integer) == str(integer)[::-1]

test_number = 12321

if is_palindrome(test_number):
    print(f"Yes, {test_number} is a palindrome.")
else:
    print(f"No, {test_number} is not a palindrome.")