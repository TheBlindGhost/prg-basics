def sum_natural(n):
    if n > 0:
        return n + sum_natural(n-1)
    return n
def rec(n):
    print(sum_natural(n))

rec(10)