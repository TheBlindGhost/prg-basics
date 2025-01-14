bottles = [508,500,512,499,492,511,503,476,501,509]

ideal = 500
def toler(limit,ideal):
    return lambda x: x < ideal+(ideal*limit) and x > ideal - (ideal*limit)

a = toler(0.02,ideal)

res = list(filter(lambda x: a(x),bottles))

inc = (len(bottles)-len(res))/len(bottles)

print(f'Incorrectly filled: {round(inc*100)} %')