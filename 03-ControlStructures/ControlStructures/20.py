number = int(input('Type a number'))

bin_num = ''

while number != 0:
    rem = number%2
    number = int(number/2)
    bin_num += str(rem)



print(f'The binary number is {bin_num[::-1]}')