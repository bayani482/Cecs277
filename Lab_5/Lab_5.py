"""
LAB 5

Student 1: Javier Jacobo
Student 2: Bryan Bayani

This is a progam that reads a file of contacts and puts them into a list. The user would then be able view,search and manipulate the list by adding someone to it 


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
            addresses.write(repr(contact) + "\n")
def get_menu_choice():
    userInput = int(check_input.get_int_range("\n1.Display Contacts\n2.Add Contacts\n3.Search Contacts\n4.Modify Contacts\n5.Save and Quit\n>", 1, 5))
    return userInput
def modify_contact(cont):
    
    while True:
        userModify = int(check_input.get_int_range(f"\nModifying Menu: {cont.fn} {cont.ln}\n1. First Name>\n2. Last Name\n3. Phone Number\n4. Street Address\n5. City\n6. Zip\n7. Save\n>", 1, 7))
        match userModify:
            case 1:
                cont.fn = input("Enter First name: ").strip().capitalize()
            case 2:
                cont.ln = input("Enter First name: ").strip().capitalize()
            case 3:
                cont.ph = input("Enter Phone: ").strip()
            case 4:
                cont.addr = input("Enter Address: ").strip()
            case 5:
                cont.city = input("Enter City: ").strip()
            case 6:
                cont.zip = input("Enter Zip: ").strip()
            case 7:
                continue
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
                print("\nEnter new contact information:")
                fn = input("First name: ").strip().capitalize()
                ln = input("Last name: ").strip().capitalize()
                ph = input("Phone number: ").strip()
                addr = input("Street address: ").strip()
                city = input("City: ").strip()
                zip_code = input("Zip code: ").strip()
                contact.append(Contact(fn, ln, ph, addr, city, zip_code))
            case 3:# Search Contacts
                search = int(check_input.get_int_range("\nSearch contacts\n1. Search by Last Name\n2. Search by zip code\n>", 1, 2))
                matches = []
                match search:
                    case 1:#search by last name
                        lastNameSearch = input("Enter Last Name:").strip().capitalize()
                        searchContact = Contact("", lastNameSearch, "", "", "", "")
                        for i in contact:
                            if i.ln == lastNameSearch:
                                matches.append(i)
                        if matches:
                            for c in matches:
                                print(c)
                        else:
                            print("No matches found")
                    case 2:# search by zip
                        zipSearch = input("Enter zip:").strip()
                        searchContact = Contact("", "", "", "", "", zipSearch)
                        for i in contact:
                            if i.zip == zipSearch:
                                matches.append(i)
                        if matches:
                            for c in matches:
                                print(c)
                        else:
                            print("No matches found")
            case 4:#Modify Contacts
                firstNameSearch = input("Enter first Name:").strip().capitalize()
                lastNameSearch = input("Enter Last Name:").strip().capitalize()
                searchContact = Contact(firstNameSearch, lastNameSearch, "", "", "", "")
                
                modify_contact(searchContact)
            case 5:#Save & Quit
                write(contact)
                print("\nSaving File...\nEnding Program")
                play = False

if __name__ == '__main__':
    main()