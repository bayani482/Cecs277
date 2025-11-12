import abc
"""
An abstract base class/interface representing a generic plate.

Methods:
    description() -- Returns a string description of the plate and its contents.
    area() -- Returns the available area on the plate.
    weight() -- Returns the weight capacity of the plate.
    count() -- Returns the number of food items on the plate.
"""
class Plate(abc.ABC):
    @abc.abstractmethod
    def description(self):
        pass

    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def weight(self):
        pass

    @abc.abstractmethod
    def count(self):
        pass
    