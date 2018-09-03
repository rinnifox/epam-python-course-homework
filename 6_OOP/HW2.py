from Modules import infix_to_postfix
from Modules import postfix_to_infix
import re


class AbstractOptimiser:
    def process(self, expressions):
        postfix = self.pre_process(expressions)
        optimized = self.process_internal(postfix)
        if optimized == postfix:
            return expressions
        else:
            return self.post_process(optimized)

    def pre_process(self, inf_expr):
        return infix_to_postfix(inf_expr)

    def process_internal(self, post_expr):
        return post_expr

    def post_process(self, opt_expr):
        a = postfix_to_infix(opt_expr)
        num = ''
        res = []
        for elem in a:
            if elem.isdigit() or elem.isalpha():
                num += elem
            else:
                if num:
                    res.append(num)
                    num = ''
                res.append(elem)
        if num:
            res.append(num)

        return res


class DoubleNegativeOptimiser(AbstractOptimiser):

    def process_internal(self, post_expr):
        # print('doub_neg input', post_expr)

        if '- -' in post_expr:
            expr = post_expr.replace(' ', '')
            pattern = r'[\S][-]{2}\Z'
            search = re.findall(pattern, expr)

            if len(expr) == 3:
                post_expr = post_expr.replace('- -', '')
            else:
                if search[0][0].isalpha():
                    post_expr = post_expr.replace('- -', '+')
                else:
                    post_expr = post_expr.replace(' - -', '')

        # print('doub_neg', post_expr)
        return post_expr


class IntegerCostantsOptimiser(AbstractOptimiser):
    def process_internal(self, post_expr):
        # print('int-opt input', post_expr)

        stack = []
        ops = set()
        digits = False

        for token in post_expr.split():
            if token.isalpha() or token.isdigit():
                stack.append(token)
                if token.isdigit():
                    digits = True
            else:
                ops.add(token)
                if token == '-' and len(stack) < 2:
                    stack.append(token)
                else:
                    elem1 = stack[-1]
                    elem2 = stack[-2]
                    if elem1.isdigit() and elem2.isdigit():
                        new_exp = elem2 + token + elem1
                        if '^' in new_exp:
                            new_exp = new_exp.replace('^', '**')
                        if '/' in new_exp:
                            new_exp = new_exp.replace('/', '//')

                        result = str(eval(new_exp))
                        stack.pop()
                        stack.pop()
                        if result[0] == '-':
                            stack.append(result[1:])
                            stack.append('-')
                        else:
                            stack.append(result)
                    else:
                        stack.append(token)

        # for addition only or multiplication only
        if (ops == {'+'} or ops == {'*'}) and digits == True:

            new_stack = ''
            operation = ops.pop()
            if operation == '+':
                for x in stack:
                    if x.isdigit():
                        expr = eval(new_stack + operation + x)
                        new_stack = str(expr)
            else:
                new_stack = '1'
                for y in stack:
                    if y.isdigit():
                        expr = eval(new_stack + operation + y)
                        new_stack = str(expr)

            for y in stack:
                if y.isalpha():
                    new_stack = new_stack + y + operation

            stack = new_stack

        # print('int optimizer', stack)
        return ' '.join(stack)


class UnnecessaryOperationsOptimiser(AbstractOptimiser):
    def process_internal(self, post_expr):
        # print('simple_input', post_expr)

        post_expr1 = ''

        while post_expr1 != post_expr:
            post_expr1 = post_expr

            div = r'[a-zA-Z\s]{4}[/]'
            search = re.findall(div, post_expr)
            alpha_set = set()
            for elem in search:
                for el in elem:
                    if el.isalpha():
                        alpha_set.update(el)
                if len(alpha_set) == 1:
                    post_expr = post_expr.replace(elem, '1')

            addzero = r'[0][\s\w]*[+|-]'
            search = re.findall(addzero, post_expr)
            for elem in search:
                for sym in elem:
                    if sym.isalpha():
                        post_expr = post_expr.replace(elem, sym)
                post_expr = post_expr.replace(elem, '')
                temp = post_expr.split()
                post_expr = ' '.join(temp)

            mulone = r'[1][\s\w]{,4}[*]'
            search = re.findall(mulone, post_expr)
            for elem in search:
                for sym in elem:
                    if sym.isalpha():
                        post_expr = post_expr.replace(elem, sym)
                post_expr = post_expr.replace(elem, '')
                temp = post_expr.split()
                post_expr = ' '.join(temp)

            mulzero = r'[\s\w]{,2}[0][\s\w]*[*]'
            search = re.findall(mulzero, post_expr)
            for elem in search:
                post_expr = post_expr.replace(elem, '0')

            if '^' in post_expr:
                post_expr = post_expr.replace('^', '**')
            pow = r'[\S\s]{,2}[\d][\s][*]{2}'
            search = re.findall(pow, post_expr)
            for elem in search:
                if '0' in elem:
                    post_expr = post_expr.replace(elem, '1')
                else:
                    for el in range (len(elem)-1):
                        if elem[el].isdigit():
                            if el % 2 == 0:
                                if elem[el-2] == '-':
                                    post_expr = post_expr.replace('-', '')
                            else:
                                if elem[el-2] and elem[el-4] == '-':
                                    post_expr = post_expr.replace('-', '')
                    post_expr = post_expr.replace('**', '^')
                    temp = post_expr.split()
                    post_expr = ' '.join(temp)

            sub = r'[\s\w]{4}[-]'
            search = re.findall(sub, post_expr)
            for elem in search:
                if elem[0] == elem[2]:
                    post_expr = post_expr.replace(elem, '0')

        # print('simplifyer', post_expr)
        return post_expr
