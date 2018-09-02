from functools import wraps
from typing import Callable

def log(mth: Callable) -> Callable:
    @wraps(mth)
    def wrapper(self, *arg, **kwargs):
        print(self, arg, kwargs)
        return mth(self, *arg, **kwargs)

    return wrapper

class Some:
    @log
    def doIt(self, a, b):
        return a + b

s = Some()
print(s.doIt(1, 2))
