def f(number):
    amount = 0
    str_num = str(number)
 
    for i in range(len(str_num)):
        for j in range(i+1, len(str_num)):
            if str_num[i] == str_num[j]:
                amount += int(str_num[i])

    return print(amount)
        
                


f(1027) #returns 0
f(230335) #returns 9    
f(513553007) #returns 21