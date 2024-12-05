def f(amount_to_pay):
    pln5 = 0
    pln2 = 0
    if amount_to_pay >= 5:
        pln5 = int(amount_to_pay/5)
        amount_to_pay = amount_to_pay%5
    if amount_to_pay >= 2:
        pln2 = int(amount_to_pay/2)
        amount_to_pay = amount_to_pay%2
    number_of_coins = pln5 + pln2 + amount_to_pay
    return number_of_coins

print(f(23),f(8) ,f(2), f(0))
