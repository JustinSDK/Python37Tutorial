from typing import Any, Type, Callable
from functools import wraps

class classmth:
    def __init__(self, mth: Callable) -> None:
        self.mth = mth

    def __get__(self, instance: Any, owner: Type) -> Callable:
        @wraps(self.mth)
        def wrapper(*arg, **kwargs):
            return self.mth(owner, *arg, **kwargs)

        return wrapper

class Other:
    @classmth   # 相當於 doIt = classmth(doIt)
    def doIt(cls, a, b):
        print(cls, a, b)

Other.doIt(1, 2)  # 相當 Other.__dict__['doIt'].__get__(None, Other)(1, 2)

o = Other()
o.doIt(1, 2)      # 相當 Other.__dict__['doIt'].__get__(o, Other)(1, 2)