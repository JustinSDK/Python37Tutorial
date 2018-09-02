from queue import Queue
import threading

def producer(clerk: Queue):
    for product in range(10):
        clerk.put(product)
        print(f'店員進貨 ({product})')

def consumer(clerk: Queue):
    for product in range(10):
        print(f'店員賣出 ({clerk.get()})')

clerk: Queue = Queue(1);
threading.Thread(target = producer, args = (clerk, )).start()
threading.Thread(target = consumer, args = (clerk, )).start()
