from plate_decorator import PlateDecorator

class Stuffing(PlateDecorator):

    def description(self):
        """
        Overrides the description method to add stuffing details.
        
        Returns:
            str: Description of the plate with stuffing.
        """
        return super().description() + ", with stuffing"
    
    def area(self):
        """
        Overrides the area method to account for stuffing area.
        
        Returns:
            int: Remaining area after adding stuffing.
        """
        return super().area() - 18
    
    def weight(self):
        """
        Overrides the weight method to account for stuffing weight.
        
        Returns:
            int: Remaining weight after adding stuffing.
        """
        return super().weight() - 7
    
    def count(self):
        """
        Overrides the count method to account for stuffing.
        Returns:
            int: Number of food items on the plate.
        """
        return super().count() + 1
    
    