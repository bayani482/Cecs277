from plate import Plate

class SmallPlate(Plate):

    def description(self):
        """
        Overrides the description method for small plate details.
        
        Returns:
            str: Description of the small plate.
            """
        return "Sturdy 10 inch paper plate"
    
    def area(self):
        """
        Overrides the area method for small plate area.
        
        Returns:
            int: Area of the small plate.
        """
        return 78
    
    def weight(self):
        """
        Overrides the weight method for small plate weight.
        
        Returns:
            int: Weight capacity of the small plate.
        """
        return 32
    
    def count(self):
        """
        Overrides the count method for small plate item count.

        Returns:
            int: Number of food items on the small plate.
        """
        return 0