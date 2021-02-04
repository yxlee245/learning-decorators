print('### 5. Function arguments and parameters ###')
print('a. Example of function with exactly one argument:')


def foo(x):
    print(f'locals() > {locals()}')


foo(1)

print('b. Example of function with positional and named arguments:')


def foo(x, y=0):
    return x - y


print(f'foo(3, 1) > {foo(3, 1)}')
print(f'foo(3) > {foo(3)}')
try:
    print(f'foo() > {foo()}')
except TypeError as e:
    print(f'!! TypeError: {e}')
print(f'foo(y=1, x=3) > {foo(y=1, x=3)}')
