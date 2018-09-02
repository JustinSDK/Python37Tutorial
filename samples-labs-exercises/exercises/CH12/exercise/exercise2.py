import unittest
from dvdlib2 import ContentRating, Customer, Movie, Rental

class CustomerTestCase(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('test')
        movies = [
            Movie('ABC', ContentRating.new_release),
            Movie('XYZ', ContentRating.regular),
            Movie('123', ContentRating.children)
        ]
        for movie in movies:
            self.customer.add_rental(Rental(movie, 7))

    def test_statement(self):
        statement = self.customer.statement()
        self.assertTrue(
            'ABC	21' in statement and
            'XYZ	9.5' in statement and
            '123	7.5' in statement and
            'Amount owed is 38.0' in statement and
            'You earned 4 frequent renter points' in statement
        )

    def test_get_total_charge(self):
        total = self.customer.get_total_charge()
        self.assertEqual(38.0, total)

    def test_get_total_freq_renter_points(self):
        total_freq_renter_points = self.customer.get_total_freq_renter_points()
        self.assertEqual(4, total_freq_renter_points)