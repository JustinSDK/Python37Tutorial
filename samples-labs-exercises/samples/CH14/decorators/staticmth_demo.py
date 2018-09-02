from typing import Any, Type, Callable

class staticmth:    # 定義一個描述器
    def __init__(self, mth: Callable) -> None:
        self.mth = mth

    def __get__(self, instance: Any, owner: Type) -> Callable:
        return self.mth

class Some:
    @staticmth       # 相當於 doIt = staticmth(doIt)
    def doIt(a, b):
        print(a, b)

Some.doIt(1, 2) # 相當於 Some.__dict__['doIt'].__get__(None, Some)(1, 2)

s = Some()
# 以下相當於 Some.__dict__['doIt'].__get__(s, Some)(1)
# 所以以下會有錯 TypeError: doIt() missing 1 required positional argument ..
s.doIt(1)
