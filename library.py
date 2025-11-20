from exceptions import UserNotFoundError, BookNotAvailableError

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def books_available(self):
        return [
            book for book in self.books if book.available
        ]

    def search_user(self, cedula):
        for user in self.users:
            if user.cedula == cedula:
                return user
        raise UserNotFoundError(f"El usuario con la cédula {cedula} no se encuentra registrado")
    
    def search_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                return book
        raise BookNotAvailableError(f"El libro con el titulo: {title} no se encuentra disponible o no esta registrado")
    
    @staticmethod
    def validate_isbn(isbn):
        return len(isbn) >= 10
