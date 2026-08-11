s = input("Enter a string: ")

printed = ""

for i in range(len(s)):
    found = False

    for ch in printed:
        if ch == s[i]:
            found = True

    if found == False:
        count = 0
        for j in s:
            if j == s[i]:
                count += 1
        print(s[i], "=", count)
        printed += s[i]