"""
Main module
"""
from models.audiobook import AudioBook
from src.models.electronic_book import ElectronicBook
from src.models.interactive_book import InteractiveBook
from src.managers.book_manager import BookManager
from src.models.paper_book import PaperBook
from src.managers.set_manager import SetManager
from decorators import method_log


def main():

    """
    main function for creating list of objects and testing their workability
    """

    catcher = ElectronicBook("Catcher in the Rye", "Me", 1235, "action", 1999, 64, "PDF")
    treasure = AudioBook("Treasure Hunt", "EEE", 1234, "fantastic", 123, 64)
    my_sweet_home = InteractiveBook("My sweet Home", "TTT", 1987, "family", 67, 674, "Game")
    calculus = PaperBook("Calculus 1-st part", "ff", 1876, "action", 142, 325)
    manager = BookManager()
    manager.add_books(catcher)
    manager.add_books(treasure)
    manager.add_books(my_sweet_home)
    manager.add_books(calculus)

    print(manager.results())
    print(manager.result_list())
    print(manager.zipperKlipper())
    print(manager.__getitem__(2))
    sm = SetManager(manager)
    print(sm.__iter__())
    print(sm.__len__())


if __name__ == "__main__":
    main()
