"""
paper book class module
"""
from src.models.book import Book


class PaperBook(Book):
    """
    paper book class inherits from Book class
    """
    shops = {"Library", "BookStore"}

    # pylint:disable=too-many-arguments
    def __init__(self, title, publisher, year, genre, count_in_warehouse, pages_count):
        super().__init__(title, publisher, year, genre, count_in_warehouse)
        self.pages_count = pages_count

    def __str__(self):
        """
        returns string representation
        """
        return f"{self.title} (Paper)"

    def get_pages_count(self):
        """
        returns pages count
        """
        return self.pages_count
    