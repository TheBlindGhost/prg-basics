
arr = [
    [1,2,3,4,5],
    [1,2,3,4,5],  
    [5,4,3,2,1]
]

for i in arr:
    for j in i:
        print(j,end=' ')
    print('\n')

arr2= arr[0]
arr3 = arr[len(arr)-1]


arr[0] = arr3 
arr[len(arr)-1] = arr2          


for i in arr:
    for j in i:
        print(j,end=' ')
    print('\n')








