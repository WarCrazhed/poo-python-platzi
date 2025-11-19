from typing import Protocol
from exceptions import BookNotAvailableError

class BookProtocol(Protocol):

    def lend_book(self) -> str: ...

    def return_book(self) -> str: ...
        
    def calculate_duration(self) -> str: ...

class Book: 
    def __init__(self, title, autor, isbn, available=True, __lended_count=0):
        self.title = title
        self.autor = autor
        self.isbn = isbn
        self.available = available
        self.__lended_count = 0

    def __str__(self):
        return f"Título: {self.title}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {self.available}, Popular: {self.is_popular()}"

    def lend_book(self):
        if not self.available:
            raise BookNotAvailableError(f"El libro '{self.title}' no está disponible.")

        if self.available:
            self.available = False
            self.__lended_count += 1
            return f"El libro '{self.title}' ha sido prestado. Total de prestamos: {self.__lended_count}."

    def return_book(self):
        if self.available:
            raise BookNotAvailableError(f"El libro '{self.title}' ya está disponible.")

        if not self.available:
            self.available = True
            self.__lended_count -= 1

    @property
    def is_popular(self):
        if self.__lended_count >= 5:
            return f"El libro es popular."
        else:
            return f"El libro no es popular."

    @property
    def lended_count(self):
        return self.__lended_count

    @lended_count.setter
    def lended_count(self, value):
        if value > 0:
            self.__lended_count = value
        raise ValueError("El valor de veces prestado debe ser mayor a 0.")

    @property
    def full_description(self):
        return f"Título: {self.title}\nAutor: {self.autor}\nISBN: {self.isbn}\n"

class PhysicalBook(Book):
    def calculate_duration(self):
        return "7 días"

class DigitalBook(Book):
    def calculate_duration(self):
        return "14 días"