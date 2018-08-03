def make_it_count(func, counter_name):

    def wrapper(*args, **kwargs):
        nonlocal counter_name

        for key, value in globals().items():
            if value == counter_name:
                globals()[key] = value+1
                counter_name += 1

        return func(*args, **kwargs)

    return wrapper