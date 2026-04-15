"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""

#s = "III" #––> 3
#s = "LVIII" #--> 58
s = "MCMXCIV" #--> 1994
# a>b>c> ---> a+b+c 

result = 0
dic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

for i in range(len(s) - 1):
    if dic[s[i]] >= dic[s[i + 1]]:
        print("přičtu", dic[s[i]])
        result += dic[s[i]]
    else:
        print("odečtu", dic[s[i]])
        result -= dic[s[i]]

last_pos = len(s) - 1

result += dic[s[last_pos]]
print(result)