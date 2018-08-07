def atom(var=None):

    def get_value():
        nonlocal var
        print('The value of variable = ', var)
        return var

    def set_value(new_value):
        nonlocal var
        var = new_value
        print('New value of variable = ', var)
        return var

    def process_value(*args):
        nonlocal var
        if var:
            for func in args:
                var = func(var)
            print('New value of variable = ', var)
        else:
            print('Impossible to process the variable, var = None')

        return var

    return get_value, set_value, process_value



