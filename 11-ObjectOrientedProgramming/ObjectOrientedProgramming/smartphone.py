import contact
import contact_list

def main():
    l = contact_list.contact_list()
    
    person1 = contact.contact("John Brown","brown@onet.pl",555234000)
    person2 = contact.contact("Anna May","am@o2.pl ",232000199 )

    l.add_contact(person1)
    l.add_contact(person2)

    l.display_con()





main()