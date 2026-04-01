s = "Hello"

result = ""
for char in s:
    if 64 < ord(char) < 91:                    # if char's value is in uppercase range 65-90 ==> True
        lowercase_val = ord(char) + 32         # 
        result += chr(lowercase_val)
    else:
        result += char

print(result)

# or just use a built in func....
print("string is:", s)
print(s.lower())
