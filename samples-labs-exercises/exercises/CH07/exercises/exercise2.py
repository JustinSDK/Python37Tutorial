import sys
from typing import Type, Optional
from types import TracebackType

class Suppress:
    def __init__(self, ex_type: Type[BaseException]) -> None:
        self.ex_type = ex_type

    def __enter__(self):
        return None

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_value: Optional[BaseException],
                 traceback: Optional[TracebackType]) -> Optional[bool]:
        return exc_type == self.ex_type

with Suppress(FileNotFoundError):
    for line in open(sys.argv[1]):
        print(line, end='')
