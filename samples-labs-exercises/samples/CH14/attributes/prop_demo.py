from typing import Any, Callable, Type

Getter = Callable[[Any], Any]
Setter = Callable[[Any, Any], None]
Deleter = Callable[[Any], None]

class PropDescriptor:
    def __init__(self, getter: Getter, setter: Setter, deleter: Deleter) -> None:
        self.getter = getter
        self.setter = setter
        self.deleter = deleter

    def __get__(self, instance: Any, owner: Type) -> Any:
        return self.getter(instance)

    def __set__(self, instance: Any, value: Any):
        self.setter(instance, value)

    def __delete__(self, instance: Any):
        self.deleter(instance)

def prop(getter: Getter, setter: Setter, deleter: Deleter) -> PropDescriptor:
    return PropDescriptor(getter, setter, deleter)

class Ball:
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError('必須是正數')
        self.__radius = radius

    def get_radius(self) -> float:
        return self.__radius

    def set_radius(self, radius: float):
        self.__radius = radius

    def del_radius(self):
        del self.__radius

    radius = prop(get_radius, set_radius, del_radius)

ball = Ball(10)
print(ball.radius)
ball.radius = 5
print(ball.radius)
