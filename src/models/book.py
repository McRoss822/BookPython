"""
Book class module
"""
from src.decorators import exception_logger
from abc import ABC, abstractclassmethod, abstractmethod
from exceptions import OutOfBooksException


class Book(ABC):
    """
   abstract book class
    """
    __instance = None

    # pylint:disable=too-many-arguments
    def __init__(self, title=None, publisher=None, year=None, genre=None, count_in_warehouse=None ):
        self.title = title
        self.publisher = publisher
        self.year = year
        self.genre = genre
        self.count_in_warehouse = count_in_warehouse

    @staticmethod
    def get_instance():
        """
        returns instance
        """
        if Book.__instance is None:
            Book.__instance = Book()
        else:
            Book.__instance = None
        return Book.__instance

    def has_more_books(self):
        """
        returns true if books are in warehouse
        """
        if self is not None:
            return True

    def current_quantity(self):
        """
        returns count in warehouse
        """
        return self.count_in_warehouse

    @exception_logger(OutOfBooksException, "file")
    def get_book(self, quantity):
        """
         returns quantity of books from warehouse
        """
        if self.has_more_books is not False and quantity < 64:
            return quantity
        else:
            raise OutOfBooksException

    @abstractmethod
    def __str__(self):
        """
        string represantion of my class
        """
        return f"Title: {self.title}"
    
    @abstractmethod
    def get_pages_count(self):
        """
        returns pages count
        """
        pass
    