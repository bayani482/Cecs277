from plate_decorator import PlateDecorator
"""
A class representing turkey on a plate. Inherits from the PlateDecorator class.

Methods:
    description() -- Returns a string description of the plate with turkey.
    area() -- Returns the available area on the plate after adding turkey.
    weight() -- Returns the weight capacity of the plate after adding turkey.
    count() -- Returns the number of food items on the plate after adding turkey.
"""
class Turkey(PlateDecorator):
    
    def description(self):
        """
        Overrides the description method to add turkey details.
        
        Returns:
            str: Description of the plate with turkey.
        """ 
        return super().description() + ", with turkey"
    
    def area(self):
        """
        Overrides the area method to account for turkey area.
        
        Returns:
            int: Remaining area after adding turkey.
        """
        return super().area() - 15
    
    def weight(self):
        """
        Overrides the weight method to account for turkey weight.

        Returns:
            int: Remaining weight after adding turkey.
        """
        return super().weight() - 4
    
    def count(self):
        """
        Overrides the count method to account for turkey.
        
        Returns:
            int: Number of food items on the plate.
        """
        return super().count() + 1