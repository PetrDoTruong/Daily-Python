#nums = [-4,-1,0,3,10] #--> [0,1,9,16,100]
nums = [-7,-3,2,3,11] #--> [4,9,9,49,121]

print(sorted(list(map((lambda x: x**2), nums))))
# returns sorted array, where items are mapped over a lambda func, which returns sqr of each num
