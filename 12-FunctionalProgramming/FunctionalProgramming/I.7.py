even = lambda x: x % 2

def ev(x):
    if even(x) == 0:
        return True
    else:
        return False
print(ev(3))