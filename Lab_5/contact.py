class Contact:
    def __init__(self, fn, ln, ph, addr, city, zip):
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
        return f"{self.ln} {self.fn}\n{self.ph}\n{self.addr}\n{self.city}\n{self.zip}\n"
    
    def __repr__(self):
        return f"{self.fn},{self.ln},{self.ph},{self.addr},{self.city},{self.zip}"