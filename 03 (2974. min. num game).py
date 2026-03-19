nums = [2,7,9,6,4,6]

arr = []
while nums:                 # cyklus dokud máme čísla
    min1 = min(nums)        # najdeme min1, smažeme
    nums.remove(min1)

    min2 = min(nums)        # najdeme min2, smažene
    nums.remove(min2)

    arr.append(min2)        # vložíme v opačném pořadím = min2, pak min1
    arr.append(min1)

print(arr)


# efektivnější:
nums = [5,4,2,3] # --> [3,2,5,4]


arr = []
nums.sort()
print(nums)
for i in range(0, len(nums), 2):
    arr.append(nums[i + 1])
    arr.append(nums[i])
print(arr)
