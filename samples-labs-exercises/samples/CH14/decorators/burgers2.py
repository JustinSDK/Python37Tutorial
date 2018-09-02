from typing import Callable

PriceFunc = Callable[..., float]

def sidedish1(meal: PriceFunc) -> PriceFunc:
    return lambda: meal() + 30

def sidedish2(meal: PriceFunc) -> PriceFunc:
    return lambda: meal() + 40

@sidedish1
@sidedish2
def friedchicken():
    return 49.0

print(friedchicken())   # 顯示119.0