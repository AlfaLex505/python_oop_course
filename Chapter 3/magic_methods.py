# Learning the first two magic methods, "__str__" & "__repr__"
""" Learning module """

# Creating the first class "Book"
class Book:
    """ Book class. """
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: Use the __str__ method to return a string
    # This method is a way of the object to describe itslef with a simple
    # string, its ussually used to display it to the user
    def __str__(self):
        return f'{self.title} by {self.author}, costs {self.price}'


    # TODO: Use the __repr__ method to return an obj representation
    # The repr method does something similiar of the str method, but this
    # method give information that is more useful for programmers debugging
    def __repr__(self):
        return (f'title = {self.title}\nauthor = {self.author}\n'
                f'price = {self.price}')


# Creating new objects for demonstration
b1 = Book('War and Peace', 'Leo Tolstoy', 39.95)
b2 = Book('The Catcher in the Rye', 'JD Salinger', 29.95)

print(b1)
print(b2)
print(str(b1))
print(repr(b2))
