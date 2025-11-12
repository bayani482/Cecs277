from plate_decorator import PlateDecorator

class GreenBeans(PlateDecorator):
    
    def description(self):
        """
        Overrides the description method to add green beans to the plate.

        Returns:
            str: Description of the plate with green beans.
        """
        return super().description() + ", with green beans"
    
    def area(self):
        """
        Overrides the area method to account for green beans area.

        Returns:
            int: Remaining area after adding green beans.
        """
        return super().area() - 20
    
    def weight(self):
        """
        Overrides the weight method to account for green beans weight.

        Returns:
            int: Remaining weight after adding green beans.
        """
        return super().weight() - 3
    
    def count(self):
        """
        Overrides the count method to account for green beans.

        Returns:
            int: Number of food items on the plate.
        """
        return super().count() + 1