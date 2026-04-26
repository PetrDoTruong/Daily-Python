"""
nums = [1,3,5,6]
target = 5 #--> 2
"""

"""
nums = [1,3,5,6]
target = 2  #--> 1
"""

"""
nums = [1,3,5,6]
target = 7  #––> 4
"""
nums = [1]
target = 0 #--> 0
"""

"""

def Search_insert(nums, target):
    result = 0
    if target in nums:
        for i in range(len(nums)):
            if target == nums[i]:
                return i
    else:
        for i in range(len(nums)):
            if target >= nums[i]:
                result = i + 1
            

    return result

print(Search_insert(nums, target))
