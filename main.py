from users import Student, Teacher
from books import PhysicalBook
from library import Library
from exceptions import UserNotFoundError

biblioteca = Library("Platzi Biblioteca")
student = Student('Luis', '12345678', 'Ingeniería')
student2 = Student('José', '11223344', 'Medicina')
teacher = Teacher('Felipe', '87654321')
mi_libro = PhysicalBook("El Principito", "Antoine de Saint-Exupéry", "9781644734728", )
otro_libro = PhysicalBook("Don Quijote de la Mancha","Miguel de Cervantes","9781644734728",)

biblioteca.users = [student, student2, teacher]
biblioteca.books = [mi_libro, otro_libro]

print("Bienvenido a Platzi Biblioteca")

print("Libros disponibles:")
for book in biblioteca.books_available():
    print(f"  - {book}") 
print()

cedula = input("Ingrese su cédula: ")
try:
    user = biblioteca.search_user(cedula)
    print(f"Bienvenido {user.name}")
except UserNotFoundError as e:
    print(e)
