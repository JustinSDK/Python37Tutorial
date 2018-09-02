from typing import Dict
from threading import Thread, Lock

def setTo1(data: Dict[str, int], lock: Lock):
    while True:
        with lock:
            data['Justin'] = 1
            if data['Justin'] != 1:
                raise ValueError(f'setTo1 資料不一致：{data}')

def setTo2(data: Dict[str, int], lock: Lock):
    while True:
        with lock:
            data['Justin'] = 2
            if data['Justin'] != 2:
                raise ValueError(f'setTo2 資料不一致：{data}')

lock = Lock()
data: Dict[str, int] = {}

t1 = Thread(target = setTo1, args = (data, lock))
t2 = Thread(target = setTo2, args = (data, lock))

t1.start()
t2.start()

