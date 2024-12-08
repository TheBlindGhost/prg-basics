#Tuple: 50,20,40,50,30,50
#Value: 50
#Number of occurrences: 3

def occer(number, tul):
    value = 0
    for i in range(len(tul)):
        if number == tul[i]:
            value += 1
    return value


if __name__ == "__main__":  
    tul = (50,20,40,50,30,50)
    number = 50
    print(occer(number,tul))