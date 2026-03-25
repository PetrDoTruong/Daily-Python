words = ["abc","car","ada","racecar","cool"]

palindrom = ""
for string in words:
    for char in string:
        palindrom = char + palindrom
    if palindrom == string:
        print(palindrom)
        break
    else:
        palindrom = ""

print(palindrom)

# efektivnější kód
"""
   def firstPalindrome(self, words):
        for word in words:
           if word == word[::-1]:
            return word
        return ""
"""