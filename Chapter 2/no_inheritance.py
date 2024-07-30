""" Script for understanding the inheritance """

# Defining our first classes with no inheritance
class Book:
    """
    Creating a Book class.
    """
    def __init__(self, title, author, pages, price):
        self.title = title
        self.price = price
        self.author = author
        self.pages = pages


class Magazine:
    """
    Creating a Magazine class.
    """
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.price = price
        self.period = period
        self.publisher = publisher


class Newspaper:
    """
    Creating a Newspaper class.
    """
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.price = price
        self.period = period
        self.publisher = publisher


book_1 = Book('Brave New World', 'Aldous Huxlet', 311, 29.0)
newspaper_1 = Newspaper('NY Times', 'New York Times Company', 6.0, 'Daily')
magazine_1 = Magazine('Scientific American', 'Springer Nature', 5.99,
                      'Monthly')


print(book_1.author)
print(newspaper_1.publisher)
print(book_1.price, magazine_1.price, newspaper_1.price)
