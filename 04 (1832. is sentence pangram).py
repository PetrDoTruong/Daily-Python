sentence = "leetcode" # --> False
sentence2 = "thequickbrownfoxjumpsoverthelazydog" #--> True

chars = []
if len(sentence) >= 26:
    for c in sentence:
        if c not in chars:
            chars += [c]
            print(chars)
    if len(chars) >= 26:
        result = True
    else:
        result = False
    print("true", chars)
else:
    result = False
    print("false")