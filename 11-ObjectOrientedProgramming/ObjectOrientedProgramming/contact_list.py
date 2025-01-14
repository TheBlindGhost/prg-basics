import contact


class contact_list:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self,obj): 
        self.contacts.append(obj)
    
    
    def display_con(self):
        for obj in self.contacts:
            print(obj.who())