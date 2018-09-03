from Modules import infix_to_postfix
from HW2 import UnnecessaryOperationsOptimiser
from HW2 import IntegerCostantsOptimiser


class Calculator:
    def __init__(self, opcodes: list, operators=None):
        self.opcodes = opcodes
        self.operators = operators if operators is not None else []

    def __str__(self) -> str:
        res = infix_to_postfix(self.opcodes).replace(' ', '')
        return res

    def optimise(self):
        for operator in self.operators:
            self.opcodes = operator.process(self.opcodes)

    def validate(self) -> bool:
        operations = ['+', '-', '*', '/']
        parenthesis = ['(', ')']
        parenthesis_counter = 0

        if self.opcodes[0] in operations and self.opcodes[0] != '-' or self.opcodes[0] == ')':
            print('err', 0)
            return False

        if self.opcodes[len(self.opcodes)-1] in operations or self.opcodes[len(self.opcodes)-1] == '(':
            # print('err', 1)
            return False

        if self.opcodes[len(self.opcodes)-1] == ')':
            parenthesis_counter -= 1

        for token in range(len(self.opcodes)-1):

            if self.opcodes[token].isdigit():
                if self.opcodes[token+1].isalpha():
                    # print('err', 2)
                    return False

            elif self.opcodes[token].isalpha():
                if self.opcodes[token+1].isdigit() or self.opcodes[token+1].isalpha():
                    # print('err', 3)
                    return False

            elif self.opcodes[token] in operations:
                if self.opcodes[token + 1] in operations or self.opcodes[token + 1] == ')':
                    # print('err', 4)
                    return False
                if self.opcodes[token] == '/':
                    if self.opcodes[token+1] == '0':
                        return False
                    if '0' not in self.opcodes:
                        temp = self.opcodes
                        temp = UnnecessaryOperationsOptimiser().process(temp)
                        temp = IntegerCostantsOptimiser().process(temp)
                        if '/' in temp:
                            i = temp.index('/')
                            if temp[i+1] == '0':
                                return False

            elif self.opcodes[token] in parenthesis:
                if self.opcodes[token] == '(':
                    if self.opcodes[token + 1] in operations and self.opcodes[token + 1] != '-':
                        # print('err', 5)
                        return False
                    parenthesis_counter += 1
                if self.opcodes[token] == ')':
                    if self.opcodes[token + 1].isdigit() or self.opcodes[token + 1].isalpha():
                        # print('err', 6)
                        return False
                    parenthesis_counter -= 1

        if parenthesis_counter != 0:
            return False

        return True
