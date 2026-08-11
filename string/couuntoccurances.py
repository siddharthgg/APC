s = input("Enter a sentence: ")
word = input("Enter word: ")

count = 0
temp = ""

for ch in s + " ":
    if ch != " ":
        temp += ch
    else:
        if temp == word:
            count += 1
        temp = ""

print("Occurrences =", count)