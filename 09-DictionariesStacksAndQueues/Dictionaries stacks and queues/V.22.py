import json
data = {}

name = input('Product name:')
price = round(float(input('Product price:')),2)
paid = input('Did you pay (yes/no):')
while paid != "yes" and paid != "no":
    paid = input('Did you pay (yes/no)[WRITE CORRECT VALUE!!!!!]:')



data['name'] = name
data['price'] = price
if paid == "yes":
    data['paid'] = True
else:
    data['paid'] = False



# Specify the file path and name
file_name = "product.json"

# Open the file in write mode and use json.dump() to write the data to the file
with open(file_name, 'w') as file:
   json.dump(data, file, indent=4)

print("Data has been written to", file_name)