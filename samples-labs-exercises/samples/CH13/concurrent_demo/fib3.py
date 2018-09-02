from concurrent.futures import ProcessPoolExecutor
import time

def fib(n: int) -> int:
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__=='__main__':
    with ProcessPoolExecutor() as executor:
        begin = time.time()
        fibs = [n for n in executor.map(fib, range(3, 35))]
        print(time.time() - begin)
        print(fibs)
