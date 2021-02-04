print('### 8. Closures ###')


def outer(x):
    def inner():
        print(f'x = {x}')
    return inner


print1 = outer(1)
print2 = outer(2)
print1()
print2()
