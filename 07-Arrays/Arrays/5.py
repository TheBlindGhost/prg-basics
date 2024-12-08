arr1 = [15, 8, 31, 47, 2, 19]
mean = 0

for i in arr1:
    mean += i

for i in arr1:
    print(i,end=' ')

print(f'The mean is {mean/len(arr1)}')