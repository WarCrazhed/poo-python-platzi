import json
from datetime import datetime

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
        print(f"datos {data}")