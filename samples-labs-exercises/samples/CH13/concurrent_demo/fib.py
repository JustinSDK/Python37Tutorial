import time

def fib(n: int) -> int:
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

begin = time.time()
fibs = [fib(n) for n in range(3, 35)]
print(time.time() - begin)
print(fibs)
