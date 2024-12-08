arr1 = [1,2,3,4,5,6,7,8,9,8,12,12,12]
arr2 = [1,2,3,4,12]


def subset(arr1,arr2):
    count = 0
    arr1 = set(arr1)
    arr1 = list(arr1)
    for i in range(len(arr2)):
        for j in range(len(arr1)):
            if arr2[i] == arr1[j]:
                count += 1
    if count == len(arr2):
        return True
    else:
        return False

print(subset(arr1,arr2))