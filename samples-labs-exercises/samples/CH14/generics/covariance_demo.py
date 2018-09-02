from typing import TypeVar, Generic, Optional

T = TypeVar('T', covariant=True)

class Node(Generic[T]):
    def __init__(self, value: T, next: Optional['Node[T]']) -> None:
        self.value = value
        self.next = next

class Fruit:
    pass

class Apple(Fruit):
    def __str__(self):
        return 'Apple'

class Banana(Fruit):
    def __str__(self):
        return 'Banana'

def show(node: Node[Fruit]):
    n: Optional[Node[Fruit]] = node
    while n:
        print(n.value)
        n = n.next

apple1 = Node(Apple(), None)
apple2 = Node(Apple(), apple1)
apple3 = Node(Apple(), apple2)

banana1 = Node(Banana(), None)
banana2 = Node(Banana(), banana1)
banana3 = Node(Banana(), banana2)

show(apple3)
show(banana3)