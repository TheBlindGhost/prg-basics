def f(x,y):
    sume = 0
    for num in range(x,y+1):
        if num%2 == 0 and num%3 ==0 and num%4 != 0:
            sume += num
    return print(sume)


f(1,20) #returns 24
f(10,30) #returns 48
