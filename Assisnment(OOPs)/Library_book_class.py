class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # default value

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Borrowed: {self.is_borrowed}")

book1 = Book("The Alchemist", "Paulo Coelho")
book2 = Book("Harry Potter", "J.K. Rowling")
book3 = Book("Python Programming", "John Zelle")

book2.is_borrowed = True
book1.is_borrowed = True

book1.display_info()
book2.display_info()
book3.display_info()