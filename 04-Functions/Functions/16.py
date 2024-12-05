def f(n):
    t1 = 0
    t2 = 1
    i = 0
    while i <= n-3:
        t3 = t1+t2
        t1 = t2
        t2 = t3
        i += 1
    if n == 0:
        print(t1)
    elif n == 1:
        print(t2)
    else:
        print(t3)

f(5) #returns 3
f(9) #returns 21