def f(x,y):
    amount = 0
    for num in range(x,y):
        if num < 0 and num%2 == 0:
            amount += 1
    return print(amount)


f(-7,8) #returns 3
f(-1,11) #returns 0