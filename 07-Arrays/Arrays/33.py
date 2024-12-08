arr = [
    [1,2,3,4,5],
    [1,2,3,4,5],  
    [5,4,3,2,1]
]


for i in arr:
    for j in i:
        print(j,end=' ')
    print('\n')



for i in range(len(arr)):
    for j in range(len(arr[i])):
        if j == 0:
            temp = arr[i][j]
            arr[i][j] = arr[i][j-1]
        elif j == len(arr[i])-1:
            arr[i][j] = temp


for i in arr:
    for j in i:
        print(j,end=' ')
    print('\n')
