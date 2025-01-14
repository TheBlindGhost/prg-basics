
names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']


sor = lambda a: len(a)

sorte = sorted(names,key=sor)
print(sorte)