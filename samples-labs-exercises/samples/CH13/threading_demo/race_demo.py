from typing import Dict
import threading

def setTo1(data: Dict[str, int]):
    while True:
        data['Justin'] = 1
        if data['Justin'] != 1:
            raise ValueError(f'setTo1 資料不一致：{data}')

def setTo2(data: Dict[str, int]):
    while True:
        data['Justin'] = 2
        if data['Justin'] != 2:
            raise ValueError(f'setTo2 資料不一致：{data}')

data: Dict[str, int] = {}

t1 = threading.Thread(target = setTo1, args = (data, ))
t2 = threading.Thread(target = setTo2, args = (data, ))

t1.start()
t2.start()

