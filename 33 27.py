nums = [3,2,2,3] #--> 2, nums = [2,2,_,_]
val = 3

"""
nums = [0,1,2,2,3,0,4,2] #--> 5, nums = [0,1,4,0,3,_,_,_]
val = 2
"""

def remVal(nums, val):
    if len(nums) == 0 or val not in nums:
        return len(nums)

    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
        else:
            nums[i] += 1

    return k

print(remVal(nums, val), nums)