import os.path
import sqlite3

db_name = 'dvd_lib.sqlite3'

def connect(name: str) -> sqlite3.Connection:
    create = not os.path.exists(name)
    conn = sqlite3.connect(name)
    if create:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE dvds ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
            "title TEXT NOT NULL, "
            "year INTEGER NOT NULL, "
            "duration INTEGER NOT NULL, "
            "director_id TEXT NOT NULL)")
        conn.commit()

    return conn

class DVD:
    def __init__(self, title: str, year: int, duration: int, director: str) -> None:
        self.title = title
        self.year = year
        self.duration = duration
        self.director = director

    def save(self):
        with connect(db_name) as conn:
            conn.cursor().execute("INSERT INTO dvds (title, year, duration, director_id) VALUES (?, ?, ?, ?)",
                                  (self.title, self.year, self.duration, self.director))

    @staticmethod
    def load(title: str) -> 'DVD':
        with connect(db_name) as conn:
            c = conn.cursor()
            fields = c.execute('SELECT title, year, duration, director_id FROM dvds WHERE title =?', (title,)).fetchone()
            return DVD(*fields)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "DVD('{0}', {1}, {2}, '{3}')".format(
            self.title, self.year, self.duration, self.director)

dvd1 = DVD('Birds', 2018, 8, 'Justin Lin')
dvd1.save()
dvd2 = DVD.load('Birds')
print(dvd2) # 顯示DVD('Birds', 2018, 8, 'Justin Lin')

