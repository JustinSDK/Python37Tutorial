from typing import Callable
from functools import wraps

PriceFunc = Callable[..., float]

def sidedish1(meal: PriceFunc) -> PriceFunc:
    @wraps(meal)
    def wrapper():
        return meal() + 30
    return wrapper

@sidedish1
def friedchicken():
    return 49.0

#  顯示 79.0
print(friedchicken())

#  顯示 <function friedchicken at 0x00EB4BB8>
print(friedchicken)