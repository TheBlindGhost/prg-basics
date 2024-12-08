number = float(input('Type a number'))

array = [15, 38.22, 7, 23.1, 14.32]
count = 0
for i in range(len(array)):
    if number < float(array[i]):
        count += 1

print(count)