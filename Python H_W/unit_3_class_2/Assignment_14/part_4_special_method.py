class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

book_1 = Book("Naruto", "Masashi Kishimoto")
print(book_1)         # Output: Naruto by Masashi Kishimoto
print(repr(book_1))   # Output: Book(title='Naruto', author='Masashi Kishimoto')

book_2 = Book("One Piece", "Eiichiro Oda")
print(book_2)         # Output: One Piece by Eiichiro Oda
print(repr(book_2))   # Output: Book(title='One Piece', author='Eiichiro Oda')
