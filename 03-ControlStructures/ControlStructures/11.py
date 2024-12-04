current_price = 140.00
previous_price = 200.00

decrease = (previous_price - current_price)/previous_price*100

if decrease > 10:
    print(f"Buy the producy\n Price decreased by {int(decrease)}%") 