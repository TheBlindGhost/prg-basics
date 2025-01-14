class taxi:
    def _init_(self, distamce, rate):
        self.distamce = 0
        self.rate = 0
    def fare(self):
        return self.distamce * self.rate
    def print_receipt(self):
        print(f'The customer rode for {self.distamce}, the rate is {self.rate}. The finall rate is {self.fare()}.')

ride1 = taxi()
ride2 = taxi()
ride1.distamce = 10
ride1.rate = 50
ride2.distamce = 1000
ride2.rate = 9

print(ride1.print_receipt())
print(ride2.print_receipt())

    