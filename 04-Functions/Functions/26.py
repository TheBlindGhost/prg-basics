def f(text):
    string = ''
    for lett in range(len(text)):
        string += text[lett]
        if lett < len(text)-1:
            string += '-'
    return print(string)


f("Univesity") #returns "U-n-i-v-e-r-s-i-t-y"
f("UE") #returns "U-E"
f("x") #returns "x"
f("") #returns ""