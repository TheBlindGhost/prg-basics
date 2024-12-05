def f(detector):
    amount = 0
    for num in detector:
        if num == '+':
            amount += 1
        if num == '-':
            amount -= 1
        if amount >= 3:
            return print(True)
    return print(False)


f("+-+++-+---") #returns True
f("+-+-+-+-") #returns False
f("+-++-+--") #returns False
f("+-++-++-+---") #returns True