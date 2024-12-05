import range

number = int(input('Type a number:'))
x = int(input('Type range from:'))
y = int(input('Type range to:'))


print(f'The number {number} in range <{x,y}>:{range.num_in_range(number,x,y)}')