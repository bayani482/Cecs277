import abc
from plate import Plate
"""
An abstract decorator class for plates. Inherits from the Plate interface.

Methods:
    description() -- Returns a string description of the plate and its contents.
    area() -- Returns the available area on the plate.
    weight() -- Returns the weight capacity of the plate.
    count() -- Returns the number of food items on the plate.
"""

class PlateDecorator(Plate, abc.ABC):
    
    def __init__(self,p):
        self._plate = p
    
    def description(self):
        return self._plate.description()
    
    def area(self):
        return self._plate.area()

    def weight(self):
        return self._plate.weight()

    def count(self):
        return self._plate.count()