def atom(var=None):

    """
    To get and modify the variable:
    - get_value: atom(var)[0],
    - set_value: atom(var)[1](new_value),
    - process_value: atom(var)[2](functions)
    """

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
            for f in args:
                var = f(var)
            print('New value of variable = ', var)
        else:
            print('Impossible to process the variable, var = None')

        return var

    return get_value, set_value, process_value


# example function for the usage of process_value()
def example(value):
    return value ** 2


# example function for the usage of process_value
def example1(value):
    return value * 3


# example of usage of nested functions
a = atom()
a[0]()
a[1](5)
a[2](example, example1)
