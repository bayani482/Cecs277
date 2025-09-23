"""
LAB 5

Student 1: Javier Jacobo
Student 2: Bryan Bayani

"""
import check_input
from contact import Contact


def read_file():
    address_list = []
    with open("addresses.txt","r") as addresses:
        for line in addresses:
            contactInfo = line.strip().split(",")
            if len(contactInfo) == 6:
                person = Contact(*contactInfo)
                address_list.append(person)

        address_list.sort(key=lambda c: (c.ln,c.fn))
    return address_list

def write(contacts):
    with open("addresses2.txt","w") as addresses:# change back to addresses.txt debug
        for contact in contacts:
            addresses.write(repr(contact) + "\n")#
        
def get_menu_choice():
    userInput = int(check_input.get_int_range("\n1.Display Contacts\n2.Add Contacts\n3.Search Contacts\n4.Modify Contacts\n5.Save and Quit\n>", 1, 5))
    return userInput

def modify_contact(cont):
    print("modify_contact")

def main():
    contact = read_file()
    play = True
    while play:
        userChoice = get_menu_choice()

        match userChoice:
            case 1:#display contacts
                print(f"Number of contacts: {len(contact)}")
                for key, value in enumerate(contact):
                    print(f"{key + 1}. {value}")
            case 2:# Add Contacts
                print("add contacts")
            case 3:# Search Contacts
                print("search contacts")
            case 4:#Modify Contacts
                write(contact)
                print("modify contacts")
            case 5:#Save & Quit
                play = False

if __name__ == '__main__':
    main()