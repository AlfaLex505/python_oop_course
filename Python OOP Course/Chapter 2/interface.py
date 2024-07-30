# Interfaces are sort of like a contract or promise that some class will be
# able to do some capability

from abc import ABC, abstractmethod

# Adding another abstract class for convert this shapes to JSON's
class JSONify(ABC):
    """ JSON class """
    @abstractmethod
    def to_json(self):
        """ To Json function """
        pass

class GraphicShape(ABC):
    """ GraphicShape class """
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calc_area(self):
        """ Calc area class """
        pass


class Circle(GraphicShape, JSONify):
    """ Circle class """
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        """ Calculating area function """
        return 3.1416 * (self.radius ** 2)

    def to_json(self):
        return f'Returning some json stuff {self.calc_area}'

circle_1 = Circle(10)
print(circle_1.calc_area())
print(circle_1.to_json())
