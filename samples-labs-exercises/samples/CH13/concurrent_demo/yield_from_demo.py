
from concurrent.futures import ThreadPoolExecutor
import time
import random

def doAsync(task):
    g = task()
    future = next(g)
    while True:
        try:
            future = g.send(future.result())
            g.send(future.result())
        except StopIteration:
            break

def asyncFoo(n):
    def process(n):
        time.sleep(n)
        return n * random.random()

    with ThreadPoolExecutor(max_workers=4) as executor:
        return executor.submit(process, n)

def asyncTasks():
    r1 = yield asyncFoo(1)
    r2 = yield asyncFoo(r1)
    r3 = yield asyncFoo(r2)
    print(r3)

doAsync(asyncTasks)

def asyncMoreTasks():
    yield from asyncTasks()
    yield from asyncTasks()

doAsync(asyncMoreTasks)