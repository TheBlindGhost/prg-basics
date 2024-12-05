def f(n):
    i = 0
    while i < n:
        if i == 0:
            print('*',end='')
        else:
            print('/*',end='')
        i +=1

f(4) #returns "*/*/*/*"
f(1) #returns "*"