print('### 3. Variable resolution rules')
print('a. Printing global variable in a function:')
a_string = 'This is a global variable'


def foo():
    print(f'a_string = {a_string}')


foo()

print('b. Assign to global variable inside function:')
a_string = 'This is a global variable'


def foo():
    a_string = 'test'
    print(f'locals() > {locals()}')


foo()
print(f'a_string = {a_string}')
