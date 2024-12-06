def power(x, n):
    if n == 0:
        return 1
    return x * power(x,n-1)

def pow(x,n):
    print(power(x,n))


pow(2,10)
