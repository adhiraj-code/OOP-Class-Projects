class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        
    def borrow(self, is_borrow = True):
        print("Book is Borrowed") 

    def return_book(self, is_borrow = False):
        print("Book is returned")

    book1 = Book("Story","Author")
    book2 = Book("Story","Author")    