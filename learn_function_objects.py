print('### 7. Functions are first class objects in Python ###')
print('a. In Python, functions are objects just like everything else:')
print(f'issubclass(int, object) > {issubclass(int, object)}')
# all objects in Python inherit from a common baseclass


def foo():
    pass


print(f'foo.__class__ = {foo.__class__}')
print(
    f'issubclass(foo.__class__, object) > {issubclass(foo.__class__, object)}'
)

print('b. Example o fpassing functions to functions as argument:')


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def apply(func, x, y):
    return func(x, y)


print(f'apply(add, 2, 1) . {apply(add, 2, 1)}')
print(f'apply(sub, 2, 1) > {apply(sub, 2, 1)}')

print('c. Example of returning functions as values:')


def outer():
    def inner():
        print('Inside inner')
    return inner


foo = outer()
print(f'foo = {foo}')
foo()
