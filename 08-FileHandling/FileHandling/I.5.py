n = 1
with open('countries.txt', 'r') as file:
    for line in file:
        print(f'{n}. {line}', end="")
        n += 1
