# Learning about Decorators in Python

## About this repo
The main portion of codes in this repo was inspired from
[this excellent post](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)
that gives an intuitive step-by-step introduction to using decorators in Python.
I have also added in this repo some additional examples of how decorators can be
used.

## Specs
Python 3.7.8 was used to execute the scripts in this repo. Modifications may be
needed if earlier versions of Python is used.

## The step-by-step introduction
The following scripts correspond to the 12 steps mentioned in the steps
mentioned in the abovementioned blog post:
1. Functions: [`learn_functions.py`](learn_functions.py)
2. Scope: [`learn_scope.py`](learn_scope.py)
3. Variable resolution rules:
[`learn_variable_resolution_rules.py`](learn_variable_resolution_rules.py)
4. Variable lifetime:
[`learn_variable_lifetime.py`](learn_variable_lifetime.py)
5. Function arguments and parameters:
[`learn_function_args.py`](learn_function_args.py)
6. Nested functions: [`learn_nested_functions.py`](learn_nested_functions.py)
7. Functions are first class objects in Python
[`learn_function_objects.py`](learn_function_objects.py)
8. Closures: [`learn_closures.py`](learn_closures.py)
9. Decorators!: [`learn_decorators.py`](learn_decorators.py)
10. The `@` symbol applies a decorator to a function
[`learn_syntatic.py`](learn_syntatic.py)
11. `*args` and `**kwargs`: [`learn_args_kwargs.py`](learn_args_kwargs.py)
12. More generic decorators:
[`learn_generic_decorators.py`](learn_generic_decorators.py)

## More examples

### Example 1
Imagine that you want to record and print out the execution time of all the
functions you execute in a script (perhaps to get a sense of how fast these
functions run). Without using a decorator, one might probably do something like
this:
```
time_start = time.time()
func1()
print(time.time() - time_start)

time_start = time.time()
func2()
print(time.time() - time_start)

...
```
While this approach may be reasonable for a small number of functions, it will
become repetitive and error-prone if you wish to time a significant number of
functions. With the use of a decorator, measurement of function runtime can be
performed for a large number of functions with much less repeated code.
[`example1.py`](example1.py) shows how this can be done.

### Example 2
Inspired from the example of logging in step 12 (More generic decorators), in
this example, the built-in logging module is used to print out log messages:
- before execution of each function
- after execution of each function
- for errors that occur during execution

The "non-decorator" way to do this would be something like this:
```
logger.info('Executing func1...')
try:
    func1()
    logger.info('Successfully executed func1')
except Exception as e:
    logger.error(f'Failed to execute func1: {e}')

logger.info('Executing func2...')
try:
    func2()
    logger.info('Successfully executed func2')
except Exception as e:
    logger.error(f'Failed to execute func2: {e}')

...
```
which is repetitive and prone to errors and typos, especially when you want to
do logging for a large number of functions. Decorators can help to greatly
reduce the repetition of code for logging, which makes our lives so much easier.
[`example2.py`](example2.py) shows how this can be done.