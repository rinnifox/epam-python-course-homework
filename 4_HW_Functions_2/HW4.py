import time
import requests


def make_cache(timer):

    def wrap_function(func):
        cache = {}
        times_dct = {}

        def wrapper(*args):

            if args in cache:
                end_time = time.time()
                if end_time-times_dct[args] > timer:
                    cache.pop(args)
                    val = func(*args)
                    cache[args] = val
                    times_dct.update({args: time.time()})
                    return val
                else:
                    print('getting from cache...')
                    return cache[args]
            else:
                val = func(*args)
                cache[args] = val
                times_dct.update({args:time.time()})
                return val

        return wrapper

    return wrap_function


# tests


@make_cache(12)
def check_code(site):
    try:
        r = requests.head(site)
        return r.status_code, r.url
    except requests.ConnectionError:
        print("failed to connect")


print(check_code('https://stackoverflow.com'))  # getting from function
print(check_code('https://github.com'))  # getting from function

time.sleep(10)

print(check_code('https://github.com'))  # getting from cache
print(check_code('https://stackoverflow.com'))  # getting from cache
print(check_code('https://www.youtube.com/'))  # getting from function

time.sleep(7)

print(check_code('https://github.com'))  # getting from function
print(check_code('https://stackoverflow.com'))  # getting from function
print(check_code('https://www.youtube.com/'))   # still getting from cache
