arr =[[-38, 19], [5,40],[-7,11],[-729,16]]

max = arr[0][0]
min = arr[0][0]
posmin = [0,0]
posmax = [0,0]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] > max:
            posmax = []
            max = arr[i][j]
            posmax.append(i)
            posmax.append(j)    
        
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < min:
            posmin = []
            min = arr[i][j]
            posmin.append(i)
            posmin.append(j)

print(f'MAX {max} Index {posmax} MIN {min} Index {posmin}')