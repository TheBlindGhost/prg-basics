def bubblesort(array):
    for n in range(len(array) - 1, 0, -1):

        swapped = False  

        for i in range(n):
            if array[i] > array[i + 1]:
              
                array[i], array[i + 1] = array[i + 1], array[i]

                swapped = True
        
        if not swapped:
            break

arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]

bubblesort(arr1)

for i in arr1:
    print(i, end=' ')