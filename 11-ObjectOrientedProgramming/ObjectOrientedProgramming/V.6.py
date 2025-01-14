import bank

def main():
    acc = bank.account()
    

    acc.info()
    acc.deposit(25.30)
    acc.info()
    acc.withdraw(12.17)
    acc.info()
    acc.withdraw(14)
    acc.info()

if __name__ == "__main__":
    main()
