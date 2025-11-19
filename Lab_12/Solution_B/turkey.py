from plate_decorator import PlateDecorator

class Turkey(PlateDecorator):
    def description(self):
        return super().description() + ", with turkey"
    
    def area(self):
        return super().area() - 15
    
    def weight(self):
        return super().weight() - 4
    
    def count(self):
        return super().count() + 1