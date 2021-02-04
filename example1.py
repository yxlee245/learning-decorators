from typing import Callable, Any
import time


def timer(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def inner(*args: Any, **kwargs: Any) -> Any:
        time_start = time.time()
        ret = func(*args, **kwargs)
        duration = time.time() - time_start
        print(
            f'Time taken for function `{func.__name__}` to execute:\n'
            f'~{duration:.3f} s\n'
            f'~{1000 * duration:.3f} ms'
        )
        return ret
    return inner


@timer
def loop():
    for i in range(10000):
        if i % 1000 == 0:
            print(i)


@timer
def average(*args):
    return sum(args) / len(args)


print('Executing loop()...')
loop()
print('Executing average(*range(1, 100001))...')
print(f'average(*range(1, 100001)) > {average(*range(1, 100001))}')