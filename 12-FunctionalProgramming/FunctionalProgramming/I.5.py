dist = int(input("distance(km)"))
h = int(input("time(h)"))
m = int(input("time(m)"))
def avg_speed(distance,hours,minutes):
    totalm = (hours*60) + minutes
    avrage = distance/(totalm/60)
    print(round(avrage,2))

avg_speed(dist,h,m)