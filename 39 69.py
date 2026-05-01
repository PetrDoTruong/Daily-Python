#x = 4 #--> 2
#x = 8 #--> 2
#x = 36 #--> 6
#x = 7
x = 0

def sqrt(x):
    for i in range(x + 1):
        if i * i > x:
            return i - 1
        
    return x

print(sqrt(x))