nums = [1,1,2] #--> k = 2, nums = [1,2,_]
#nums = [0,0,1,1,1,2,2,3,3,4] #--> 5, nums = [0,1,2,3,4,_,_,_,_,_]

def remDupl(nums):
    if len(nums) == 0:
        return 0

    k = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k

print(remDupl(nums))