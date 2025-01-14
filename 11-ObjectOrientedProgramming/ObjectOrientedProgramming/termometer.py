
class termometer:
    def __init__(self):
        self.temp = 0
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    
    def measure(self,temp):
        if self.is_on == True:
            if temp < 32 or temp > 42:
                print("Invalide temperature")
            else:
                self.temp = temp
        else:
            print('Thermometer off')
    def show_resault(self):
        if self.is_on == True:
            if self.temp >= 37 and self.temp < 41:
                print(f"Temperature: {self.temp} C ", end='')
                print("feaver")
            elif self.temp >= 41:
                print(f"Temperature: {self.temp} C ",end='')
                print("CRITICAL TEMPERATURE!!")
            else:
                print(f"Temperature: {self.temp} C")
        else:
            print('Thermometer off')

            