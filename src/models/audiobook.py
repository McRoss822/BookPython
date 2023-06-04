"""
audio module
"""

from models.book import Book


class AudioBook(Book):
    """
    audiobook class inherits from Book class
    """
    BYTES_PER_MINUTE = 16
    shops = {"AppStore", "Spotify"}

    # pylint:disable=too-many-arguments
    def __init__(self, title, publisher, year, genre, count_in_warehouse, file_size):
        super().__init__(title, publisher, year, genre, count_in_warehouse)
        self.file_size = file_size

    def __str__(self):
        """
        returns string representation
        """
        return f" {self.title} (Audio)"

    def get_pages_count(self):
        """
        returns pages count
        """
        return self.file_size / self.BYTES_PER_MINUTE
