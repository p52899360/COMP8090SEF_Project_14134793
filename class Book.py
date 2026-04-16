class Book:
    def __init__(self, book_id, title, author, stock=0):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__stock = stock

    def get_info(self):
        return f"ID {self.__book_id}: {self.__title}, Author {self.__author}, Stock {self.__stock}"

    def get_stock(self):
        return self.__stock

    def get_title(self):
        return self.__title

    def get_book_id(self):
        return self.__book_id

    def add_stock(self, num):
        if num > 0:
            self.__stock += num
            print(f"Stock added {num}, current stock: {self.__stock}")
        else:
            print("Add number must be greater than 0!")

    def show_type(self):
        return "Normal Paper Book"


class Ebook(Book):
    def __init__(self, book_id, title, author, fmt="PDF", stock=0):
        super().__init__(book_id, title, author, stock)
        self.__fmt = fmt

    def show_type(self):
        return f"E-book, Format {self.__fmt}"

    def get_fmt(self):
        return self.__fmt