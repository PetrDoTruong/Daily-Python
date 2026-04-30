"""

"""
a = "11"
b = "1" #--> "100"
"""
a = "1010"
b = "1011" #--> "10101"
"""
def add_bin(a, b):
    result = ""
    cf = 0

    while len(a) != len(b):
        if len(a) > len(b):
            b = "0" + b
        else:
            a = "0" + a

    last_num = len(a) - 1

    while last_num >= 0:
        bit_a = int(a[last_num])
        bit_b = int(b[last_num])

        total = bit_a + bit_b + cf
        result_bit = total % 2
        result = str(result_bit) + result
        cf = total // 2

        last_num -= 1


    if cf:
        result = "1" + result

    return result

print(add_bin(a,b))

 
