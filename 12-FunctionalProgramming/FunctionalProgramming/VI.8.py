points = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
   return lambda pts: pts>=limit

lim70 =min_pts(70)
lim40 =min_pts(40)
lim30 =min_pts(30)

t1 = list(filter(lambda x: lim70(x),points))
t2 = list(filter(lambda x : lim40(x),points))
t3 = list(filter(lambda x: lim30(x),points))

print(t1)
print(t2)
print(t3)