import inspect


def partial(func, *fixated_args, **fixated_kwargs):

    def wrapper(*args, **kwargs):
        nonlocal fixated_args
        fixated_args = fixated_args + args
        fixated_kwargs.update(kwargs)
        return func(*fixated_args, **fixated_kwargs)

    setargs = {}
    otherargs = []

    setargs_names = inspect.getfullargspec(func)[0]

    if len(setargs_names) > len(fixated_args):
        someargs = fixated_args
    else:
        someargs = setargs_names

    for i in range(len(someargs)):
        setargs.update({setargs_names[i]: fixated_args[i]})

    if len(fixated_args) > len(setargs_names):
        otherargs = fixated_args[len(setargs):]

    wrapper.__name__ = 'partial_{}'.format(func.__name__)
    wrapper.__doc__ = """ 
    A partial implementation of {} with pre-applied arguements being: position_args = {}, *args = {}, **kwargs = {}
    """.format(func.__name__, setargs, otherargs, fixated_kwargs)

    return wrapper


# TESTS

def avg(a, b):
    return (a+b)/2


def random_func(a, *args, **kwargs):
    zero = a + 3
    first = sum(args)/2
    second = kwargs
    return zero, first, second


_avg = partial(avg, 4, 3)
print(_avg.__name__)
print(_avg.__doc__)
print(_avg())

_avg = partial(avg, 4)
print(_avg.__name__)
print(_avg.__doc__)
print(_avg(3))

_avg = partial(avg)
print(_avg.__name__)
print(_avg.__doc__)
print(_avg(3, 4))

_random_func = partial(random_func, 4, 3, 6, x=5)
print(_random_func.__name__)
print(_random_func.__doc__)
print(_random_func())

