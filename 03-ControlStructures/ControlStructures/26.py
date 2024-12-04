pin = 8005
i = 0



while i < 3:
    attempt = int(input('Type your PIN'))

    if attempt == pin:
        print('Good PIN')
        break
    else:
        print('Incorrect...')
        if i == 2:
            print('Sorry, your payment card has been blocked.')
            break   
        i+=1


