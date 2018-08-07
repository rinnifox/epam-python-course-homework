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


operator = namedtuple('Operator_Info', ['priority', 'symbol'])


class Operators(Enum):

    MULT = operator(3, '*')
    DIV = operator(3, '/')
    PLUS = operator(2, '+')
    MIN = operator(2, '-')
    PAR_1 = operator(1, '(')
    PAR_2 = operator(1, ')')
    ALPHA = operator(0, 'alpha')


def brackets_trim(input_data: str) -> str:

    priority = {}

    for elem in Operators:
        priority.update({elem.value.symbol: elem.value.priority})

    def infix_to_postfix(infix_ex):
        op_stack = Stack()
        postfix_list = []
        token_list = infix_ex

        for token in token_list:
            if token.isalpha():
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
        priority_history = Stack()
        token_list = postfix_ex.split()

        for token in token_list:
            if token.isalpha():
                stack.append(token)
            else:
                op_priority = priority[token]

                elem1 = stack.pop()
                elem2 = stack.pop()

                if elem1.isalpha():
                    el1_priority = Operators.ALPHA.value.priority
                else:
                    el1_priority = priority_history.peek()

                if elem2.isalpha():
                    el2_priority = Operators.ALPHA.value.priority
                else:
                    el2_priority = priority_history.peek()

                if el1_priority < op_priority and el1_priority != 0:
                    elem1 = '(' + elem1 + ')'
                if el2_priority < op_priority and el2_priority != 0:
                    elem2 = '(' + elem2 + ')'

                stack.append(elem2 + token + elem1)

                priority_history.push(op_priority)

        return " ".join(stack)

    to_rpn = infix_to_postfix(input_data)
    from_rpn = postfix_to_infix(to_rpn)

    return from_rpn

