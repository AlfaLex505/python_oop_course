""" Learning module. """
# Checking classes and instances

# Creating the book class
class Book:
    """
    Creating a book class.
    """
    def __init__(self, title):
        self.title = title


class Newspaper:
    """
    Creating a newspaper class.
    """
    def __init__(self, name):
        self.name = name

# Creating some instances of these classes
book_1 = Book('Loki')
book_2 = Book('Norse Mythology')
newspaper_1 = Newspaper('The New York Times')
newspaper_2 = Newspaper('El informador')

# TODO: Use the type() function to inspect the object type
# print(f'The {book_1.title} is a {type(book_1)} of object.')
# print(f'The {newspaper_2.name} is a {type(newspaper_2)} of object.')

# # TODO: Comparing objects
# print(f'Is the object {book_1.title} the same type as {book_2.title}?')
# print(type(book_1) == type(book_2))
# print(f'Is the object {book_1.title} the same type as {newspaper_2.name}?')
# print(type(book_1) == type(newspaper_2))

# TODO: Using isinstance to compare a specific instance to a know type
# This is useful even for PEP8
print(isinstance(book_1, Book))
print(isinstance(newspaper_1, Newspaper))
print(isinstance(newspaper_2, Book))
print(isinstance(newspaper_2, object))
