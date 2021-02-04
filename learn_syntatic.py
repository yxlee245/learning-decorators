print('### 10. The @ symbol applies a decorator to a function ###')


class Coordinate:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return 'Coord: ' + str(self.__dict__)


def wrapper(func):
    def checker(a, b):
        if a.x < 0 or a.y < 0:
            a = Coordinate(max(a.x, 0), max(a.y, 0))
        if b.x < 0 or b.y < 0:
            b = Coordinate(max(b.x, 0), max(b.y, 0))
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(max(ret.x, 0), max(ret.y, 0))
        return ret
    return checker


# Equivalent to add = wrapper(add)
@wrapper
def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)


one = Coordinate(100, 200)
three = Coordinate(-100, -100)
print(f'add(one, three) > {add(one, three)}')
