from functools import reduce


def is_armstrong(number):

    digits = [i for i in str(number)]

    s = reduce(lambda a, b: a+b,  map(lambda x: x**(len(digits)), map(int, digits)))

    return True if s == number else False
