""" Marci M. McBride CSE 107 lab 10 """

class Library(object):
    """ Library object stores
    multiple objects and has methods to return statistics about those books. When printed, the
    object should list all of the books it contains in alphabetical order by author (as listed. You
    do not need to split into first and last names). """
    def __init__(self):
        self.book = []
        # return self
    def add_book(self, book):
        #self.book.append(book)
        if isinstance(book, str):
            book = book.split('\n')[0]
            newTitle = book.split(' by ')[0]
            newAuthor = book.split(' by ')[1]
            newBook = Book(newTitle, newAuthor)
            self.book.append(newBook)
        elif isinstance(book, Book):
            self.book.append(book)
    def get_authors(self):
        authors = []
        for i in self.book:
            if authors.count(i.author) == 0:
                authors.append(i.author)
        return authors
    def get_books_per_author(self):
        dictAuthors = {}
        for i in self.book:
            if i.author not in dictAuthors.keys():
                dictAuthors[i.author] = []
            dictAuthors[i.author].append(i.title)
        return dictAuthors
class Book(object):
    """
    stores the author and title of a book
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
