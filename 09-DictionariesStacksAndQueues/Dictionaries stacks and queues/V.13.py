import queue

math = queue.LifoQueue()

RPN = "8 3 1 + / 3 2 - 4 + * ="
num1 = 0
num2 = 0
res = 0

for i in RPN:
    if i in "0123456789":
        math.put(i)
    if i == "+":
        num1 = int(math.get())
        num2 = int(math.get())
        res = num1 + num2
        math.put(res)
    if i == "-":
        num1 = int(math.get())
        num2 = int(math.get())
        res = num2 - num1
        math.put(res)
    if i == "*":
        num1 = int(math.get())
        num2 = int(math.get())
        res = num1 * num2
        math.put(res)
    if i == "/":
        num1 = int(math.get())
        num2 = int(math.get())
        res = num2 / num1
        math.put(res)
    if i in "=":
        print(math.get())

