#nums = [1,2,3,4,10] #--> false
#nums = [1,2,3,4,5,14] #--> True
nums = [1] #--> True

single_sum = 0
sum = 0

for num in nums:
    if num > 9:
        sum += num
    else:
        single_sum += num

print(single_sum != sum)