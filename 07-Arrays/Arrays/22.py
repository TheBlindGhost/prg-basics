import random
arr = [7,9,2,4,5,6]

def rand_elem(array):
    num = random.randint(0,len(array)-1)
    return array.index(num)

print(rand_elem(arr))
    