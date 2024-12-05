def f(product_code):
    sume = 0
    for num in range(len(product_code)-1):
        sume += int(product_code[num])
    if sume%7 == int(product_code[3]):
        return print(True)
    return print(False)


f("1082") #returns True
f("2035") #returns True
f("1114") #returns False
f("7071") #returns False