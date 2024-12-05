def f(dice):
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    for num in range(len(dice)):
        if dice[num] == '1':
            a1 += 1
        elif dice[num] == '2':
            a2 += 1
        elif dice[num] == '3':
            a3 += 1
        elif dice[num] == '4':
            a4 += 1
        elif dice[num] == '5':
            a5 += 1
        elif dice[num] == '6':
            a6 += 1
    num = [a1,a2,a3,a4,a5,a6]
    return print(num.index(max(num))+1)

f("5233165554211") #returns 5
f("2133") #returns 3