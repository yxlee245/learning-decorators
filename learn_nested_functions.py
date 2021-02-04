print('### 6. Nested functions ###')


def outer():
    x = 1
    def inner():
        print(f'x = {x}')
    inner()


outer()
