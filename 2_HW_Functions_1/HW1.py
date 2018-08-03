import inspect


def partial(func, *fixated_args, **fixated_kwargs):

    def wrapper(*args, **kwargs):
        nonlocal fixated_args
        fixated_args = fixated_args + args
        fixated_kwargs.update(kwargs)

        arg_names = inspect.getcallargs(func, *fixated_args, **fixated_kwargs)

        wrapper.__name__ = 'partial_{}'.format(func.__name__)
        wrapper.__doc__ = """ 
        A partial implementation of {} with pre-applied arguements being: {}
        """.format(func.__name__, arg_names)

        return func(*fixated_args, **fixated_kwargs)

    return wrapper
