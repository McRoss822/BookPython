"""
Class for managing objects of Book class
"""


class BookManager:
    """
    class for managing book objects and searching certain objects by some criteria
    """

    def __init__(self):
        self.list_of_books = []

    def add_books(self, book):
        """
        adding objects to book_manager class object
        """
        self.list_of_books.append(book)

    def find_book_by_title(self, title):
        """
        find books by title
        """
        return list(filter(lambda book: book.title == title, self.list_of_books))

    def find_book_by_genre(self, genre):
        """
        find books by genre
        """
        return list(filter(lambda book: book.genre == genre, self.list_of_books))

    def __iter__(self):
        """
        turning manager list to iter
        """
        if self.list_of_books is not None:
            return iter(self.list_of_books)
        else:
            raise

    def __len__(self):
        """
        returning length of manager list
        """
        if self.list_of_books is not None:
            return len(self.list_of_books)
        else:
            raise

    def __getitem__(self, item):
        """
        returning given item if it`s on the list
        """
        if self.list_of_books and self.list_of_books[item] is not None:
            return self.list_of_books[item]
        else:
            raise

    def results(self):
        """
        returns results of has_more_books method`s work
        """
        for book in self.list_of_books:
            book.has_more_books()
        return [book.current_quantity() for book in self.list_of_books]

    def result_list(self):
        """
        returns list of objects and results
        """
        return enumerate(self.list_of_books)

    def zipper(self):
        """
        returns object + result of method work
        """
        result_list = tuple(self.results())
        object_list = tuple(self.list_of_books)
        return zip(result_list, object_list)

    def all_arguments_by_type(self, type):
        arguments = self.__dict__
        return {k:v for (k, v) in arguments if v == type}

    def conditions_list(self):
        return {
            'any': any(book.has_more_books() for book in self.list_of_books),
            'all': all(book.has_more_books() for book in self.list_of_books)
        }