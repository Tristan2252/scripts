Debug = False  # used for debugging, if True then in Debug mode


class Library(object):

    def __init__(self):
        """
        initializes dictionary to sto books
        :return: None
        """
        self.library_dict = {}

    def add_book(self, book):
        """
        takes in self and book, if book is a string the string is split in
        correct format to be added to the dictionary, if book is a Book obj
        then the author and tile of the Book obj is added to the dictionary
        :param book: str, Book()
        :return: None
        """
        if isinstance(book, str):
            book_input = book.split("\n")[0]
            title, author = book_input.rsplit(" by ", 1)
            self.library_dict[author] = title

        else:
            self.library_dict[book.author] = book.title

    def get_authors(self):
        """
        gets every author in the dictionary by iterating through it and
        adding every key to a temp list to be returned
        :return: [] # sorted temp list
        """
        temp_lst = []
        for author in self.library_dict:
            temp_lst.append(author)

        return sorted(temp_lst)

    def get_books_per_author(self):
        """
        returns every book per author in a dictionary fromat
        :return: {} # dictionary of books
        """
        return self.library_dict


class Book(object):

    def __init__(self, title, author):
        """
        takes in two strings and assigns them to author and tile
        :param title: str # title of the book
        :param author: str # author of the book
        :return: None
        """
        self.author = author
        self.title = title


def library():

    if Debug:
        lib = Library()
        lib.add_book("Abhorsen Trilogy by Garth Nix")
        lib.add_book("Aladore by Henry Newbolt")
        lib.add_book("The Belgariad series by David Eddings")
        print(lib.get_authors())

    else:
        pass

if __name__ == '__main__':
    library()