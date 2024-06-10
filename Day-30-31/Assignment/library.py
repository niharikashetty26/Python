class BookNotAvailableError(Exception):
    pass


class BookNotBorrowedError(Exception):
    pass


class Library:
    def __init__(self):
        self.books = {
            "1984": 3,
            "To Kill a Mockingbird": 2,
            "The Great Gatsby": 4
        }
        self.borrowed_books = {}

    def borrow_book(self, book, user):
        if book not in self.books or self.books[book] == 0:
            raise BookNotAvailableError(f"The book '{book}' is not available.")
        if user not in self.borrowed_books:
            self.borrowed_books[user] = []
        self.books[book] -= 1
        self.borrowed_books[user].append(book)
        print(f"{user} borrowed '{book}'. Available copies: {self.books[book]}")

    def return_book(self, book, user):
        if user not in self.borrowed_books or book not in self.borrowed_books[user]:
            raise BookNotBorrowedError(f"{user} did not borrow the book '{book}'.")
        self.books[book] += 1
        self.borrowed_books[user].remove(book)
        print(f"{user} returned '{book}'. Available copies: {self.books[book]}")

    def get_available_books(self):
        return self.books


def main():
    library = Library()

    try:
        library.borrow_book("1984", "Alice")
        library.borrow_book("To Kill a Mockingbird", "Bob")
        library.borrow_book("The Great Gatsby", "Alice")
        library.borrow_book("1984", "Alice")
        library.return_book("1984", "Alice")
        library.borrow_book("1984", "Charlie")
        library.return_book("1984", "Bob")

    except BookNotAvailableError as e:
        print(f"Error: {e}")

    except BookNotBorrowedError as e:
        print(f"Error: {e}")

    finally:
        print("Final available books:")
        print(library.get_available_books())


if __name__ == "__main__":
    main()
