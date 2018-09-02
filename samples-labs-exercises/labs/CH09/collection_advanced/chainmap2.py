from typing import Any, Set, Dict, Hashable, Optional
from collections.abc import MutableMapping

class ChainMap(MutableMapping):
    def __init__(self, *tulp: Dict) -> None:
        self.dictLt = list(tulp)

    def lookup(self, key: Hashable) -> Optional[Dict]:
        for m in self.dictLt:
            if key in m:
                return m
        return None


    # 完成未實作之協定
    
    def key_set(self) -> Set:
        keys: Set = set()
        for m in self.dictLt:
            keys.update(m.keys())
        return keys

    def __iter__(self):
        return iter(self.key_set())

    def __len__(self):
        return len(self.key_set())


c = ChainMap({'A' : 'Justin'}, {'A' : 'Monica', 'B' : 'Irene'})
print(list(c))
print(len(c))
print(c.pop('A'))
print(list(c.keys()))
