from typing import Tuple, List
from functools import reduce

Pt = Tuple[int, int]

class Knight:
    @staticmethod
    def travel(start: Pt) -> List[Pt]:
        route = [start]
        current = start
        for m in range(1, 64):
            possibleSteps = Knight.possible(route, current)
            if len(possibleSteps) == 0:
                break;
            if len(possibleSteps) == 1:
                current = possibleSteps[0]
            else:
                current = Knight.hard(route, possibleSteps)
            route.append(current)
        return route

    @staticmethod
    def possible(route: List[Pt], step: Pt) -> List[Pt]:
        dirs = [(-2, 1), (-1, 2), (1, 2),   (2, 1),
                (2, -1), (1, -2), (-1, -2), (-2, -1)]
        steps = [(step[0] + dir[0], step[1] + dir[1]) for dir in dirs]
        return [step for step in steps if Knight.isVisitable(route, step)]

    @staticmethod
    def isVisitable(route: List[Pt], step: Pt) -> bool:
        return -1 < step[0] < 8 and -1 < step[1] < 8 and not step in route

    @staticmethod
    def hard(route: List[Pt], steps: List[Pt]) -> Pt:
        allSteps = [Knight.possible(route, step) for step in steps]
        minIndex = reduce(
            lambda c, i: i if len(allSteps[i]) < len(allSteps[c]) else c,
            range(1, len(steps)), 0)
        return steps[minIndex]

x = int(input('x = '))
y = int(input('y =' ))
route = Knight.travel((x, y))
for i in range(8):
    for j in range(8):
        print('%3d' % (route.index((i, j)) + 1), end='')
    print()