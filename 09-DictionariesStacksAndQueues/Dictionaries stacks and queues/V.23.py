import json


with open('euro.json', 'r', encoding='utf-8') as file:
   data = json.load(file)
print('Date           Buying rate     Selling rate')
print('===========================================')
for table in data['rates']:
   print(f'{table['effectiveDate']}     {table['bid']}           {table['ask']}')