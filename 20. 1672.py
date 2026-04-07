#accounts = [[1,2,3], [3,2,1]] #--> 6
accounts = [[1,5],[7,3],[3,5]] #--> 10

richest = 0

for acc in accounts:
    sum = 0

    for item in acc:
        sum += item
    
    if sum > richest:
        richest = sum

print(richest)
