#digits = [1,2,3] #-->[1,2,4]
#digits = [4,3,2,1] #-->[4,3,2,2]
#digits = [9] #--> [1,0]
digits = [9,9] #--> [1,0,0]
"""
def plus_one(digits):
    for i in range(len(digits)):
        if i == len(digits) - 1:
            digits[i] += 1

    return digits
"""

def plus_one(digits):
    num = 0
    # arr to num
    for digit in digits:
        num *= 10
        num += digit
    
    num += 1
    result = []
    # num to arr
    while num > 0:
        last_digit = num % 10
        result.append(last_digit)

        num = (num - last_digit) // 10

    result.reverse()
    return result

print(plus_one(digits))