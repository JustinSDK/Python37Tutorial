from enum import IntEnum
from typing import List

class ContentRating(IntEnum):
    regular = 0
    new_release = 1
    children = 2

class Movie:
    def __init__(self, title: str, content_rating: ContentRating) -> None:
        self.title = title
        self.content_rating = content_rating

class Rental:
    def __init__(self, movie: Movie, days_rented: int) -> None:
        self.movie = movie
        self.days_rented = days_rented

    def get_charge(self) -> float:
        this_amount = 0
        content_rating = self.movie.content_rating
        if content_rating == ContentRating.regular:
            this_amount += 2
            if self.days_rented > 2:
                this_amount += (self.days_rented - 2) * 1.5
        elif content_rating == ContentRating.new_release:
            this_amount += (self.days_rented * 3)
        elif content_rating == ContentRating.children:
            this_amount += 1.5
            if self.days_rented > 3:
                this_amount += (self.days_rented - 3) * 1.5
        return this_amount

    def get_freq_renter_points(self) -> int:
        return 2 if self.movie.content_rating == ContentRating.new_release and self.days_rented > 1 else 1


class Customer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rentals: List[Rental] = []

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)

    def statement(self) -> str:
        result = f'Rental Record for {self.name}\n'
        for rental in self.rentals:
            result += f'\t{rental.movie.title}\t{rental.get_charge()}\n'

        result += f'Amount owed is {self.get_total_charge()}\n'
        result += f'You earned {self.get_total_freq_renter_points()} frequent renter points'
        return result

    def get_total_charge(self) -> float:
        total_amount = 0
        for rental in self.rentals:
            total_amount += rental.get_charge()
        return total_amount

    def get_total_freq_renter_points(self) -> int:
        freq_renter_points = 0
        for rental in self.rentals:
            freq_renter_points += rental.get_freq_renter_points()
        return freq_renter_points


if __name__ == '__main__':
     customer = Customer('test')
     movies = [
         Movie('ABC', ContentRating.new_release),
         Movie('XYZ', ContentRating.regular),
         Movie('123', ContentRating.children)
     ]
     for movie in movies:
         customer.add_rental(Rental(movie, 7))
     print(customer.statement())
