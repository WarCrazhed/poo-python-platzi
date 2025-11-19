from books import PhysicalBook
from users import Student

# Creación de 10 Libros Fisicos con diferentes títulos y autores

libro1 = PhysicalBook("El Principito", "Antoine de Saint-Exupéry", "9781644734728", )
libro2 = PhysicalBook("Don Quijote de la Mancha","Miguel de Cervantes","9781644734728",)
libro3 = PhysicalBook("Cien años de soledad","Gabriel García Márquez","9781644734728",)
libro4 = PhysicalBook("1984","George Orwell","9781644734728",)
libro5 = PhysicalBook("Orgullo y prejuicio","Jane Austen","9781644734728",)
libro6 = PhysicalBook("Harry Potter y la piedra filosofal","J.K. Rowling","9781644734728",)
libro7 = PhysicalBook("Matar a un ruiseñor","Harper Lee","9781644734728",)
libro8 = PhysicalBook("Los juegos del hambre","Suzanne Collins","9781644734728",)
libro9 = PhysicalBook("El señor de los anillos","J.R.R. Tolkien","9781644734728",)
libro10 = PhysicalBook("El alquimista","Paulo Coelho","9781644734728",)

# Creación de 10 Estudaintes con diferentes nombres, cedulas y carreras

estudiante1 = Student("Juan Pablo Ramos", "12345678", "Ingeniería")
estudiante2 = Student("María José Rodríguez", "87654321", "Medicina")
estudiante3 = Student("Pedro López", "11223344", "Derecho")
estudiante4 = Student("Ana García", "55667788", "Arquitectura")
estudiante5 = Student("Carlos Martínez", "99887766", "Diseño")
estudiante6 = Student("Laura Sánchez", "44556677", "Psicología")
estudiante7 = Student("Diego Ramírez", "22334455", "Biología")
estudiante8 = Student("Sofía Torres", "77889900", "Historia")
estudiante9 = Student('Luis Alberto Rojas', '12345678', 'Ingeniería')
estudiante10 = Student('José Armando Rodríguez', '11223344', 'Medicina')

data_libros = [
    libro1,
    libro2,
    libro3,
    libro4,
    libro5,
    libro6,
    libro7,
    libro8,
    libro9,
    libro10
]

data_estudiantes = [
    estudiante1,
    estudiante2,
    estudiante3,
    estudiante4,
    estudiante5,
    estudiante6,
    estudiante7,
    estudiante8,
    estudiante9,
    estudiante10
]