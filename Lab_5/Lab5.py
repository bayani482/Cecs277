"""
LAB 5

Student 1: Javier Jacobo
Student 2: Bryan Bayani

"""


from contact import Contact

def main():
    address_list = []
    with open("addresses.txt","r") as addresses:
        for line in addresses:
            address_list.append(line)

    print(f"Number of contacts: {len(address_list)}")
    for key, value in enumerate(address_list):
        print(f"{value} | {key + 1}")
        
if __name__ == '__main__':
    main()