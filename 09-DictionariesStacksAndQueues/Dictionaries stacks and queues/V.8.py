# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Calculate total cost
total = 0

for key,value in prices.items():
    for k,v in cart.items():
        if k == key:
            total += value * v
print(total)