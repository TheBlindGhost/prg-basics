score = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]


final = list(map(lambda x: sum(x)-max(x)-min(x),score))        


print(final)