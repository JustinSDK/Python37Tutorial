import threading

class Resource:
    def __init__(self, name: str, resource: int) -> None:
        self.name = name
        self.resource = resource
        self.lock = threading.Lock()

    def action(self) -> int:
        with self.lock:
            self.resource += 1
            return self.resource

    def cooperate(self, other_res: 'Resource'):
        with self.lock:
            other_res.action()
            print(f'{self.name} 整合 {other_res.name} 的資源')

def cooperate(r1: Resource, r2: Resource):
    for i in range(10):
        r1.cooperate(r2)

res1 = Resource('resource 1', 10)
res2 = Resource('resource 2', 20)

t1 = threading.Thread(target = cooperate, args = (res1, res2))
t2 = threading.Thread(target = cooperate, args = (res2, res1))

t1.start()
t2.start()


