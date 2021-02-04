print('### 11. *args and **kwargs ###')
print('a. Example of using *args:')


def one(*args):
    print(f'Arguments of function `one`: {args}')


one()
one(1, 2, 3)


def two(x, y, *args):
    print(f'Arguments of function `two`: {x}, {y}, {args}')


two('a', 'b', 'c')

print('b. Example of using * to unpack an iterable:')


def add(x, y):
    return x + y


lst = [1, 2]
print(f'add(lst[0], lst[1]) > {add(lst[0], lst[1])}')
print(f'add(*lst) > {add(*lst)}')

print('c. Example of using **kwargs:')


def foo(**kwargs):
    print(f'Arguments of function `foo`: {kwargs}')


foo()
foo(x=1, y=2)

print('d. Example of using ** to unpack a dict:')
dct = {'x': 1, 'y': 2}


def bar(x, y):
    return x + y


print(f'bar(**dct) > {bar(**dct)}')
