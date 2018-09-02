from typing import Any, Iterable, Callable

Consume = Callable[[Any], None]

def for_in(iterable: Iterable[Any], consume: Consume):
    iterator = iter(iterable)
    try:
        while True:
            consume(next(iterator))
    except StopIteration:
        pass

for_in([10, 20, 30], print)

