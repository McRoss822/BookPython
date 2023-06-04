"""
set manager class
"""

from src.managers.book_manager import BookManager
from src.models import book
from src.models.book import Book
import datetime


class SetManager:
    """
    class for managing object sets
    """
    def __init__(self, manager):
        self.manager = manager
        self.index = 0
        self.sets_list = []
        for b in self.manager.list_of_books:
            for b1 in b.shops:
                self.sets_list.append(b1)

    def __iter__(self):
        """
        turns into iter
        """
        return iter(self.sets_list)

    def __next__(self):
        """
        returns next from iter
        """
        counter = 0
        result = None
        for b in self.sets_list:
            result = self.sets_list[counter]
            counter += 1
        return result

    def __len__(self):
        """
        returns lengths of shops together
        """
        length = 0
        for b in self.manager.list_of_books:
            length += len(b.shops)
        return length

    def __getitem__(self, index):
        """
        returns given item"""
        for b in self.manager.list_of_books:
            counter = 0
            for b1 in b.shops:
                if counter == index:
                    return b1
                counter += 1
