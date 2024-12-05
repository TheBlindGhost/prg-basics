def f(palindrome):
    pal = reversed(palindrome)
    for num in palindrome:
        for lett in pal:
            if lett != num:
                return print(False)
            else:
                break
    return print(True)


f("radar") #returns True
f("12-11-21") #returns True
f("book") #returns False