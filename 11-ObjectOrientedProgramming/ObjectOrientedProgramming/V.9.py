class C:
    def __init__(self,name,surname,age,seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority
        self.tag = ''
    def __str__(self):
        tag = ''
        tag += self.surname
        tag += self.name[0]
        tag += str(self.seniority)
        if self.age >= 18:
            tag = tag.upper()
        else:
            tag = tag.lower()
        return tag

a = C("Anna","May",17,7)
b = C("Grege","Brown",21,4)
print(a)
print(b)

