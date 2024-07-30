""" Learning script. """
# Implementing default values in dataclasses

from dataclasses import dataclass, field
import random

def price_func():
    """ Function dor getting random prices """
    return float(random.randrange(20, 40))

@dataclass
class Book:
    """ Book class. """
    # You can define default values when attributes are declared
    title: str = 'No title'
    author: str = 'No author'
    pages: int = 0
    # using the field way of adding a default value
    # price: float = field(default = 10.0)
    price: float = field(default_factory = price_func)

b1 = Book('War and Peace', 'Leo Tolstoy', 1225)
b2 = Book('The Catcher in the Rye', 'JD Salinger', 234)
print(b1)
print(b2)
