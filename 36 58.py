s = "Hello World" #--> 5
#s = "   fly me   to   the moon  " #--> 4
#s = "luffy is still joyboy" #--> 6


def Len_Substrings(s):
    word = ""
    len_words = []
    for char in s:
        if char != " ":
            word += char
            len_words.append(word)
            print(word, len_words)
        else:
            word = ""

    return len(len_words[len(len_words) - 1])

print(Len_Substrings(s))