import json

# Open the JSON file in read mode
with open('dogs.json', 'r', encoding='utf-8') as file:
   # Load the data from the JSON file into a variable
   data = json.load(file)

# Print the JSON data
for dog in data:
    for key ,value in dog.items():
        if dog['age'] < 5:
            print(key,':',value)
    print()
