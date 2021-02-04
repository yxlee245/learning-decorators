print('### 4. Variable lifetime ###')


def foo():
    x = 1


foo()
try:
    print(x)
except NameError as e:
    print(f'!! NameError: {e}')
