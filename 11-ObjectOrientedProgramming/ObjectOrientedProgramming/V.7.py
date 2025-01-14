import statistics
class number:
    def __init__(self):
        self.numbers = []
        self.max = 0
        self.min = 0
        self.amean = 0
        self.median = 0
    def add_number(self):
        num = int(input('What number to add?'))
        self.numbers.append(num)
    
    def display(self):
        for i in self.numbers:
            print(f"{i} ",end='')
        print()
    
    def greatest(self):
        self.max = max(self.numbers)
        print(f"Greatest number is: {self.max}")
    
    def smallest(self):
        self.min = min(self.numbers)
        print(f"Smallest num is {self.min}")
    
    def mean(self):
        self.amean = statistics.mean(self.numbers)
        print(f"The mean is {self.amean}")
    
    def med(self):
        self.median = statistics.median(self.numbers)
        print(f"The median is {self.median}")

def main():
    n = number()
    n.add_number()
    n.add_number()
    n.add_number()
    n.add_number()
    n.add_number()
    n.display()
    n.greatest()
    n.smallest()
    n.mean()
    n.med()


main()