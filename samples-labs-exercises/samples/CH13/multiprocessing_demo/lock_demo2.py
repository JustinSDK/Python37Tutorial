import multiprocessing
from multiprocessing.synchronize import Lock

def f(lock: Lock, i: int):
    with lock:
        print('hello world', i)
        print('hello world', i + 1)


if __name__ == '__main__':
    lock: Lock = multiprocessing.Lock()

    for num in range(100):
        multiprocessing.Process(target=f, args=(lock, num)).start()