import csv

region = {}
count = {}

with open('province.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        region[lines[0]] = lines[1]
region.pop("Letter")



with open('vehicle.txt', 'r')as file:
    vehicle = file.read()
    for line in vehicle.splitlines():
        for key,value in region.items():
            if key == line[0]:
                if value in count:
                    count[value] += 1
                else:
                    count[value] = 1
print(count)