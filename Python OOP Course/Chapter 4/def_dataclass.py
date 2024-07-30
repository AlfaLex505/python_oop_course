""" Learning script about data classes. """

# Importing the data classes library for representing data objects
from dataclasses import dataclass

# Using the dataclass decorator indicating that the Book class is a datatype
# class
@dataclass
class Book:
    """
    Book class.
    """
    title : str
    author : str
    pages : int
    price : float

    # Adding methods its pretty straightforward
    def book_info(self):
        """
        Method for getting book information.
        """
        return f'{self.title} by {self.author}'


# Creating some instances
b1 = Book('War and Peace', 'Leo Tolstoy', 1225, 39.95)
b2 = Book('The Catcher in the Rye', 'JD Salinger', 234, 29.95)
b3 = Book('The Catcher in the Rye', 'JD Salinger', 234, 29.95)

# Access fields
# print(b1.title)
# print(b2.title)

# # TODO: Print the book itself - dataclasses implement __repr__
# print(b1)

# # TODO: Comparing two dataclasses - they implement __eq__
# print(b1 == b3)

# TODO: Change some fields
b1.title = 'Ana Karenina'
b1.pages = 864
print(b1.book_info())
