import queue
test = input("Say something")
reverse = ""
sentance = queue.LifoQueue()

for i in test:
    sentance.put(i)
for i in test:
    reverse += sentance.get()
print(reverse)