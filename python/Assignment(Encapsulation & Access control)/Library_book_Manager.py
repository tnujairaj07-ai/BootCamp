class Book:
    def __init__(self, isbn, title, author, copies):
        self.__isbn = isbn
        self._title = title
        self._author = author
        self.__copies = copies

    @property
    def isbn(self):
        return self.__isbn

    @property
    def available(self):
        return self.__copies

    def checkout(self, n):
        if n <= 0:
            raise ValueError("Invalid number of books")

        if n > self.__copies:
            raise ValueError("Not enough copies available")

        self.__copies -= n

    def return_book(self, n):
        if n <= 0:
            raise ValueError("Invalid number of books")

        self.__copies += n


# Testing
b1 = Book("12345", "Python Basics", "Rahul", 5)

print("Available Copies:", b1.available)

b1.checkout(2)
print("After Checkout:", b1.available)

b1.return_book(1)
print("After Return:", b1.available)

print("ISBN:", b1.isbn)