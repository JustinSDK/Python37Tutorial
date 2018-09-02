import sys
from contextlib import contextmanager
from typing import Type, Iterator

@contextmanager
def suppress(ex_type: Type[BaseException]) -> Iterator[None]:
    try:
        yield
    except ex_type:
        pass

with suppress(FileNotFoundError):
    for line in open(sys.argv[1]):
        print(line, end='')
