from exceptions import UserNotFoundError

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def books_available(self):
        return [
            book.title for book in self.books if book.available
        ]

    def search_user(self, cedula):
        for user in self.users:
            if user.cedula == cedula:
                return user
        raise UserNotFoundError(f"El usuario con la cédula {cedula} no se encuentra registrado")