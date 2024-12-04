hours = int(input("Number of hours parking?"))

if hours <= 2:
    print("You owe 5PLN")
elif hours > 2 and hours <=6:
    print("You owe 10PLN")
elif hours > 6:
    print("You owe 20PLN")