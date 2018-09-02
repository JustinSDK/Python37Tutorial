import asyncio
import time
import random

async def asyncFoo(n: float):
    time.sleep(n)
    return n * random.random()

async def asyncTasks():
    r1 = await asyncFoo(1)
    r2 = await asyncFoo(r1)
    r3 = await asyncFoo(r2)
    print(r3)

async def asyncMoreTasks():
    await asyncTasks()
    await asyncTasks()

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncFoo(1))
loop.run_until_complete(asyncTasks())
loop.run_until_complete(asyncMoreTasks())
