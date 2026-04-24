"""
haystack = "sadbutsad"
needle = "sad" #--> 0
"""
"""
haystack = "leetcode"
needle = "leeto" #--> -1
"""
"""
haystack = "hello"
needle = "ll" #--> 2
"""

haystack = "a"
needle = "a" #--> 0

def Find_Needle(haystack, needle):

    if (needle in haystack and
        len(haystack) >= len(needle)):
            for i in range(len(haystack)):
                print(needle, haystack[i:len(needle) + i])

                if (needle[0] == haystack[i] and
                    needle == haystack[i:len(needle) + i]):
                    return i
    
    return -1
            
print(Find_Needle(haystack, needle))