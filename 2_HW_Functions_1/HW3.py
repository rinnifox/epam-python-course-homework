def atom(var=None):

    def get_value():
        nonlocal var
        return var

    def set_value(new_value):
        nonlocal var
        var = new_value
        return var

    def process_value(*args):
        nonlocal var
        for func in args:
            var = func(var)
        return var

    return get_value, set_value, process_value
