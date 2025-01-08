class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_book_info(self):
       
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")

    def update_author(self, new_author):
        
        self.author = new_author
        print(f"Author name updated to: {self.author}")

class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self, book):
        
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def lend_book(self, title):
       
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{book.title}' has been lent out.")
                return
        print(f"Sorry, the book '{title}' is not available.")

    def display_available_books(self):
        
        if not self.books:
            print("No books available in the library.")
        else:
            print("Available books in the library:")
            for book in self.books:
                book.display_book_info()
                print("-" * 30)




book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("1984", "George Orwell", "9780451524935")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")


library = Library()


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)


library.display_available_books()


book1.update_author("F. S. Fitzgerald")


library.lend_book("1984")


library.display_available_books()
