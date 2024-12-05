def f(number1,number2,operator):
    if operator == '+':
        return print(number1 + number2)
    elif operator == '-':
        return print(number1 - number2)
    elif operator == '*':
        return print(number1 * number2)
    elif operator == '%':
        return print(number1 % number2)
    elif operator == '**':
        return print(number1 ** number2)
    

f(2,3, "+") #returns 5
f(2,3, "%") #returns 2
f(2,3, "**") #returns 8
f(2,3, "*") #returns 6
f(2,3, "-") #returns -1