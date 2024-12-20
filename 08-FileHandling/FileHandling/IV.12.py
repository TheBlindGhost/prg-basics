import csv
from pathlib import Path
import os

generas = []


with open("books.csv","r") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
         generas.append(row[2])
    generas = set(generas)


for gen in generas:
    path = Path(f'{gen}.txt')
    if path.is_file():
        os.remove(f"{gen}.txt")
    open(f"{gen}.txt",'x')
        
    with open (f"{gen}.txt", "w") as g:
        with open("books.csv","r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if row[2] == gen:
                    g.write(f'{str(row)}\n')



