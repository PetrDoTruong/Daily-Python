#n = 7 #--> 9
n = 10 #--> 40

result = 0

for i in range(1, n + 1):
    if ((i % 3 == 0) or 
        (i % 5 == 0) or 
        (i % 7 == 0)):
        result += i
        
print(result)