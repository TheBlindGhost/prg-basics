

def factorial(n):

    # 0! = 1, 1! = 1
    if n==0 or n==1:
        return 1

    # n! = n * (n-1)!
    if n > 1:
        return n * factorial(n-1)
    
def f(num):
        print(factorial(num))
        

    
f(4)