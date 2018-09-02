from typing import Any, Callable
from collections import UserList

Consume = Callable[[Any], None]
Predicate = Callable[[Any], bool]
Mapper = Callable[[Any], Any]

class MthChainList(UserList):
    def for_each(self, consume: Consume):
        for elem in self:
            consume(elem)

    def filter(self, predicate: Predicate):
        return MthChainList(elem for elem in self if predicate(elem))

    def map(self, mapper: Mapper):
        return MthChainList(mapper(elem) for elem in self)

lt = MthChainList(['a', 'B', 'c', 'd', 'E', 'f', 'G'])
lt.filter(str.islower).map(str.upper).for_each(print)