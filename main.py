from exceptions import UserNotFoundError, BookNotAvailableError
from persistence import Persistence

persistencia = Persistence()
biblioteca = persistencia.load_data()

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

persistencia.save_data(biblioteca)