from plate_decorator import PlateDecorator

class Potatoes(PlateDecorator):

    def description(self):
        """
        Overrides the description method to add potatoes details.
        
        Returns:
            str: Description of the plate with potatoes.
        """ 
        return super().description() + ", with potatoes"
    
    def area(self):
        """
        Overrides the area method to account for potatoes area.

        Returns:
            int: Remaining area after adding potatoes.
        """
        return super().area() - 18
    
    def weight(self):
        """
        Overrides the weight method to account for potatoes weight.
        
        Returns:
            int: Remaining weight after adding potatoes.
        """
        return super().weight() - 6
        
    def count(self):
        """
        Overrides the count method to account for potatoes.
        
        Returns:
            int: Number of food items on the plate.
        """
        return super().count() + 1
    