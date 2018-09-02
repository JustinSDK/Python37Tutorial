from types import TracebackType
from typing import Optional, Type, AsyncContextManager
import asyncio
import time

class Resource:
    def __init__(self, name: str) -> None:
        self.name = name
        time.sleep(5)
        print('resource prepared')

    def action(self):
        print(f'use {self.name} resource ...')

    def close(self):
        time.sleep(5)
        print('resource closed')

def resource(name: str) -> AsyncContextManager[Resource]:
    class AsyncCtxManager:
        async def __aenter__(self) -> Resource:
            self.resource = Resource(name)
            return self.resource

        async def __aexit__(self, exc_type: Optional[Type[BaseException]],
                     exc_value: Optional[BaseException],
                     traceback: Optional[TracebackType]) -> Optional[bool]:
            self.resource.close()
            return False

    return AsyncCtxManager()

async def task():
    async with resource('foo') as res:
        res.action()

loop = asyncio.get_event_loop()
loop.run_until_complete(task())
