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
            if len(contactInfo) == 6:  # make sure data is valid
                person = Contact(*contactInfo)
                address_list.append(person)

        address_list.sort(key=lambda c: (c.ln,c.fn))
    return address_list

def write(contacts):
    with open("addresses2.txt","w") as addresses:
        for contact in contacts:
            addresses.write(repr()contact + "\n")
        
def get_menu_choice():
    userInput = int(check_input.get_int_range("\n1.Display Contacts\n2.Add Contacts\n3.Search Contacs\n4.Modify Contacts\n5.Save and Quit\n>", 1, 5))
    return userInput
def modify_contact(cont):
    print("modify_contact")


def main():
    contact = read_file()
    play = True
    while play:
        get_menu_choice()
        if get_menu_choice() == 5:
            play = False

if __name__ == '__main__':
    main()