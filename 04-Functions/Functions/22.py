def f(name):
    acronym = ''
    acronym += name[0]
    for i in range(len(name)):
        if name[i] == ' ':
            acronym += name[i+1]
    return print(acronym)

f("Internet of Things") #returns "IoT"
f("For Your Information") #returns "FYI"
f("Python") #returns "P"