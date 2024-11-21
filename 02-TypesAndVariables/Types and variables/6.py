import math
distance = int(input("Enter distance in km:"))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fule consumption per 100km:'))

fuel_per_km = fuel_consumption/100
fuel_used = math.ceil(fuel_per_km*distance)
price = fuel_used*fuel_price
print("Transport will cost:", int(price))
