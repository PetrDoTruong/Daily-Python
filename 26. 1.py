"""
nums = [2,7,11,15]
target = 9 #--> [0,1]
"""

"""
nums = [3,2,4]
target = 6 #--> [1,2]
"""

nums = [3,3]
target = 6 #-–> [0,1]

result = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(i, j)
        if (nums[i] + nums[j]) == target:
            result += [i, j]
            print(result)
            break
        