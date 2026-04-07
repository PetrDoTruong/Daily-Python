#n = 234 #--> 15
n = 4421 #--> 21

multiply_digits = 1
sum_digits = 0

while n != 0:
    last_digit = n % 10
    
    multiply_digits *= last_digit
    sum_digits += last_digit

    n = (n - last_digit) // 10

print(multiply_digits - sum_digits)