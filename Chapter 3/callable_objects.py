""" Learning script """

class Book:
    """ Book class. """
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):

        return f'{self.title} by {self.author}, costs {self.price}'
    
    # TODO: the __call__ method can be used to call the object like a function
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book('War and Peace', 'Leo Tolstoy', 39.95)
b2 = Book('The Catcher in the Rye', 'JD Salingre', 29.95)

# TODO: call the object as if it were a function
print(b1)
# This is a way to change attributes in a very easy way
b1('Anna Karenina', 'Leo Tolstoy', 49.95)
print(b1)
