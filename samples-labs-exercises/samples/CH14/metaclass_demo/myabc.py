from typing import Any, Tuple, Dict, Type, Callable

Bases = Tuple[Type]
Attrs = Dict[str, Callable]

def abstract(func):
    func.__isabstract__ = True
    return func

def absmths(cls, mths):
    cls.__abstractmethods__ = frozenset(mths)

class Abstract(type):
    def __new__(mcls, clsname: str, bases: Bases, attrs: Attrs) -> Any:
        cls = super(mcls, mcls).__new__(mcls, clsname, bases, attrs)

        # 類別上定義的抽象方法
        abstracts = {name for name, value in attrs.items()
                       if getattr(value, "__isabstract__", False)}

        # 從父類別中繼承下來的抽象方法
        for parent in bases:
            for name in getattr(parent, "__abstractmethods__", set()):
                value = getattr(cls, name, None)
                if getattr(value, "__isabstract__", False):
                    abstracts.add(name)

        # 指定給 __abstractmethods__
        absmths(cls, abstracts)

        return cls

class AbstractX(metaclass=Abstract):
    @abstract
    def doSome(self):
        pass

# TypeError: Can't instantiate abstract class AbstractX with abstract methods doSome
x = AbstractX()