def f(expression):
    value = 0
    value = int(expression[0])
    temp1 = 0
    for num in range(1,len(expression)):
        if expression[num] == '+':
            value += int(expression[num+1])
        elif expression[num] == '-':
            value -= int(expression[num+1])
    return print(value)


f("2+3") #returns 5
f("3+8+1") #returns 12
f("2+3-4+5-0") #returns 6

