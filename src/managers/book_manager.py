
"""
docstring
"""
class BookManager():
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
        