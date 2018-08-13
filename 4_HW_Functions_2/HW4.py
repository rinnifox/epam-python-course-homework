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
                # print('clearing')      # можно включить, чтобы понаблюдать за очисткой
                start_time = time.time()

            if args in cache:
                return cache[args]
            else:
                val = func(*args)
                cache[args] = val
                # print(cache)           # можно включить, чтобы понаблюдать за очисткой
                return val

        return wrapper

    return wrap_function


@make_cache(0.0001)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


print(fib(5))
print(fib(2))
print(fib(10))
print(fib(6))

