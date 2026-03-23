#num = 7        #--> 1
num = 121      #--> 2
#num = 1248     #--> 4
#num = 54        #--> 0

digits = []
count = 0
copy = num

while num != 0:
    digit = num % 10                # poslední cifra
    num = (num - digit) // 10       # vynulovat a posunout desetinné místo 
    digits.append(digit)        # přidáme cifru do pole
    print(digits, num, copy)
for digit in digits:                # průchod cifry
    print(digit)
    if (copy % digit) == 0:         # pokud je číslo dělitelné cifrou, zvyšíme count o 1
        count += 1

print("výsledek je", count)