# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/?envType=problem-list-v2&envId=wttdj9f3
#nums = [-1,-2,-3,-4,3,2,1] #--> 1
#nums = [1,5,0,2,-3] #--> 0
nums = [-1,1,-1,1,-1] #--> -1

x = 1
for item in nums:
    x *= item

def signFunc(x):
    return(1 if x > 0 else
           (0 if x == 0 else -1))

print(signFunc(x))

"""
class Solution():
    def arraySign(self, nums):
        x = 1
        for item in nums:
            x *= item
        
        return self.signFunc(x)

    def signFunc(self, x):
        return(1 if x > 0 else (0 if x == 0 else -1))
"""