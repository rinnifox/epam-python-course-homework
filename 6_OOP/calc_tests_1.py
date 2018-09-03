from HW1 import Calculator
from HW2 import DoubleNegativeOptimiser
from HW2 import IntegerCostantsOptimiser
from HW2 import UnnecessaryOperationsOptimiser


def test_05_simplify():
    simplifier_optimiser_test = [
        ('-(-a)', ['a']),
        ('-(-(-(-a)))', ['a']),
        ('-(-5)', ['5']),
        ('-(a+b)+c-(-d)', ['ab+-c+d+']),
        ('-(-(a+b))', ['ab+c+']),
        ('1', ['1']),
        ('1+2', ['3']),
        ('1-2', ['-1']),
        ('2*2', ['4'],),
        ('2/2', ['1']),
        ('33/10', ['3']),
        ('2^10', ['1024']),
        ('a+2*4', ['a8+']),
        ('a+0', ['a']),
        ('a*1', ['a']),
        ('a*0', ['0']),
        ('b/b', ['1']),
        ('a-a', ['0']),
        ('a+(b-b)', ['a']),
        ('a+(7-6-1)', ['a']),
        ('a^0', ['1']),
        ('a-(-(-a))', ['0'])
    ]

    print('{: <20} {: <10} {: <5}'.format('Case', 'Result', 'Is good?'))
    print('='*37)

    for case, exps in simplifier_optimiser_test:
            tokens = list(case)
            calc = Calculator(tokens, [DoubleNegativeOptimiser(), IntegerCostantsOptimiser(), UnnecessaryOperationsOptimiser()])
            if calc.validate():
                calc.optimise()
                res = 'True' if str(calc) in exps else 'False'

                print(f'{case: <20} {str(calc): <10} {res: <5}')
            else:
                print(f'{case: <20} is not valid')


print(test_05_simplify())
