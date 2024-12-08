def wordcount(word):
    word = word.strip()
    count = 1
    for i in word:
        if i == ' ':
            count +=1
    return count

def wordarr(word):
    order = []
    w = ''
    word = word.strip()
    word += ' '
    for i in word:
        if i == ' ':
            order.append(w)
            w = ''
        else:
            w += i
    order.sort(key=len)
    order.reverse()


    return order

def aplarr(array):
    order = wordarr(array)
    order.sort()
    return order