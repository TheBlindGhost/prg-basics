def f(password):
    if len(password) >= 6:
        str_num = str(password)
        
        for i in range(len(str_num)):
            for j in range(i+1, len(str_num)):
                if str_num[i] == str_num[j]:
                    return print(False)
        return print(True)
    else:
        return print(False)

        
f("ax15") #returns False
f("book123") #returns False
f("A2water3") #returns True
f("qwerty") #returns True
f("") #returns False