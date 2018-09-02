from typing import Any, Type

class Descriptor:
    def __get__(self, instance: Any, owner: Type):
        print(self, instance, owner, end = '\n\n')

    def __set__(self, instance: Any, value: Any):
        print(self, instance, value, end = '\n\n')

    def __delete__(self, instance: Any):
        print(self, instance, end = '\n\n')

class Some:
    x = Descriptor()

s = Some()
s.x
s.x = 10
del s.x

Some.x
