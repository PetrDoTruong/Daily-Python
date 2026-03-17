s = "ahojah"
found = -1
for i in range(len(s)):
    if found > -1:
        break
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            break
    found = i

print("found je", found)
