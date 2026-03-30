n = 5       # --> 8
start = 0 

nums = []
result = 0
for i in range(n):
    num = start + 2 * i
    nums.append(num)
    result = result ^ num

print(nums, result)
