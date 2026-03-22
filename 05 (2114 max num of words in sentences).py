sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

result = []

for sentence in sentences:
    spaces = 1                  # počítáme mezery a ne počet slov, proto +1
    for str in sentence:
            spaces += 1
    result += [spaces]

print(max(result), result)


# efektivnější řešení:
"""
class Solution(object):
    def mostWordsFound(self, sentences):
       return max(len(s.split()) for s in sentences)
"""

