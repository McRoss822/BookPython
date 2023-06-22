"""
module
"""
from src.models.book import Book


class InteractiveBook(Book):
    """
    interactive class inherits from Book class
    """
    shops = {"PlayMarket", "Torrent-Igruha"}
    BYTES_PER_PAGE = 16

    # pylint:disable=too-many-arguments
    def __init__(self, title, publisher, year, genre, count_in_warehouse, file_size, format):
        super().__init__(title, publisher, year, genre, count_in_warehouse)
        self.file_size = file_size
        self.format = format
    
    def __str__(self):
        """
        returns string representation
        """
        return f"{self.title} (Interactive)"
    
    def get_pages_count(self):
        """
        returns pages count
        """
        return self.file_size / self.BYTES_PER_PAGE
    