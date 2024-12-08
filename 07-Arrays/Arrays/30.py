arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if i == 0:
            arr[i][j] = arr[i][j-1] + 1
        elif j == 0:
            arr[i][j] = arr[i-1][j] +1
        else:
            arr[i][j] = arr[i][0] * arr[0][j]


print(arr)