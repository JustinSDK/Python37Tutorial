from typing import AsyncIterator
from contextlib import asynccontextmanager
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

@asynccontextmanager
async def resource(name: str) -> AsyncIterator[Resource]:
    try:
        res = Resource(name)
        yield res
    finally:
        res.close()

async def task():
    async with resource('foo') as res:
        res.action()

loop = asyncio.get_event_loop()
loop.run_until_complete(task())
