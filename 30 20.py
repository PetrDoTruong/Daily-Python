#s = "()" #--> true
#s = "()[]{}" #--> true
#s = "(]" #--> false
#s = "([)]" #--> false
#s = "))" #--> false
#s = "([])" #--> true
#s = "]" #--> False
#s = "((" #--> false
s = "){" #––> false

def brackets(s):
    while s: #--> if "" not empty
        if (len(s) % 2 == 0 and
            any(c in s for c in "])}") and
            s[0] not in ("])}")): #--> if string is even and there is a closing bracket not on 1st pos.

            for i in range(1, len(s)): #start from second bcs there are only odds and in 1 pair the second is always closing
                match s[i]:         # if "" == closing bracket --> prev must be opening bracket of same type --> else false
                    case "}":
                        print("remove {}")
                        if s[i - 1] == "{":
                            s = s.replace("{}", "", 1)
                            break
                        else:
                            return False

                    case "]":
                        print("remove []")
                        if s[i - 1] == "[":
                            s = s.replace("[]", "", 1)
                            break
                        else:
                            return False

                    case ")":
                        print("remove ()")
                        if s[i - 1] == "(":
                            s = s.replace("()", "", 1)
                            break
                        else:
                            return False
        else:
            return False

    return True #--> if brackets empty always true

print(brackets(s))