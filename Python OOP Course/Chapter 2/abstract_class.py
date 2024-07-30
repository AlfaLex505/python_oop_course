""" Module for learning about abstract classes. """

# Using the abc library, ABC stands for "Abstract Base Class"
from abc import ABC, abstractmethod

class GraphicShape(ABC):
    """
    Creating an abstract class.
    """
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calc_area(self):
        """
        Calculating the area for the 2D shape.
        """
        pass


class Circle(GraphicShape):
    """
    Circle object.
    """
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    # Overwriting the calc_area method
    def calc_area(self):
        return 3.1416 * (self.radius ** 2)


class Square(GraphicShape):
    """
    Squarea object.
    """
    def __init__(self, side):
        super().__init__()
        self.side = side

    # Overwriting the calc_area method
    def calc_area(self):
        return self.side ** 2

# Trying to instantiate an abstract class
# test = GraphicShape() # This won't be possible

# Trying to instantiate some Circle and Square Objects
circle = Circle(10)
print(circle.calc_area())
square = Square(12)
print(square.calc_area())
