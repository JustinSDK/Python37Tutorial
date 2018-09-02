from typing import Any

class Repeat:
    def __init__(self, elem: Any, n: int) -> None:
        self.elem = elem
        self.n = n

    def __iter__(self):
        elem = self.elem
        n = self.n

        class _Iter:
            def __init__(self):
                self.count = 0

            def __next__(self):
                if self.count < n:
                    self.count += 1
                    return elem
                raise StopIteration

            def __iter__(self):
                return self

        return _Iter()

for elem in Repeat('A', 5):
    print(elem, end = '')
