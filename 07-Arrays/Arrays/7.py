arr1 = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
long = 0
ind = 0

for i in arr1:
    if len(i) > long:
        long = len(i)
        ind = arr1.index(i)

print(arr1[ind])