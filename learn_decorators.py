print('### 9. Decorators! ###')
print('a. Simple example of decorator:')


def outer(some_func):
    def inner():
        print('Before some_func')
        ret = some_func()
        return ret + 1
    return inner


def foo():
    return 1


decorated = outer(foo)
print(f'decorated() > {decorated()}')

print('b. Re-assigning the variable containing our function:')
foo = outer(foo)
print(f'foo = {foo}')

print('c. Preparation for example of more useful decorator:')


class Coordinate:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return ' '.join(['Coord:', str(self.__dict__)])


def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)


def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)


one = Coordinate(100, 200)
two = Coordinate(300, 200)
print(f'add(one, two) > {add(one, two)}')
three = Coordinate(-100, -100)
print(f'sub(one, two) > {sub(one, two)}')
print(f'add(one, three) > {add(one, three)}')

print('d. Useful decorator to check bounds of coordinates:')


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


add = wrapper(add)
sub = wrapper(sub)
print(f'sub(one, two) > {sub(one, two)}')
print(f'add(one, three) > {add(one, three)}')
