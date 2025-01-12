import json

# Open the JSON file in read mode
with open('reservations.json', 'r', encoding='utf-8') as file:
   # Load the data from the JSON file into a variable
   data = json.load(file)


#number of rooms
def num_of_rooms(data):
    return len(data['reservations'])

#number of paid reservations
def num_of_paid_rooms(data):
    count = 0
    for room in data['reservations']:
        if room['paid'] == True:
            count += 1
    return count
#number of unpaid reservations
def num_of_unpaid_rooms(data):
    count = 0
    for room in data['reservations']:
        if room['paid'] == False:
            count += 1
    return count
#total value of paid reservations
def value_of_paid_reservations(data):
    count = 0
    for room in data['reservations']:
        if room['paid'] == True:
            count += room["price_per_night"]
    return count
#total value of unpaid reservations
def value_of_unpaid_reservations(data):
    count = 0
    for room in data['reservations']:
        if room['paid'] == False:
            count += room["price_per_night"]
    return count
