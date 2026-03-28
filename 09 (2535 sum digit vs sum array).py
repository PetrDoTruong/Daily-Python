nums = [1,15,6,3] #--> 9

elem_sum = 0
digit_sum = 0

for num in nums:
    elem_sum += num
    tmp = num

    while tmp > 0:
        last_digit = tmp % 10
        digit_sum += last_digit
        tmp = (tmp - last_digit) // 10

result = abs(elem_sum - digit_sum)

print(result)