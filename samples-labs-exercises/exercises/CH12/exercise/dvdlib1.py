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


class Customer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rentals: List[Rental] = []

    def add_rental(self, rental: Rental):
        self.rentals.append(rental)

    def statement(self) -> str:
        total_amount = 0
        freq_renter_points = 0
        result = f'Rental Record for {self.name}\n'
        for rental in self.rentals:
            this_amount = 0
            # determine amounts for each line
            content_rating = rental.movie.content_rating
            if content_rating == ContentRating.regular:
                this_amount += 2
                if rental.days_rented > 2:
                    this_amount += (rental.days_rented - 2) * 1.5
            elif content_rating == ContentRating.new_release:
                this_amount += (rental.days_rented * 3)
            elif content_rating == ContentRating.children:
                this_amount += 1.5
                if rental.days_rented > 3:
                    this_amount += (rental.days_rented - 3) * 1.5

            # add frequent renter points
            freq_renter_points += 1

            # add bonus for a two day new release rental
            if content_rating == ContentRating.new_release and rental.days_rented > 1:
                freq_renter_points += 1

            # show figures for this rental
            result += f'\t{rental.movie.title}\t{this_amount}\n'
            total_amount += this_amount

        # add footer lines
        result += f'Amount owed is {total_amount}\n'
        result += f'You earned {freq_renter_points} frequent renter points'
        return result

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