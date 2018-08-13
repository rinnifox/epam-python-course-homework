import time


def dec_counter(var_name: str):
    start_time = time.time()

    def wrap_function(func):
        call_counter = 0

        def wrapper(*args):
            nonlocal call_counter
            call_counter +=1
            val = func(*args)
            current_time = time.time()
            globals()[var_name] = (current_time-start_time, call_counter)
            return val

        return wrapper

    return wrap_function


x = 15

# recursive

counter1 = 0


@dec_counter('counter1')
def fib_rec(n):
    if n < 2:
        return n
    return fib_rec(n-1) + fib_rec(n-2)


print('Результат расчета рекурсивной функции: ', fib_rec(x))
print('Время (с), кол-во вызовов: ', globals()['counter1'])


# recursive with memorizing the calculations

counter2 = 0
M = {0: 0, 1: 1}


@dec_counter('counter2')
def fib_rec_mem(n):
    if n in M:
        return M[n]
    M[n] = fib_rec_mem(n - 1) + fib_rec_mem(n - 2)
    return M[n]


print('Результат расчета рекурсивной функции с запоминанием: ', fib_rec_mem(x))
print('Время (с), кол-во вызовов: ', globals()['counter2'])


# non-recursive

counter3 = 0


@dec_counter('counter3')
def fib_non_rec(n):
    fib1=fib2=1
    fib_sum = 0
    i = 2
    while i < n:
        fib_sum = fib2 + fib1
        fib1 = fib2
        fib2 = fib_sum
        i += 1
    return fib_sum


print('Результат расчета нерекурсивной функции: ', fib_non_rec(x))
print('Время (с), кол-во вызовов: ', globals()['counter3'])

# using matrixes

counter4 = 0
counter00 = 0
counter01 = 0


@dec_counter('counter00')
def matrix_mul(a, b):
    return [[
        a[0][0] * b[0][0] + a[0][1] * b[1][0],
        a[0][0] * b[0][1] + a[0][1] * b[1][1]
    ], [
        a[1][0] * b[0][0] + a[1][1] * b[1][0],
        a[1][0] * b[0][1] + a[1][1] * b[1][1]
    ]]


@dec_counter('counter01')
def power(p):
    m = [[1, 1], [1, 0]]
    t = [[1, 0], [0, 1]]
    while p:
        if p % 2:
            t = matrix_mul(t, m)
        m = matrix_mul(m, m)
        p //= 2
    return t


@dec_counter('counter4')
def fib_matrix(n):
    return power(n)[1][0]


print('Результат расчета с помощью возведения матрицы в степень: ', fib_matrix(x))
print('Общее время (с): ', globals()['counter4'][0])
print('Общее число вызовов:  ', globals()['counter4'][1]+globals()['counter00'][1]+globals()['counter01'][1])

# dynamic

counter5 = 0


@dec_counter('counter5')
def fib_dyn(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a


print('Результат расчета динамической функции: ', fib_dyn(x))
print('Время (с), кол-во вызовов: ', globals()['counter5'])


# ВЫВОД:

# Среди наилучших методов можно выделить нерекурсивный метод, а также динамический подход. Они занимают наименьшее время
# по сравнению с остальными методами, а также требуют минимального числа вызовов. При этом нерекурсивный способ немного
# опережает динамический способ вычисления по времени выполнения.

# Затем можно отметить рекурсию с запоминанием и матричный подход, которые занимают небольшое количество времени
# (примерно равное между собой), но требуют большего числа вызовов.

# Наихудшим показал себя рекурсивный подход, который требует большого числа вызовов и занимает продолжительное время по
# сравнению с остальными способами вычисления.