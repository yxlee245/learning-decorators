print('### 12. More generic decorators ###')


def logger(func):
    def inner(*args, **kwargs):
        print(f'Arguments were: {args}, {kwargs}')
        return func(*args, **kwargs)
    return inner


@logger
def foo1(x, y=1):
    return x * y


@logger
def foo2():
    return 2


print(f'foo1(5, 4) > {foo1(5, 4)}')
print(f'foo1(x=1, y=2) > {foo1(x=1, y=2)}')
print(f'foo1(1) > {foo1(1)}')
print(f'foo1(1, y=2) > {foo1(1, y=2)}')
print(f'foo2() > {foo2()}')
