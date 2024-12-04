x = 3
y = -1

if x == 0 and y == 0:
    print("Middle of the plane")
elif x == 0 and y != 0:
    print('X axis')
elif x != 0 and y == 0:
    print('Y axis')
elif x > 0 and y > 0:
    print('First quadrant')
elif x < 0 and y > 0:
    print('Secund quadrant')
elif x < 0 and y < 0:
    print('Third quadrant')
elif x > 0 and y < 0:
    print('Forth quadrant')
