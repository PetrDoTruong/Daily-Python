#moves = "UD" #--> True
moves = "LL" #--> False
# Up == [1, 1]
# Down == [-1, -1]
# Left == [-1, 0]
# Right == [+1, 0]

pos = [0, 0]

for move in moves:
    match move:
        case 'U':
            pos[0] += 1
            pos[1] += 1
        case 'D':
            pos[0] -= 1
            pos[1] -= 1
        case 'L':
            pos[0] -= 1
        case 'R':
            pos[0] += 1

print(pos == [0, 0])

# lepší řešení
"""
print(moves.count('U') == moves.count('D') and
      moves.count('L') == moves.count('R'))
"""

