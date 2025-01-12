price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
totalValueBefore = 0
totalValueAfter = 0
print("Products before discount")
for key,value in price_list.items():
   print(f"{key} : {value}")
   totalValueBefore += float(value)
print("Total value =", round(totalValueBefore,2))
print('Products after discount')

for key,value in price_list.items():
    value = round((value*0.9),2)
    print(f"{key} : {value}")
    totalValueAfter += float(value)
print("Total value =", round(totalValueAfter,2))