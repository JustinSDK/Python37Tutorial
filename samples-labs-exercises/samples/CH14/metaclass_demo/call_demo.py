class SomeMeta(type):
    def __call__(cls, *args, **kwargs):
        print('call __new__')
        instance = cls.__new__(cls, *args, **kwargs)
        print('call __init__')
        cls.__init__(instance, *args, **kwargs)
        return instance

class Some(metaclass = SomeMeta):
    def __new__(cls):
        print('Some __new__')
        return object.__new__(cls)

    def __init__(self):
        print('Some __init__')

s = Some()