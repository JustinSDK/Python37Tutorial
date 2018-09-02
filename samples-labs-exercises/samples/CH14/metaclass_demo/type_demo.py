from typing import Any, Tuple, Dict, Type, Callable

Bases = Tuple[Type]
Attrs = Dict[str, Callable]

class SomeMeta(type):
    def __new__(mcls, clsname: str, bases: Bases, attrs: Attrs) -> Any:
        cls = super(mcls, mcls).__new__(
            mcls, clsname, bases, attrs)
        print('SomeMeta __new__', mcls, clsname, bases, attrs)
        return cls

    def __init__(self, clsname: str, bases: Bases, attrs: Attrs) -> None:
        super(type(self), self).__init__(clsname, bases, attrs)
        print('SomeMeta __init__', self, clsname, bases, attrs)

Some = SomeMeta('Some', (object,), {'doSome' : (lambda self, x: print(x))})

s = Some()
s.doSome(10)
