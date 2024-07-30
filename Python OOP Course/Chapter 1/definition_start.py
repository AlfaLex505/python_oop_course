""" Learning OOP script """
# Basic class definition

# TODO: Create a basic class

class Book:
    """
    Creating a class for books.
    """
    # Creating the initializer, that, according to the teacher is not the same
    # as a constructor.
    def __init__(self, title, author, pages, price):
        # Attributes
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        # Adding an attribute and making it unaccesible by putting two unders-
        # cores in front of it
        self.__secret = 'This is the secret attribute'

    def get_price(self):
        """
        Method to get the price of a book.
        """
        # We will get the return method by simply getting its attribute with
        # the dot notation, and applying a discount if its the case.

        # The function "hasattr" it's used to verify if we have the attribute
        # of the discount, in these example
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        """
        Creating a method to get a discount on the book.
        """
        # In this case, we are using the underscore at the beginning of the
        # discount to announce to other programmers that it's private
        self._discount = amount


# TODO: Create instances of the class
# Explanation of why the "init" method has two arguments, but it only gets one,
# when creating an object in python, it automatically passed the first argument
# as itself, in this case, the books, also the word "self" it just a naming
# convetion, I could name that any other way with no problem.
book_1 = Book('The phychology of Money', 'Morgan Mousel', 224, 269.99)
book_2 = Book('The Dumb Things Smart People Do with Their Money',
              'Jill Schlesinger', 253, 69)

# TODO: Print the class and the property
print(book_1)
# I can use the dot notation to access to the notatio of the property, in this
# case I'm using it to access the book's title.
print(f'The book title is: {book_1.title}')
print(f'The book price before discount is: {book_1.get_price()}')
book_1.set_discount(0.15)
print(f'The book price after a discount 15% is: {book_1.get_price()}')

# Trying to access to the private variable
# print(book_1.__secret) # Unable to access this way
print(book_1._Book__secret) # This way we can access the attribute
