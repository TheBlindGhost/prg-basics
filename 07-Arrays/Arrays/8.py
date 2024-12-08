
def stars(n):
    number = ''
    for i in range(n):
        number += ' * '
    return number



arr1 = [2, 6, 4, 9, 7]
i = 0
while i < len(arr1):
    print(arr1[i], ': ', stars(arr1[i]))
    i += 1