price = int(input('What is the price?'))
amount = int(input('How many items?'))

if amount < 3:
    payment = amount * price
else:
    amount = amount-2
    payment = (2*price) + (amount * (price * 0.75))

print(f'You need to pay {payment} $')