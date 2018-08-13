def transform(num):
    return num / 2 if num % 2 == 0 else num * 3 + 1


def collatz_numbers(n, l):
    if n != 1:
        l.append(n)
        collatz_numbers(transform(n), l)
    return l


def collatz_steps(n):
    return len(collatz_numbers(n, list()))


print(collatz_steps(12))

