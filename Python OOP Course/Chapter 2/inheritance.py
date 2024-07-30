""" Script for understanding the inheritance """

# Defining our classes with inheritance
# First "publication" super class
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


# This class will inherit from the publication class
class Book(Publication):
    def __init__(self, title, price, author, pages):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher


class Magazine(Periodical):
    """
    Creating a Magazine class.
    """
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)


class Newspaper(Periodical):
    """
    Creating a Newspaper class.
    """
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price, period, publisher)


book_1 = Book('Brave New World', 'Aldous Huxlet', 311, 29.0)
newspaper_1 = Newspaper('NY Times', 6.0, 'Daily', 'New York Times Company')
magazine_1 = Magazine('Scientific American', 'Springer Nature', 5.99,
                      'Monthly')

print(book_1.author)
print(newspaper_1.publisher)
print(book_1.price, magazine_1.price, newspaper_1.price)
