import random

class account:
    def __init__(self):
        self.account_no = random.randint(10000000000000000000000000,99999999999999999999999999)
        self.balance = 0
    def deposit(self,money):
        self.balance += money
    def withdraw(self,money):
        if money <= self.balance:
            self.balance -= money
        else:
            print("Insufficient funds on the account")
    def info(self):
        print(f"Bank account No:  ", end='')
    
        j = 0
        m = 0
        for i in str(self.account_no):
            if m < 2:
                print(str(self.account_no)[int(i)],end='')
                m += 1
                if m == 2:
                    print(" ",end='')
            else:   
                print(str(self.account_no)[int(i)],end='')
                j += 1
                if j%4 == 0:
                    print(" ",end='')
                    j = 0

        print(f"\nBalance: PLN {self.balance}")
        