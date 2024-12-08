arr1 = [-15, 8, -31, 47, -2, 19]
maxarr = 0
minarr = 0
for i in arr1:
    if i > maxarr:
        maxarr = i

for i in arr1:
    if i < minarr:
        minarr = i

print(f'MAX = {maxarr} MIN = {minarr}')