s = "ahojahoj"

found = -1                      # pokud nenajdeme unikát, vracíme -1
counts = {}
for c in s:                     # projdeme znaky stringu
    if c in counts:             # vytvoříme slovník
        counts[c] += 1          # přičteme opakovaný výskyt
    else:
        counts[c] = 1           # jinak nastavíme výskyt na 1.
print(counts)
for i in range(len(s)):         # projdeme celý slovník
    if counts[s[i]] == 1:       # hledáme ve slovníku znak na indexu, který se rovná 1
        found = i
        break                   # ukončíme předčasně cyklus
print(found)