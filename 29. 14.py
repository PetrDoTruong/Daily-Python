#strs = ["flower","flow","flight"] #--> "fl"
#strs = ["dog","racecar","car"] #--> ""
#strs = [] #--> ""
strs = ["ab", "a"] # --> "a"


""" 
# nefunguje na case: strs = ["ab", "a"] a []
result = ""

for i in range(len(strs[0])):
    for j in range(1, len(strs)):
        print("str je:", strs[0][i], "slovo: ", strs[j])

        if (strs[0][i] != strs[j][i]):
            break
        
    else: # for-else loop
        result += strs[0][i]
        continue # break vs continue --> break ends loop / continue = jmp to next iter

    break
print(result)
"""

if not strs:
    print("výsledek:", "")
else:
    longest_prefix = 0

    for i in range(len(strs[0])): # --> in range len(1st_word)
        for word in strs:
            if i >= len(word) or word[i] != strs[0][i]:
                break
        else:
            longest_prefix += 1
            continue

        break

    print("výsledek:", strs[0][:longest_prefix])