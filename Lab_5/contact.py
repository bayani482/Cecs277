class Contact:
    """creates a contact object .
    Attributes:
    fn (str): first name.
    ln (str): last name.
    ph (str): phone.
    addr (str): address.
    city (str): city.
    zip (str): zip.
    """
    def __init__(self, fn, ln, ph, addr, city, zip):
        """Initializes the contact information.
        Args:
        fn (str): first name set from argument.
        ln (str): last name set from argument.
        ph (str): phone set from argument.
        addr (str): address set from argument.
        city (str): city set from argument.
        zip (str): zip set from argument.
        """
        self.fn = fn
        self.ln = ln
        self.ph = ph
        self.addr = addr
        self.city = city
        self.zip = zip

    def __lt__(self,other):
        if self.ln != other.ln:
            return self.ln < other.ln
        return self.fn < other.fn
            
    def __str__(self):
        """Returns the contact object as a formatted string.
        Returns:
        str: A string with first name, last name, phone, address, city, zip.
        """
        return f"{self.ln} {self.fn}\n{self.ph}\n{self.addr}\n{self.city}\n{self.zip}\n"
    
    def __repr__(self):
        """Returns the rectangle as a formatted string.
Returns:
str: A string with location, width, and height.
"""
        return f"{self.fn},{self.ln},{self.ph},{self.addr},{self.city},{self.zip}"