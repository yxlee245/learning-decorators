print('### 2. Scope ###')
a_string = 'This is a global variable'


def foo():
    print(f'locals() > {locals()}')


print(f'globals() > {globals()}')
foo()
