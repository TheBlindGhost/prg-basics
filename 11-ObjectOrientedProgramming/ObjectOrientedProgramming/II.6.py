class Phone():
    def __init__(self,model,price,maker):
        self.model = model
        self.price = price
        self.maker = maker
    def show_price(self):
        print(f"This phone cost {self.price}")
    def update_model(self,model):
        print(f"Phone model {self.model} was updated ", end = '')
        self.model = model  
        print(self.model)
    def info(self):
        print(f"The phone {self.model} made by {self.maker} cost {self.price}.")

def main():
    p1 = Phone('A20',200,'Samsung')
    print(p1.model)
    p1.show_price()      
    p1.update_model('A30')
    p1.info()

main()