def f(n):
    i = 1
    string = ''
    while i <= n:
        string += str(i)
        i += 1
    return print(string)

f(11) #returns "1234567891011"
f(4) #returns "1234"