
def f(number, even):
    sume = 0
    number = str(number)
    if even == True:
        for num in number:
            if int(num)%2 == 0:
                sume += int(num)
    else:
        for num in number:
            if int(num)%2 != 0:
                sume += int(num)
    return print(sume)

f(3124,True) #returns 6
f(3124,False) #returns 4
f(20576,False) #returns 12
f(20576,True) #returns 8
f(13115,True) #returns 0