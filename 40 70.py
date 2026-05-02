#n = 1
#n = 2 #--> 2
#n = 3 #--> 3
n = 4 #--> 5
#n = 6 #--> 13
"""
def steps(n):
    return (1 if n == 1 else (
        2 if n == 2 else ((steps(n - 1) + steps(n - 2)))
    ))

print(steps(n))
"""
# efektivnější
def steps(n):
    if n == 1:
        return 1
    
    a = 1
    b = 2

    for i in range(3, n + 1):
        new_num = a + b
        a = b
        b = new_num

    return b

print(steps(n))

"""
n = 1 -- 1x
n = 2 -- 2x
n = 3 -- 3x
n = 4 -- 5x
n = 5 -- (11111, 2111, 1211, 1121, 1112, 221, 212, 122) == 8x
n = 6 -- (11 11 11, 2 2 2, 2 2 11, 2 11 11, 11 2 2 , 2 11 2, 11 11 2, 11 2 11, 12111, 21111, 11211, 11121, 11112) == 13x
"""