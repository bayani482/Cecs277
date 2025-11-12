from plate_decorator import PlateDecorator

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