arr1 = ["water","book","sky"] 
arr2 = ["water","book","sky"]
arr3 = [True,False]   
arr4 = [True,False,True]
arr5 = [5,3,1] 
arr6 = [5,3,1]
arr7 = [3,2,1] 
arr8 = [3,2]


def compare(arr1,arr2):
    i = 0
    if len(arr1) == len(arr2):
        while i < len(arr1):
            if arr1[i] != arr2[i]:
                return False
            i += 1
        return True 
    return False


def twoarr(arr1,arr2):
    print('Arry 1:')
    for i in arr1:
        print(i,end=',')
    print('\nArry 2:')
    for j in arr2:
        print(j, end=',')
    if compare(arr1,arr2) == True:
        print('\nThe arrays are the same')
    else:
        print('\nArrays are different')

twoarr(arr1,arr2)
