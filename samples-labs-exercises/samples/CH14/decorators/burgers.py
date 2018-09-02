from typing import Callable

PriceFunc = Callable[..., float]

def sidedish1(meal: PriceFunc) -> PriceFunc:
    return lambda: meal() + 30

@sidedish1
def friedchicken():
    return 49.0

print(friedchicken())    #  顯示 79.0