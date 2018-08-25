from HW1 import Calculator
from HW2 import DoubleNegativeOptimiser
from HW2 import IntegerCostantsOptimiser
from HW2 import SimplifierOptimiser


validate_check_list = [('a+2', True), ('a-(-2)', True), ('a+2-', False), ('a+(2+(3+5)', False), ('a^2', True),
    ('a^(-2)', True), ('-a-2', True), ('6/0', False), ('a/(b-b)', False), ('a/(5-5)', False)]

for case, exp in validate_check_list:
    tokens = list(case)
    calc = Calculator(tokens).validate()
    if calc != exp:
        print(f'Error in case for "{case}". Actual "{calc}", expected {exp}')
    else:
        print(f'OK in "{case}". Actual "{calc}", expected {exp}')


str_check_list = [("a", "a"), ("-a", "a-"), ("(a*(b/c)+((d-f)/k))", "abc/*df-k/+"), ("(a)", "a"), ("a*(b+c)", "abc+*"),
                  ("(a*(b/c)+((d-f)/k))*(h*(g-r))", "abc/*df-k/+hgr-**"), ("(x*y)/(j*z)+g", "xy*jz*/g+"),
                  ("a-(b+c)", "abc+-"), ("a/(b+c)", "abc+/"), ("a^(b+c)", "abc+^")]

for case, exp in str_check_list:
    tokens = list(case)
    calc = Calculator(tokens)
    if str(calc) != exp:
        print(f'Error in case for "{case}". Actual "{calc}", expected {exp}')
    else:
        print(f'OK in "{case}". Actual "{calc}", expected {exp}')


double_negate_tests = [
    ('-(-a)', 'a'),
    ('-(-5)', '5'),
    ('-(a+b)+c-(-d)', 'ab+-c+d+'),
]

for case, exp in double_negate_tests:
    tokens = list(case)
    calc = Calculator(tokens, [DoubleNegativeOptimiser()])
    calc.optimise()

    if str(calc) != exp:
        print(f'Error in case for "{case}". Actual "{calc}", expected {exp}')
    else:
        print(f'OK in"{case}". Actual "{calc}", expected {exp}')

integer_constant_optimiser_tests = [
    (['1'], ['1']),
    (['1', '+', '2'], ['3']),
    (['1', '-', '2'], ['1-']),
    (['2', '*', '2'], ['4']),
    (['2', '/', '2'], ['1']),
    (['2', '^', '10'], ['1024']),
    (['a', '+', '2', '*', '4'], ['a8+', '8a+']),
    (['2', '+', 'a', '+', '3'], ['5a+', 'a5+']),  # (*)
]

for case, exp in integer_constant_optimiser_tests:
    calc = Calculator(case, [DoubleNegativeOptimiser(), IntegerCostantsOptimiser()])

    calc.optimise()

    if str(calc) not in exp:
        print(f'Error in case for "{case}". Actual "{calc}", expected one of {exp}')
    else:
        print(f'OK in "{case}". Actual "{calc}", expected one of {exp}')


simplifier_optimiser_test = [
    ('a+0', ['a']),
    ('a*1', ['a']),
    ('a*0', ['0']),
    ('b/b', ['1']),
    ('a-a', ['0']),
    ('a+(b-b)', ['a']),
    ('a+(7-6-1)', ['a']),
    ('a^0', ['1']),
    ('a-(-(-a))', ['0']),
    ('(-a)^2', ['a2^']),
    ('-(-a)^3', ['a3^']),

    #('a+a+a', ['a3*', '3a*']),  # (*)
    #('(a-b)-(a-b)', ['0']),  # (*)
    #('(a-b)/(a-b)', ['1']),  # (*)
    #('(a+b)+(a+b)', ['ab+2*', '2ab+*']),  # (*)
    #('a*b+a*b', ['2ab**', '2ba**', 'a2b**', 'ab2**', 'b2a**', 'ba2**']),  # (*)
]

for case, exps in simplifier_optimiser_test:
    tokens = list(case)
    calc = Calculator(tokens, [DoubleNegativeOptimiser(), IntegerCostantsOptimiser(), SimplifierOptimiser()])

    calc.optimise()

    if str(calc) not in exps:
        print(f'Error in case for "{case}". Actual "{calc}", expected one of {exps}')
    else:
        print(f'OK in "{case}". Actual "{calc}", expected one of {exps}')