
"""
docstring
"""

from book import Book

def main():
    '''
    main
    '''
    book1 = Book("BBB", "VVVV", 1235, "ffff", 123),
    book2 = Book("FFF", "EEE", 1234, "333", None ),
    book3 = Book.get_instance()
    book4 = Book.get_instance()

    list_of_books = [
        book1,
        book2,
        book3,
        book4
    ]

    for book in list_of_books:
        print(book)

list_of_integers = [1, 2, 4, 6, 5, 8]

def thing(your_list):
    """
    docstring
    """
    counter = 0
    for i in your_list:
        if (counter + 1) % 2 == 0:
            print(i**2)
        elif (counter + 1) % 3 == 0:
            print(i / 3)
        counter += 1

thing(list_of_integers)

if __name__ == "__main__":
    main()
