""" Learning script """
# Using class level and static methods

class Book:
    """
    Creating a book class.
    """
    #TODO: Properties defined at the class level are shared by all instances
    # Creating a class variable that stores the book types, declare it in
    # capital letters for acknowledgement that this is a class variable
    BOOK_TYPES = ('Hardcover', 'Paperback', 'eBook')

    #TODO: double-underscore properties are hidden from other classes
    __booklist = None # This is a private variable

    #TODO: Create a class method
    # Using the class method decorator
    @classmethod
    # Function to get the permitted book types
    def getbooktypes(cls):
        """
        Class method to return the permitted book types.
        """
        # This will work only on a class instances, not in an object instance
        return cls.BOOK_TYPES

    #TODO: Create a Static Method
    @staticmethod
    def getbooklist():
        if Book.__booklist is None:
            Book.__booklist = []

        return Book.__booklist

    # Instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, new_title):
        self.title = new_title

    def __init__(self, title, booktype):
        self.title = title
        if not booktype in Book.BOOK_TYPES:
            raise ValueError(f'{booktype} is not a valid book type.')
        else:
            self.booktype = booktype


# TODO: Access the class attributes
print(f'The book types are: {Book.getbooktypes()}')

# TODO: Create some book instances

# TODO: Create some objects
book_1 = Book('Title 1', 'eBook')
# book_2 = Book('Title 2', 'Comic') # NOTE: This book won't be an real object
# because we don't have a permitted book type
book_2 = Book('Title 2', 'Paperback')

# TODO: Use the static method to access a singleton
the_books = Book.getbooklist()
the_books.append(book_1)
the_books.append(book_2)
print(the_books)
