class Libro: 
    def __init__(self, title, autor, isbn, available, lended_count=0):
        self.title = title
        self.autor = autor
        self.isbn = isbn
        self.available = available
        self.lended_count = 0

    def __str__(self):
        return f"Título: {self.title}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {self.available}, Popular: {self.is_popular()}"

    def lend_book(self):
        if self.available:
            self.lended_count += 1
            self.available = False
        return f"El libro '{self.title}' ha sido prestado."

    def return_book(self):
        if not self.available:
            self.available = True
        return f"El libro '{self.title}' ha sido devuelto."

    def is_popular(self):
        if self.lended_count >= 5:
            return f"El libro es popular."
        else:
            return f"El libro no es popular."

libros = [
    Libro("100 Años de Soledad", "Gabriel García Márquez", "9781644734728", True),
    Libro("El Principito", "Antoine de Saint-Exupéry", "9781644734728", True),
    Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "9781644734728", True),
]

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

for libro in libros:
    print(libro)