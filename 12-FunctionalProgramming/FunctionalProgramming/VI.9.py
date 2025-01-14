temp = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

res = list(filter(lambda x: x>0,temp.values()))


for key,value in temp.items():
    if value in res:
            print(key, '  ',end='')