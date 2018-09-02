import threading

class Clerk:
    def __init__(self):
        self.product = -1
        self.cond = threading.Condition()

    def purchase(self, product: int):
        with self.cond:
            while self.product != -1:
                self.cond.wait()
            self.product = product
            self.cond.notify()

    def sellout(self) -> int:
        with self.cond:
            while self.product == -1:
                self.cond.wait()
            p = self.product
            self.product = -1
            self.cond.notify()
            return p

def producer(clerk: Clerk):
    for product in range(10):
        clerk.purchase(product)
        print(f'店員進貨 ({product})')

def consumer(clerk: Clerk):
    for product in range(10):
        print(f'店員賣出 ({clerk.sellout()})')


clerk = Clerk();
threading.Thread(target = producer, args = (clerk, )).start()
threading.Thread(target = consumer, args = (clerk, )).start()
