from typing import Protocol
from exceptions import InvalidTittleError
from abc import ABC, abstractmethod

class RequestProtocol(Protocol):
    def request_book(self, book: str) -> str:
        """Method that any applicant must implement"""
        ... 

class UserBase(ABC):
    @abstractmethod
    def request_book(self):
        pass

    # Los abstracmethods garantizan que funcione un metodo dentro de una clase
    @abstractmethod
    def return_book(self):
        pass

class User(UserBase):
    def __init__(self, name, cedula):
        self.name = name
        self.cedula = cedula
        self.borrowed_books = []

    def request_book(self, book):
        return f"Solicitud del libro '{book}' realizada."

class Student(User):
    def __init__(self, name, cedula, degree):
        super().__init__(name, cedula)
        self.degree = degree
        self.books_limit = 3

    def request_book(self, book):
        if not book:
            raise InvalidTittleError(f"El libro con el titulo {book} no es válido")

        if len(self.borrowed_books) < self.books_limit:
            self.borrowed_books.append(book)
            return f"Estudiante {self.name} ha solicitado el libro '{book}'."
        else:
            return f"Estudiante {self.name} ha alcanzado el límite de libros prestados. Libros prestados: {len(self.borrowed_books)}."

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return f"Estudiante {self.name} ha devuelto el libro '{book}'."
        else:
            return f"El libro '{book}' no está en la lista de libros prestados de {self.name}."

class Teacher(User):
    def __init__(self, name, cedula):
        super().__init__(name, cedula)
        self.books_limit = None
    
    def request_book(self, book):
        self.borrowed_books.append(book)
        return f"Profesor {self.name} ha solicitado el libro '{book}'."

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return f"Profesor {self.name} ha devuelto el libro '{book}'."
        else:
            return f"El libro '{book}' no está en la lista de libros prestados de {self.name}."
