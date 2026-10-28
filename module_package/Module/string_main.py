

from string_utils import count_vowels, reverse_string, is_palindrome, count_words, remove_spaces

text = input("Enter a string: ")

print("\n----- String Operations -----")

print("Number of vowels:", count_vowels(text))

print("Reversed string:", reverse_string(text))

if is_palindrome(text):
    print("Palindrome: Yes")
else:
    print("Palindrome: No")

print("Number of words:", count_words(text))

print("String without spaces:", remove_spaces(text))