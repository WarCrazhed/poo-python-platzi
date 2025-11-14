from typing import Protocol

class LibroProtocol(Protocol):

    def lend_book(self) -> str: ...

    def return_book(self) -> str: ...
        
    def calculate_duration(self) -> str: ...

class Libro: 
    def __init__(self, title, autor, isbn, available=True, __lended_count=0):
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