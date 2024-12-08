arr = [7,9,2,4,5,6]
arreven = []
arrodd = []


for i in range(len(arr)):
    if arr[i]%2 == 0:
        arreven.append(arr[i])
    else:
        arrodd.append(arr[i])

arrall = arreven + arrodd

print(arrall)