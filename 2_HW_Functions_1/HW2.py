def make_it_count(func, counter_name):

    def wrapper(*args, **kwargs):
        globals()[counter_name] += 1
        return func(*args, **kwargs)

    return wrapper
