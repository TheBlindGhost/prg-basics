hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]
def hotel_list(hotel):
    i = 0
    hotel_names = ""
    for hot in hotel:
        for key,value in hot.items():
            if key == "name":
                i += 1
                hotel_names += value
                if i < len(hotels_in_Krakow):
                    hotel_names += ","
    return hotel_names
            
def avg_price(hotel):
    total = 0            
    for hot in hotel:
        for key,value in hot.items():
            if key == "price":
                total += value
    avrage = round((total/len(hotel)))
    return avrage

print(f"Hotels in Krakow: {hotel_list(hotels_in_Krakow)}")
print(f"Average hotel price in Krakow: {avg_price(hotels_in_Krakow)}")
print(f"Hotels in Sopot: {hotel_list(hotels_in_Sopot)}")
print(f"Average hotel price in Sopot: {avg_price(hotels_in_Sopot)}")
if avg_price(hotels_in_Krakow) < avg_price(hotels_in_Sopot):
    print("Cheaper hotels in: Krakow")
else:
    print("Cheaper hotels in: Sopot")

    


