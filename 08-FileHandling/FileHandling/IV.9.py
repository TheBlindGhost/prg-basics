import csv


# initializing the titles and rows list
fields = []
rows = []

with open("it_company.csv") as file:
    
    
    csvreader = csv.reader(file)

    fields = next(csvreader)

    print("GRAPHIC DESIGNERS\n=================")
    for row in csvreader:
        if row[2] == "Graphic Designer":
            print(f'{row[0]} {row[1]},{row[3]}' )




