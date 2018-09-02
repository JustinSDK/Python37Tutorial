from concurrent.futures import ProcessPoolExecutor
import time

def fib(n: int) -> int:
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__=='__main__':
    with ProcessPoolExecutor() as executor:
        begin = time.time()
        futures = [executor.submit(fib, n) for n in range(3, 35)]
        fibs = [future.result() for future in futures]
        print(time.time() - begin)
        print(fibs)
