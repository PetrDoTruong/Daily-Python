"""
words = ["leet","code"]
x = "e"
#--> [0,1]

"""

"""
words = ["abc","bcd","aaaa","cbc"]
x = "a"
#--> [0,2]

"""

words = ["abc","bcd","aaaa","cbc"]
x = "z"
#--> []

result =[]
for i in range(len(words)):
    if x in words[i]:
        result.append(i)

print(result)


"""
        return [ i for i in range(len(words)) if x in words[i]]
"""