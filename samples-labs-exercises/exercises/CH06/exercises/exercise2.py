from functools import total_ordering

@total_ordering
class Rational:
    def __init__(self, numer: int, denom: int) -> None:
        self.numer = numer
        self.denom = denom

    def __add__(self, that):
        return Rational(
            self.numer * that.denom + that.numer * self.denom,
            self.denom * that.denom
        )

    def __sub__(self, that):
        return Rational(
            self.numer * that.denom - that.numer * self.denom,
            self.denom * that.denom
        )

    def __mul__(self, that):
        return Rational(
            self.numer * that.numer,
            self.denom * that.denom
        )

    def __truediv__(self, that):
        return Rational(
            self.numer * that.denom,
            self.denom * that.denom
        )

    def __str__(self):
        return f'{self.numer}/{self.denom}'

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def __can_eq__(other):
        return hasattr(other, 'numer') and hasattr(other, 'denom')

    def __eq__(self, other):
        return __class__.__can_eq__(other) and (self.numer * other.denom == self.denom * other.numer)

    def __gt__(self, other):
        return __class__.__can_eq__(other) and (self.numer / self.denom) > (other.numer / other.denom)

    def __ge__(self, other):
        return __class__.__can_eq__(other) and (self.numer / self.denom) >= (other.numer / other.denom)

r1 = Rational(1, 2)
r2 = Rational(2, 4)

print(r1 == r2)
print(r1 > r2)
print(r1 <= r2)
