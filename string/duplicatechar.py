s = input("Enter a string: ")

printed = ""

for i in range(len(s)):
    count = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1

    found = False
    for ch in printed:
        if ch == s[i]:
            found = True

    if count > 1 and found == False:
        print(s[i])
        printed += s[i]