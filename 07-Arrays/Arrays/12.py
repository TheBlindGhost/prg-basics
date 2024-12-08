arr1 = [2, 3, 2, 5, 8, 1, 9, 8]
#Unique elements: 3 5 1 9
uarr = []
for i in range(len(arr1)):
    count = arr1.count(arr1[i])
    if count == 1:
        uarr.append(arr1[i])

print(uarr)

    
