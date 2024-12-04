age = int(input('Enter dogs age'))

if age <= 2:
    humane_age = age*10,5
else:
    humane_age = int(21 + (age-2)*4)
print(f'Dog is {humane_age} humane years')