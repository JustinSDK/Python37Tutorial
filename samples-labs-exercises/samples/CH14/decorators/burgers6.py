from typing import Callable
from functools import wraps

PriceFunc = Callable[..., float]

class Sidedish1:
    def __init__(self, func: PriceFunc) -> None:
        self.func = func

    def __call__(self):
        return self.func() + 30

def sidedish1(meal: PriceFunc) -> PriceFunc:
    sidedish1 = Sidedish1(meal)

    @wraps(meal)
    def wrapper():
        return sidedish1()

    return wrapper

@sidedish1
def friedchicken():
    return 49.0

print(friedchicken())    #   79.0