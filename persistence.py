import json
from datetime import datetime

from library import Library
from books import PhysicalBook
from users import Student, Teacher

class Persistence:
    def __init__(self, file="library.json") -> None:
        self.file = file

    def save_data(self, library):
        data = {
            "name": library.name,
            "users": [user.__dict__ for user in library.users],
            "books": [book.__dict__ for book in library.books],
            "save_date": datetime.now().isoformat()
        }

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_data(self):
        with open(self.file, "r", encoding="utf-8") as f:
            data = json.load(f)

        library = Library(data["name"])
        for data_book in data["books"]:
            book = PhysicalBook(
                data_book["title"],
                data_book["autor"],
                data_book["isbn"],
                data_book["available"],
            )
            library.books.append(book)

        for user_data in data["users"]:
            if 'degree' in user_data:
                user = Student(
                    user_data["name"],
                    user_data["cedula"],
                    user_data["degree"]
                )
            else:
                user = Teacher(
                    user_data["name"],
                    user_data["cedula"]
                )
            library.users.append(user)

        return library

