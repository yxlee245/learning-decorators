from typing import Callable, Any
import logging
import sys


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s: %(name)s - %(levelname)s - %(message)s'
)
handler.setFormatter(formatter)
logger.addHandler(handler)


def log_wrapper(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def inner(*args: Any, **kwargs: Any):
        logger.info(f'Executing function `{func.__name__}`')
        try:
            ret = func(*args, **kwargs)
            logger.info(f'Function `{func.__name__}` executed successfully')
            return ret
        except Exception as e:
            logger.error(
                f'Failed to execute function `{func.__name__}` successfully:'
                f' {e}'
            )
    return inner


@log_wrapper
def loop():
    for i in range(10000):
        if i % 1000 == 0:
            print(i)


@log_wrapper
def average(*args):
    return sum(args) / len(args)


@log_wrapper
def error_func():
    return 1 / 0


loop()
logger.info(f'average(*range(1, 100001)) > {average(*range(1, 100001))}')
error_func()