from plate import Plate

class LargePlate(Plate):

    def description(self):
        """
        Overrides the description method for large plate details.
        
        Returns:
            str: Description of the large plate.
        """
        return "Flimsy 12 inch paper plate"
    
    def area(self):
        """
        Overrides the area method for large plate area.
        
        Returns:
            int: Area of the large plate."""
        return 113
    
    def weight(self):
        """
        Overrides the weight method for large plate weight.
        
        Returns:
            int: Weight capacity of the large plate.
        """
        return 24
    
    def count(self):
        """
        Overrides the count method for large plate item count.
        
        Returns:
            int: Number of food items on the large plate.
        """
        return 0