from typing import Protocol

class LibroProtocol(Protocol):

    def lend_book(self) -> str: ...

    def return_book(self) -> str: ...
        
    def calculate_duration(self) -> str: ...

class Libro: 
    def __init__(self, title, autor, isbn, available, __lended_count=0):
        self.title = title
        self.autor = autor
        self.isbn = isbn
        self.available = available
        self.__lended_count = 0

    def __str__(self):
        return f"Título: {self.title}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {self.available}, Popular: {self.is_popular()}"

    def is_popular(self):
        if self.__lended_count >= 5:
            return f"El libro es popular."
        else:
            return f"El libro no es popular."

    def get_lended_count(self):
        return self.__lended_count

    def set_lended_count(self, value):
        self.__lended_count = value

class PhysicalBook(Libro):
    def lend_book(self):
        return "7 días"

class DigitalBook(Libro):
    def lend_book(self):
        return "14 días"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def books_available(self):
        return [
            book.title for book in self.books if book.available
        ]

mi_libro = PhysicalBook(
    "El Principito", 
    "Antoine de Saint-Exupéry", 
    "9781644734728", 
    True
)

mi_libro_no_disponible = PhysicalBook(
    "Cien Años de Soledad",
    "Gabriel García Márquez",
    "9781644734728",
    False,
)

otro_libro = PhysicalBook(
    "Don Quijote de la Mancha",
    "Miguel de Cervantes",
    "9781644734728",
    True,
)

biblioteca = Library("Platzi Biblioteca")
biblioteca.books = [
    mi_libro, 
    mi_libro_no_disponible, 
    otro_libro
]

print(biblioteca.books_available())

""" libros = [
    Libro("100 Años de Soledad", "Gabriel García Márquez", "9781644734728", True),
    Libro("El Principito", "Antoine de Saint-Exupéry", "9781644734728", True),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "9781644734728", True),
]

libros[0].set_lended_count(10)

print(libros[0].lend_book())
print(libros[0].return_book())
print(libros[0].lend_book())
print(libros[0].return_book())
print(libros[0].lend_book())
print(libros[0].return_book())
print(libros[0].lend_book())
print(libros[0].return_book())
print(libros[0].lend_book())
print(libros[0].return_book())

print(libros[0].get_lended_count())

for libro in libros:
    print(libro) """