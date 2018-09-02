from typing import Generic, TypeVar, Dict, DefaultDict
from collections import defaultdict
from collections.abc import MutableMapping

KT = TypeVar('KT')
VT = TypeVar('VT')

class MultiMap(Generic[KT, VT], MutableMapping):
    def __init__(self, *tulp: Dict[KT, VT]) -> None:
        self.map: DefaultDict = defaultdict(set)
        for m in tulp:
            for k in m:
                self.map[k].add(m[k])

    def __getitem__(self, key: KT) -> VT:
        if key in self.map:
            return self.map[key]
        raise KeyError(key)

    def __setitem__(self, key: KT, value: VT):
        self.map[key].add(value)

    def __delitem__(self, key: KT):
        del self.map[key]

    def __iter__(self):
        return iter(self.map)

    def __len__(self):
        return len(self.map)

    def __str__(self):
        return str(self.map)[len("defaultdict(<class 'set'>, ") :  -1]

mmap = MultiMap({'A' : 'Justin'}, {'A' : 'Monica', 'B' : 'Irene'})
print(mmap) # 顯示 {'B': {'Irene'}, 'A': {'Justin', 'Monica'}}

mmap['B'] = 'Pika'
print(mmap) # 顯示 {'B': {'Irene', 'Pika'}, 'A': {'Justin', 'Monica'}}

