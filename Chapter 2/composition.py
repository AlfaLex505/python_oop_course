""" Learning about composition """

# Creating a class book, this class wil be compused from author class
class Book:
    """ Book class """
    def __init__(self, title, price, author = None):
        self.price = price
        self.title = title
        # Author object down here!
        self.author = author
        self.chapters = []

    def add_chapter(self, chapter):
        """ Function """
        self.chapters.append(chapter)


    def getbook_pagecount(self):
        """ Function """
        total = 0
        for chapter in self.chapters:
            total += chapter.page_count
        return total


class Author:
    """ Author class """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Chapter:
    """ Chapter class """
    def __init__(self, name, page_count):
        self.name = name
        self.page_count = page_count

# Adding some objects
auth = Author('Leo', 'Tolstoy')
b1 = Book('War and Peace', 39.0, auth)
# Adding some chapters
b1.add_chapter(Chapter('Chapter 1', 125))
b1.add_chapter(Chapter('Chapter 2', 97))
b1.add_chapter(Chapter('Chapter 3', 143))

print(b1.author)
print(b1.title)
print(b1.getbook_pagecount())
