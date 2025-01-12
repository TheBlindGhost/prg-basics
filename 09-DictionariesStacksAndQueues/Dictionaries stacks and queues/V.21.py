import json

data = {
   "favorite_book": {
      "name": "dune",
      "main_character": "Paul",
      "genera": "sci-fi",
      "setting": "desert",
      "valuable_resource": "spice",
      
   }
}

# Specify the file path and name
file_name = "favorite.json"

# Open the file in write mode and use json.dump() to write the data to the file
with open(file_name, 'w') as file:
   json.dump(data, file, indent=4)

print("Data has been written to", file_name)