import pickle

class DVD:
    def __init__(self, title: str, year: int, duration: int, director: str) -> None:
        self.title = title
        self.year = year
        self.duration = duration
        self.director = director
        self.filename = self.title.replace(' ', '_') + '.pickle'

    def save(self):
        with open(self.filename, 'wb') as fh:
            pickle.dump(self, fh)

    @staticmethod
    def load(filename: str) -> 'DVD':
        with open(filename, 'rb') as fh:
            return pickle.load(fh)

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return "DVD('{0}', {1}, {2}, '{3}')".format(
            self.title, self.year, self.duration, self.director)

dvd1 = DVD('Birds', 2018, 8, 'Justin Lin')
dvd1.save()
dvd2 = DVD.load('Birds.pickle')
print(dvd2)
