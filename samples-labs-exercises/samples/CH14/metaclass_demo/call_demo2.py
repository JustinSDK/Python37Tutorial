def metafunc(clsname, bases, attrs):
     print(clsname, bases, attrs)
     return type(clsname, bases, attrs)

class Some(metaclass = metafunc):
     def doSome(self):
         print('XD')

