#s = "()" #--> true
#s = "()[]{}" #--> true
#s = "(]" #--> false
#s = "([)]" #--> false
s = "([])" #--> true

print(any(["]", "}", ")"]) in s)

def brackets(s):
    i = 0
    if len(s) > 2 and any("]", "}", ")") in s:
        while s:
            match s[i]:
                case ')':
                    if s[i - 1] != '(':
                        return False
                    else:
                        print("odstraňuju ()")
                        s = s.replace("()", "", 1)
                        i -= 2

                case ']':
                    if s[i - 1] != '[':
                        return False
                    else:
                        print("odstraňuju []")
                        s = s.replace("[]", "", 1)
                        i -= 2
                
                case '}':
                    if s[i - 1] != '{':
                        return False
                    else:
                        print("odstraňuju {}")
                        s = s.replace("{}", "", 1)
                        i -= 2
            i += 1

        return True
    else:
        return False

#print(brackets(s))

"""if len(s) % 2 == 0:
    while s:
        s = s.replace("()", "", 1)
        s = s.replace("{}", "", 1)
        s = s.replace("[]", "", 1)
        print(s)
    print(True)
else:
    print(False)"""