"""
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3 # --> [1,2,2,3,5,6]
"""

"""
nums1 = [1]
m = 1
nums2 = []
n = 0 #-->[1]
"""
nums1 = [0]
m = 0
nums2 = [1]
n = 1 #--> [1]
"""

"""
"""
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3 #--> [1,2,3,4,5,6]
"""
def merge_sort(nums1, nums2, m, n):
    while n > 0:
        for num2 in nums2:
            nums1[m] = num2
            m += 1
            n -= 1
    
    for i in range(len(nums1) - 1):
        for j in range(i + 1, len(nums1)):
            if nums1[i] > nums1[j]:
                print("swapuju", nums1[i], nums1[j])
                tmp = nums1[i]
                nums1[i] = nums1[j]
                nums1[j] = tmp
                
    print(nums1)
        

merge_sort(nums1, nums2, m, n)