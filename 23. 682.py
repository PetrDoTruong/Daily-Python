#ops = ["5","2","C","D","+"] #--> 30
#ops = ["5","-2","4","C","D","9","+","+"] #--> 27
ops = ["1","C"] #--> 0

records = []

for i in range(len(ops)):

    match ops[i]:
        case 'D':
            last_num = len(records) - 1
            records.append(records[last_num] * 2)

        case 'C':
            last_num = len(records) - 1
            records.remove(records[last_num])
        case '+':
            last_num = len(records) - 1
            new_record = records[last_num] + records[last_num - 1]
            records.append(new_record)
        case _:
            records.append(int(ops[i]))

print(sum(records), records)

