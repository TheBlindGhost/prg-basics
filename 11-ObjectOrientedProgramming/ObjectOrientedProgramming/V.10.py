class C:
    def __init__(self,points = []):
        self.points = points
    def m(self,n):
        t = 0
        count = 0
        for i in self.points:
            for j in i:
                if j > 0:
                    t += 1
                    continue
                else:
                    break
            if t == 2:
                count +=1
                t = 0
            else:
                t = 0
        if count >= n:
            return True
        else:
            return False
        

a = C([[2,3],[1,8],[-6,4],[3,-7]])
print(a.m(2))
print(a.m(3))