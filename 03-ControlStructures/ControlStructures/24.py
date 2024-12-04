i = 1
while i<10:
    if i < 6:
        for number in range(i):
            print('*', end='')
    else:
        for number in range(10-i):
            print('*', end='')
    print('\n')
    i += 1
