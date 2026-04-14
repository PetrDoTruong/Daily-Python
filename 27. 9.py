x = 121 #--> true
#x = -121 #--> false
#x = 10 #--> false

"""
result = 0
copy = x

if x >= 0:
    while copy != 0:
        result *= 10
        last_digit = copy % 10
        
        copy = (copy - last_digit) // 10
        result += last_digit

    print(result, copy, x)

    print(result == x)
else:
    print(False)
"""

# alternativa
"""str_x = str(x)
result = ""

while len(str_x) != 0:
    last_pos = len(str_x) - 1
    last_char = str_x[last_pos:] # cut untill last_pos and keep only last char
    result += last_char          # add char to result

    str_x = str_x[:last_pos]     # cut away from last pos ==> 121 -> 12
 
print(result, str(x), result == str(x))
"""

"""
# efektivnější
str_x = str(x)
    if str_x == str_x[::-1]:
        return True
    return False
"""