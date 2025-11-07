from typing import Protocol
from main import Libro

class RequestProtocol(Protocol):
    def request_book(self, book: str) -> str:
        """Method that any applicant must implement"""
        ... 

class User:
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


student = Student('Luis', '12345678', 'Ingeniería')
student2 = Student('José', '11223344', 'Medicina')
teacher = Teacher('Felipe', '87654321')

libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", "9781644734728", True)

usuarios: list[RequestProtocol] = [student, student2, teacher, libro]

for usuario in usuarios:
    print(usuario.request_book('Cien Años de Soledad'))