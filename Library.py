from book import Book, Ebook
from heap_sort import heap_sort

class Library:
    lib_name = "School Library"

    def __init__(self):
        self.__book_list = []

    def add_book(self, book):
        self.__book_list.append(book)
        print("Book added successfully: " + book.get_info())

    def check_all_books(self):
        if not self.__book_list:
            print("No books in the library!")
        else:
            print("=====All Books in Library=====")
            for b in self.__book_list:
                print(b.get_info() + ", Type: " + b.show_type())

    @classmethod
    def change_name(cls, new_name):
        cls.lib_name = new_name
        print("Library name changed to: " + cls.lib_name)

    @staticmethod
    def check_bookid(book_id):
        if str(book_id).isdigit():
            return True, "ID format correct"
        else:
            return False, "ID must be a number!"

    def sort_books_by_stock(self):
        if not self.__book_list:
            print("No books to sort!")
            return
        self.__book_list = heap_sort(self.__book_list, key=lambda book: book.get_stock())
        print("=====Books Sorted by Stock (Ascending)=====")
        for b in self.__book_list:
            print(b.get_info() + ", Type: " + b.show_type())