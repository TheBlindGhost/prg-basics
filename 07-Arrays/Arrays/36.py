arr1=[
[2, 3],
[1, 5]
]
arr2 =[ 
[5, 0, 3, 7, 5],
[9, 0, 9, 1, 2]
]
arr3 =[
[2, 1],
[3, 5],
[7, 4],
[2, 6]
]

def convert_array(arr):
    arrcon = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arrcon.append(arr[i][j])
    return arrcon


print(convert_array(arr3))