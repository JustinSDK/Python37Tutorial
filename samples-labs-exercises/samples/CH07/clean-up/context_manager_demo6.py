from contextlib import contextmanager
from typing import Any, Iterator

@contextmanager
def closing(thing: Any) -> Iterator[Any]:
    try:
        yield thing
    finally:
        thing.close()

class Some:
    def __init__(self, name: str) -> None:
        self.name = name

    def close(self):
        print(self.name, 'is closed.')

with closing(Some('Resource')) as res:
    print(res.name)