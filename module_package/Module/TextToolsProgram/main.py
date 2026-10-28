# main.py

from texttools.cleaning import remove_punctuation, remove_extra_spaces
from texttools.tokenization import tokenize
from texttools.freq import word_frequency

text = input("Enter a text: ")

# Cleaning
cleaned_text = remove_punctuation(text)
cleaned_text = remove_extra_spaces(cleaned_text)

print("\n----- Text Processing -----")
print("Cleaned Text:", cleaned_text)

# Tokenization
words = tokenize(cleaned_text)

print("Tokens:", words)

# Word frequency
frequency = word_frequency(words)

print("\n----- Word Frequency -----")

for word, count in frequency.items():
    print(word, ":", count)