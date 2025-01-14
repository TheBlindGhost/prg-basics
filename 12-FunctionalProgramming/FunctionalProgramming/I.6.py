dist = int(input("distance(km)"))
h = int(input("time(h)"))
m = int(input("time(m)"))

avg_speed = lambda distance,hours,minutes: distance/(hours+(minutes/60))

print(avg_speed(dist,h,m))