def power(x, n):
    if n > 0:
        return x * x**(n-1)
    return n

def pow(x,n):
    print(power(x,n))


pow(2,10)