import csv
with open("clothing.csv") as file:
    
    
    csvreader = csv.reader(file)

    fields = next(csvreader)

    print("Products\n")
    for row in csvreader:
        if float(row[5]) < 60 and int(row[6])<40:
            print(f'{row[1]} {row[2]} {row[3]} {row[4]} {row[5]} {row[6]}' )
