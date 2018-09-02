from typing import List, Optional
import shelve

class DVD:
    def __init__(self, title: str, year: int, duration: int, director: str) -> None:
        self.title = title
        self.year = year
        self.duration = duration
        self.director = director

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return ("DVD('{title}', {year}, {duration}, '{director}')"
                    .format(**vars(self)))

class DvdDao:
    def __init__(self, dbname: str) -> None:
        self.dbname = dbname

    def save(self, dvd: DVD):
        with shelve.open(self.dbname) as shelve_db:
            shelve_db[dvd.title] = dvd

    def all(self) -> List[DVD]:
        with shelve.open(self.dbname) as shelve_db:
            return [shelve_db[title]
                        for title in sorted(shelve_db, key = str.lower)]

    def load(self, title: str) -> Optional[DVD]:
        with shelve.open(self.dbname) as shelve_db:
            if title in shelve_db:
                return shelve_db[title]
        return None

    def remove(self, title: str):
        with shelve.open(self.dbname) as shelve_db:
            del shelve_db[title]


dao = DvdDao('dvdlib.shelve')
dvd1 = DVD('Birds', 2018, 1, 'Justin Lin')
dvd2 = DVD('Dogs', 2018, 7, 'Monica Huang')

dao.save(dvd1)
dao.save(dvd2)
print(dao.all())
print(dao.load('Birds'))
dao.remove('Birds')
print(dao.all())
