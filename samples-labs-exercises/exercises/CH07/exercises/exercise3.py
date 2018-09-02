import sys
from types import TracebackType
from typing import Type, Any, Generator, Callable, Optional, ContextManager

WrappedFunc = Callable[..., Generator]
CtxMgrWrapper = Callable[[Any], ContextManager]

def contextmanager(func: WrappedFunc) -> CtxMgrWrapper:
    def wraps(*args: Any, **kwargs: Any) -> ContextManager:
        g = func(*args, **kwargs)

        class ContextDecorator:
            def __enter__(self):
                return next(g)

            def __exit__(self, exc_type: Optional[Type[BaseException]],
                         exc_value: Optional[BaseException],
                         traceback: Optional[TracebackType]) -> Optional[bool]:
                if exc_type:
                    try:
                        g.throw(exc_type, exc_value, traceback)
                    except StopIteration:
                        pass
                    return True
                return False

        return ContextDecorator()

    return wraps

def suppress0(ex_type: Type[BaseException]) -> Generator:
    try:
        yield
    except ex_type:
        pass

suppress: CtxMgrWrapper = contextmanager(suppress0)

with suppress(FileNotFoundError):
    for line in open(sys.argv[1]):
        print(line, end='')

def closing0(thing: Any) -> Generator:
    try:
        yield thing
    finally:
        thing.close()

closing: CtxMgrWrapper = contextmanager(closing0)

class Some:
    def __init__(self, name: str) -> None:
        self.name = name

    def close(self):
        print(self.name, 'is closed.')


with closing(Some('Resource')) as res:
    print(res.name)
