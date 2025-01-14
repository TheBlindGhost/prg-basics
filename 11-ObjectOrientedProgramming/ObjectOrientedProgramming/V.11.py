class C:
    def __init__(self,stadion = {}):
        self.stadion = stadion
    def m1(self,s,n):
        self.stadion[s] = n
    def m2(self,s = ''):
        count = 0
        for i in s:
            for key,value in self.stadion.items():
                if i == key:
                   count += value 
        print(count)


a = C({"A":120,"D":150,"G":90,"K":110})
a.m1("G",130)
a.m2("GD")
a.m2("KEJ") 