import queue
number = 18

bin_stack = queue.LifoQueue()

while number != 0:
    bin_stack.put(number%2)
    number = int(number/2)

bin_num =""

while not bin_stack.empty():
    bin_num += str(bin_stack.get())
print(bin_num)