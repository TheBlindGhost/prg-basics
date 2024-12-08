def arrmax(type,array):
    max = array[0]
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            ind = array.index(array[i])
    if type == 1:
        return max
    elif type == 2:
        return ind
def arrmin(array):
    min = array[0]
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
    return min

def diff(array):
    return arrmax(1,array) - arrmin(array)

def med(array):
    array.sort()
    if len(array)%2 == 0:
        m = (array[int((len(array)/2))-1] + array[(int(len(array)/2))]) / 2
    else:
        m = array[int(len(array)/2)]
    return m

def maxmin(array):
    a= []
    a.append(arrmin(array))
    a.append(arrmax(1,array))
    return a

def asstring(array):
    string = ''
    for i in range(len(array)):
        string += str(array[i])
        if array[i] != array[len(array)-1]:
            string += '-'
    return string


def secund(array):
    array.remove(arrmax(1,array))
    return arrmax(1,array)
    

arr = [7,3,8,5,2]

print(asstring(arr))