from users import Teacher
from library import Library
from exceptions import UserNotFoundError, BookNotAvailableError
from data import data_libros, data_estudiantes

biblioteca = Library("Platzi Biblioteca")
teacher = Teacher('Felipe', '87654321')

biblioteca.users = [teacher] + data_estudiantes
biblioteca.books = data_libros

# Ejemplo de Libro setter
# libro_de_prueba = data_libros[0]
# libro_de_prueba.lended_count = -1

print("Bienvenido a Platzi Biblioteca")

print("Libros disponibles:")
for book in biblioteca.books_available():
    print(book.full_description) 
print()

cedula = input("Ingrese su cédula: ")
try:
    user = biblioteca.search_user(cedula)
    print(f"Bienvenido {user.name}")
except UserNotFoundError as e:
    print(e)

titulo = input("Digite el título del libro: ")
try:
    book = biblioteca.search_book(titulo)
    print(f"El libro que seleccionaste es: {book}")
except BookNotAvailableError as e:
    print(e)

resultado = user.request_book(book.title)
print(f"\n{resultado}")

try:
    resultado_prestar = book.lend_book()
    print(f"\n{resultado_prestar}")
except BookNotAvailableError as e:
    print(e)