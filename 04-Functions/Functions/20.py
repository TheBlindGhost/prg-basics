def f(n):
    count = 0
    for possiblePrime in range(2,100000000000):
        
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
        
        if isPrime:
            count += 1
            if count == n:
                return print(possiblePrime)

        
f(1) #returns 2
f(5) #returns 11
