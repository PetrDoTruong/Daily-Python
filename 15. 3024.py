#nums = [3,3,3]
#nums = [9,4,9]
nums = [5,3,8]



def tria(nums):
    if ((nums[0] + nums[1] > nums[2]) and
        (nums[0] + nums[1] > nums[1]) and
        (nums[1] + nums[2] > nums[0])):
        return("equilateral" if (nums[0] == nums[1] == nums[2]) else
               ("isosceles" if ((nums[0] == nums[1]) or 
                                (nums[1] == nums[2]) or 
                                nums[0] == nums[2]) else "scalene"))
    else:
        return "Null"
    
print(tria(nums))