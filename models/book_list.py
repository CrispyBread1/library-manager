from models.Book import *



book1 = Book("Norwegan Wood", "Murakami", "Drama")
book2 = Book("Foundation", "Isaac Asimov", "Sci-Fi")
book3 = Book("The Secret History", "Donna Tart", "Drama")
book_list=[book1, book2, book3]

def delete_book_at_index(index):
    book_list.pop(index)