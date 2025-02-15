class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

class Book(LibraryItem):
    def __init__(self, title, author, isbn):
        super().__init__(title, author)
        self.isbn = isbn

    def get_isbn(self):
        return self.isbn

book_1 = Book("Naruto", "Masashi Kishimoto", "3454") 
print(book_1.get_title())           # Output: Naruto
print(book_1.get_author())          # Output: Masashi Kishimoto
print(book_1.get_isbn())            # Output: 3454

print("--------------------")       # Output: --------------------

book_2 = Book("One Piece", "Eiichiro Oda", "3425234")       
print(book_2.get_title())           # Output: One Piece
print(book_2.get_author())          # Output: Eiichiro Oda
print(book_2.get_isbn())            # Output: 3425234