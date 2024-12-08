#Number: 23
#Array: 15 38 7 23 14
#Result: number 23 appears in the array



def occurs(number,array):
    for i in range(len(array)):
        if number == array[i]:
            return True
    return False

if __name__ == "__main__":
    array = [15, 38, 7, 23, 14]
    number = int(input('Type a number'))
    if occurs(number,array):
        print(f'Number {number} apperes in the array')
    else:
        print(f'Number {number} dose not appere in the array')

