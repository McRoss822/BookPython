"""
Book class module
"""

from abc import ABC, abstractclassmethod


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
        '''
        returns instance
        '''
        if Book.__instance is None:
            Book.__instance = Book()
        else:
            Book.__instance = None
        return Book.__instance

    def has_more_books(self):
        '''
        returns true if books are in warehouse
        '''
        if self is not None:
            return True, self.count_in_warehouse

    def get_book(self, quantity):
        '''
        returns quantity of books in warehouse
        '''
        if self.has_more_books is not False and quantity < self.count_in_warehouse:
            self.count_in_warehouse = self.count_in_warehouse - quantity
            return quantity

    @abstractclassmethod
    def __str__(self):
        '''
        string represantion of my class
        '''
        return f"Title: {self.title}"
    
    @abstractclassmethod
    def get_pages_count(self):
        """
        returns pages count
        """
        pass
    