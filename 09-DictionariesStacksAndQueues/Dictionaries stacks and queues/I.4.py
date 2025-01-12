person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

# Name

#print(person['name'])

# Hobby

#print(person["hobby"])

# Whole content

#print(person)

# Surname to Nowak

#person["surname"] = "Nowak"
#print(person["surname"])

# Marriage status

#person["married"] = False
#print(person["married"])

# Add gender

#person["gender"] = 'male'
#print(person["gender"])

# Add hobby

#person["hobby"].append('bicycle')
#print(person["hobby"])

# Add phone

#Dict1['CorrectionHistory'][0]['CorrectionsAll'].append({'CorrChngDesc': 'Discount Line Changed'})
#person["phone"].update({'Work phone': '65327896579283'})
#print(person["phone"])

# Itterate through a dictionary


#for key,value in person.items():
#   print(f"{key} : {value}")
