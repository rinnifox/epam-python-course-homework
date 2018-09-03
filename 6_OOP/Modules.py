from enum import Enum
from collections import namedtuple


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


op = namedtuple('Operator_Info', ['priority', 'symbol'])


class Operators(Enum):
    POW = op(4, '^')
    DIV = op(3, '/')
    MULT = op(3, '*')
    MIN = op(2, '-')
    PLUS = op(2, '+')
    PAR_1 = op(1, '(')
    PAR_2 = op(1, ')')
    SYMBOL = op(0, 'symbol')


priority = {}

for elem in Operators:
    priority.update({elem.value.symbol: elem.value.priority})


def infix_to_postfix(token_list):

        op_stack = Stack()
        postfix_list = []

        new_token_list = list()
        number = ''

        for elem in token_list:
            if elem.isdigit():
                number = ''.join([number, elem])
            else:
                if number != '':
                    new_token_list.append(number)
                new_token_list.append(elem)
                number = ''

        if number != '':
            new_token_list.append(number)

        token_list = new_token_list

        for token in token_list:
            if token.isalpha() or token.isdigit():
                postfix_list.append(token)
            elif token == '(':
                op_stack.push(token)
            elif token == ')':
                top_token = op_stack.pop()

                while top_token != '(':
                    postfix_list.append(top_token)
                    top_token = op_stack.pop()

            else:
                while (not op_stack.isEmpty()) and (priority[op_stack.peek()] >= priority[token]):
                    postfix_list.append(op_stack.pop())
                op_stack.push(token)

        while not op_stack.isEmpty():
            postfix_list.append(op_stack.pop())

        return " ".join(postfix_list)


def postfix_to_infix(postfix_ex):
    stack = []
    priority_history = []
    token_list = postfix_ex.split()

    for token in token_list:
        if token.isalpha() or token.isdigit():
                stack.append(token)
        elif token == '-' and len(stack) == 1:
            elem = stack.pop()
            stack.append('-({})'.format(elem))
            priority_history.append(1)
        else:
            op_priority = priority[token]

            elem1 = stack.pop()
            elem2 = stack.pop()

            if elem1.isalpha() or elem1.isdigit():
                    el1_priority = Operators.SYMBOL.value.priority
            else:
                el1_priority = priority_history.pop()
                if token == Operators.DIV.value.symbol and el1_priority == Operators.DIV.value.priority:
                    el1_priority -= 0.5
                elif token == Operators.MIN.value.symbol and el1_priority == Operators.MIN.value.priority:
                    el1_priority -= 0.5

            if elem2.isalpha() or elem2.isdigit():
                el2_priority = Operators.SYMBOL.value.priority
            else:
                el2_priority = priority_history.pop()

            if el1_priority < op_priority and el1_priority != 0:
                    elem1 = '(' + elem1 + ')'
            if el2_priority < op_priority and el2_priority != 0:
                elem2 = '(' + elem2 + ')'

            stack.append(elem2 + token + elem1)

            priority_history.append(op_priority)

    return ' '.join(stack)

