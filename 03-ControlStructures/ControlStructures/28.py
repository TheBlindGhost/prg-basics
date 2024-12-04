t1 = 0
t2 = 1

print(f'{t1} ', end='')
print(f' {t2} ', end='')
for number in range (20):
    t3 = t1+t2
    t1 = t2
    t2 = t3
    print(f' {t3} ', end='')