"""
Main module
"""
from models.audiobook import AudioBook
from models.electronic_book import ElectronicBook
from models.interactive_book import InteractiveBook
from managers.book_manager import BookManager
from models.paper_book import PaperBook


def main():

    """
    main function for creating list of objects and testing their workability
    """

    catcher = ElectronicBook("Catcher in the Rye", "Me", 1235, "action", 1999, 64, "PDF")
    treasure = AudioBook("Treasure Hunt", "EEE", 1234, "fantastic", 123, 64  )
    my_sweet_home = InteractiveBook("My sweet Home", "TTT", 1987, "family", 67, 674, "Game")
    calculus = PaperBook("Calculus 1-st part", "ff", 1876, "action", 142, 325)
    manager = BookManager()
    manager.add_books(catcher)
    manager.add_books(treasure)
    manager.add_books(my_sweet_home)
    manager.add_books(calculus)
    print(manager.find_book_by_title("Catcher in the Rye"))
    print(manager.find_book_by_genre("action"))

if __name__ == "__main__":
    main()
