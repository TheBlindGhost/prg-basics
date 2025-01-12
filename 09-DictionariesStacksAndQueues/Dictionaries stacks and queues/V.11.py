import json
# Read the contents of the json file

with open('voting.json', mode ='r')as file:
    file_data = json.load(file)


    # Vote for a person
person_name = input('Name of the person you are voting for:')

voted = False

for key,value in file_data.items():
    if key == person_name:
        file_data[key] += 1
        voted = True   
if voted != True:
    file_data[person_name] = 1


    # Save voting data to json file
with open('voting.json', mode ='w')as file:
    json.dump(file_data,file)