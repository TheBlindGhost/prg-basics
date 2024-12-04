EAN_13 = 5901230094938

if len(str(EAN_13)) == 13:
    print('Article number is correct')
    
    if str(EAN_13)[0:3] == '590':
        print('Article manufactured in Poland')
else:
    print('Wrong code!!')