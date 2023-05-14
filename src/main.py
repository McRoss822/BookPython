class Book:
    __instance = None

    def __init__(self, title, publisher, year, genre, count_in_warehouse ):
            self.__title = title
            self.__publisher = publisher
            self.__year = year
            self.__genre = genre
            self.__count_in_warehouse = count_in_warehouse 
        

   # def get_instance(self):
   #     return Book().__instance

    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        self.__title = title
    
    @property
    def publisher(self):
        return self.__publisher
    
    @publisher.setter
    def publisher(self, publisher):
        self.__publisher = publisher

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, year):
        self.__year = year
    
    @property
    def genre(self):
        return self.__genre
    
    @genre.setter
    def genre(self, genre):
        self.__genre = genre
    
    @property
    def count_in_warehouse(self):
        return self.__count_in_warehouse
    
    @count_in_warehouse.setter
    def count(self, count_in_warehouse):
        self.__count_in_warehouse = count_in_warehouse

    def has_more_books(self):
        if self is not None:
            return True, self.count_in_warehouse
        else:
            return False    

    def get_book(self, quantity):
        if self.has_more_books != False and quantity < self.count_in_warehouse:
            self.count = self.count - quantity
            return  quantity   
    
    def __str__(self):
        return f"Title: {self.title}, Count:{self.__count_in_warehouse}"
    
def main():
    
    book1 = Book("RRR", "BBB", 1987, "fantastic", 12),
  #  book2 = Book(),
    #book3 = Book().get_instance()

    list_of_books = [
        book1,
     #   book2,
     #   book3
    ] 
    for book in list_of_books:
        print(book)

if __name__ == "__main__":
    main()
