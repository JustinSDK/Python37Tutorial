from typing import Type
from functools import wraps

def sidedish1(cls: Type) -> Type:
    wrapped_content = cls.content
    wrapped_price = cls.price

    @wraps(wrapped_content)
    def content(self):
        return wrapped_content(self) + " | 可樂 | 薯條"

    @wraps(wrapped_price)
    def price(self):
        return wrapped_price(self) + 30.0

    cls.content = content
    cls.price = price

    return cls

@sidedish1
class FriedChicken:
    def content(self):
        return "不黑心炸雞"

    def price(self):
        return 49.0

friedchicken = FriedChicken()
print(friedchicken.content())   # 不黑心炸雞 | 可樂 | 薯條
print(friedchicken.price())        # 79.0