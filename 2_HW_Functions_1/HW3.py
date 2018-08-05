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
get1, set1, process1 = atom(10)
a = get1()
b = set1(3)
c = process1(example, example1)

get2, set2, process2 = atom(20)
d = get2()
e = set2(5)
f = process2(example, example1)

print(a, b, c)
print(d, e, f)



