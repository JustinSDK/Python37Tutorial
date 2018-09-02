from typing import TypeVar, Generic, List, Callable, Any

T = TypeVar('T', contravariant=True)

class Fruit:
    def __init__(self, weight: int, price: int) -> None:
        self.weight = weight
        self.price = price

    def __str__(self):
        return f'({self.weight}, {self.price})'

class Apple(Fruit):
    def __init__(self, weight: int, price: int) -> None:
        super().__init__(weight, price)

    def __str__(self):
        return 'Apple' + super().__str__()

class Banana(Fruit):
    def __init__(self, weight: int, price: int) -> None:
        super().__init__(weight, price)

    def __str__(self):
        return 'Banana' + super().__str__()

class Lt(Generic[T]):
    def __init__(self):
        self.lt = []

    def append(self, elem: T):
        self.lt.append(elem)

    def sort(self, key: Callable[[T], Any]):
        self.lt.sort(key=key)

    def foreach(self, consume: Callable[[T], None]):
        for elem in self.lt:
            consume(elem)


class Basket(Generic[T]):
    def __init__(self, things: List[T]) -> None:
        self.things = things

    def dropinto(self, lt: Lt[T]):
        while len(self.things):
            lt.append(self.things.pop())

apples = Basket([Apple(25, 150), Apple(20, 100)])
bananas = Basket([Banana(15, 250), Banana(30, 500)])

fruits = Lt[Fruit]()
apples.dropinto(fruits)
bananas.dropinto(fruits)

fruits.sort(key=lambda fruit: fruit.weight)
fruits.foreach(print)
