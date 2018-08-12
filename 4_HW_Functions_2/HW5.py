import time


def dec_counter(var_name: str):
    start_time = time.time()

    def wrap_function(func):
        call_counter = 0

        def wrapper(*args):
            nonlocal call_counter
            call_counter +=1
            val = func(*args)
            current_time = time.time()
            globals()[var_name] = (current_time-start_time, call_counter)
            return val

        return wrapper

    return wrap_function
