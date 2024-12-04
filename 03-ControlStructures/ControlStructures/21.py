money = int(input('How much money?'))

if money > 5:
    pln5 = int(money/5)
    money = money%5
if money > 2:
    pln2 = int(money/2)
    money = money%2

print(f'5 PLN coins: {pln5} \n2 PLN coins: {pln2} \n1 PLN coins: {money}')