#arr = [2,6,4,1] #--> false
#arr = [1,2,34,3,4,5,7,23,12] #--> true

for i in range(len(arr) - 2):
    if (arr[i] % 2 == 1 and
        arr[i + 1] % 2 == 1 and
        arr[i + 2] % 2 == 1):
        print(True)                 #--> kdyby byl return, nemuseli bychom break
        break

print(False)                        #--> kdyby byla funkce, tak se nevytiskne False