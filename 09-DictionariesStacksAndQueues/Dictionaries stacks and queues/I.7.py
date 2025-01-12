products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

print('Product list')
prodTotal = 0
for key,value in products.items():
   print(f"{key} : {value} ")
   prodTotal += int(value)
print('Total product quantity = ', prodTotal)
print('Total individual product = ', len(products))