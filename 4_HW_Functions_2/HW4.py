import time


def make_cache(timer):
    start_time = time.time()

    def wrap_function(func):
        cache = {}

        def wrapper(*args):
            nonlocal start_time
            end_time = time.time()

            if end_time - start_time >= timer:
                cache.clear()
                start_time = time.time()

            if args in cache:
                return cache[args]
            else:
                val = func(*args)
                cache[args] = val
                return val

        return wrapper

    return wrap_function
