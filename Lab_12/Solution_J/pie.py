from plate_decorator import PlateDecorator
"""
A class representing a pie on a plate. Inherits from the PlateDecorator class.

Methods:
    description() -- Returns a string description of the plate with pie.
    area() -- Returns the available area on the plate after adding pie.
    weight() -- Returns the weight capacity of the plate after adding pie.
    count() -- Returns the number of food items on the plate after adding pie.
"""
class Pie(PlateDecorator):
    
    def description(self):
        """
        Overrides the description method to add pie details.
        
        Returns:
            str: Description of the plate with pie.
        """
        return super().description() + ", with pie"
    
    def area(self):
        return super().area() - 19
    
    def weight(self):
        return super().weight() - 8
    
    def count(self):
        return super().count() + 1