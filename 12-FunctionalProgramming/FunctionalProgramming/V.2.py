from functools import reduce

numbers = [2,4,6,3,7,5]


res = reduce(lambda x,y: x+y,list(filter(lambda x: x%2 == 0,numbers)))

print(res)