arr1 = [15, 8, 31, 47, 2, 19]
i = 0
mean = 0

while i < len(arr1):
    mean += arr1[i]
    i += 1

while i < len(arr1):
    print(arr1[i],end=' ')
    i += 1

print(f'The mean is {mean/len(arr1)}')
