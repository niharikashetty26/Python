class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            print(f"{self.name} borrowed {book}")
        else:
            print(f"Sorry, {book} is not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            print(f"{self.name} returned {book}")
        else:
            print(f"{self.name} does not have {book}")

    def __str__(self):
        return self.name

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Added {book} to the library")

    def register_member(self, name):
        member = Member(name)
        self.members.append(member)
        print(f"Registered {member} as a library member")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        if member and book:
            member.borrow_book(book)
        else:
            print(f"Either the book or the member does not exist in the library")

    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        book = self.find_book(book_title)
        if member and book:
            member.return_book(book)
        else:
            print(f"Either the book or the member does not exist in the library")


library = Library()
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("1984", "George Orwell")

library.register_member("Niharika")
library.register_member("Anushka")

library.borrow_book("Niharika", "1984")
library.borrow_book("Anushka", "The Great Gatsby")
library.return_book("Niharika", "1984")
library.return_book("Anushka", "The Great Gatsby")
