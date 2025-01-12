countries = [
{"name":"Poland ", "population":38000000},
{"name":"Germany", "population":3768000000},
{"name":"USA    ", "population":380026575600},
{"name":"China  ", "population":380},
{"name":"India  ", "population":380060000},
]
print('COUNTRY   POPULATION' )
for country in countries:
    for key,value in country.items():
        print(value, end='   ')
    print()
