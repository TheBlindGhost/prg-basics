e = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),("Jackson","Peter"),("Johnson","Rick"),("Lewis","Terry"),("Clarke","Robin")]

proper = list(map(lambda x: x[0].upper() + f', {x[1]}' ,e))


for i in proper:
    print(i)