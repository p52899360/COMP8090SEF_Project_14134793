from book import Book, Ebook
from library import Library

if __name__ == "__main__":
    my_lib = Library()
    print("Initial library name: ", Library.lib_name)
    Library.change_name("HKMU Mini Library")
    print("Changed library name: ", Library.lib_name)
    print("-"*30)

    print(Library.check_bookid(1001))
    print(Library.check_bookid("book1002"))
    print("-"*30)

    b1 = Book(1001, "Data Structures", "Teacher Li", 3)
    b2 = Book(1003, "Algorithms", "Teacher Zhang", 7)
    e1 = Ebook(1002, "Python Beginner", "Teacher Wang", "EPUB", 5)

    my_lib.add_book(b1)
    my_lib.add_book(b2)
    my_lib.add_book(e1)
    print("-"*30)

    my_lib.check_all_books()
    print("-"*30)

    b1.add_stock(2)
    e1.add_stock(4)
    print("-"*30)

    my_lib.sort_books_by_stock()