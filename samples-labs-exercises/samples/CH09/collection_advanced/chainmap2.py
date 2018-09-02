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

    def __getitem__(self, key: Hashable) -> Any:
        m = self.lookup(key)
        if m:
            return m[key]
        else:
            raise KeyError(key)

    def __setitem__(self, key: Hashable, value: Any):
        m = self.lookup(key)
        if m:
            m[key] = value
        else:
            self.dictLt.append({key: value})

    def __delitem__(self, key: Hashable):
        m = self.lookup(key)
        if m:
            del m[key]
            if len(m) == 0:
                self.dictLt.remove(m)
        else:
            raise KeyError(key)

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
