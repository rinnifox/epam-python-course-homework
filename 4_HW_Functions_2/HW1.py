def find_number(string):
    digit = int(string)

    if digit / 10 < 1:
        return digit % 10
    else:
        return 10*find_number(string[:-1]) + digit % 10


while True:
    line = input('Введите текст: ')

    if line == 'cancel':
        print('Bye')
        break
    elif line.isdigit():
        number = find_number(line)
        if number % 2 == 0:
            res = number // 2
        else:
            res = number * 3 + 1

        print(res)
    else:
        print('Не удалось преобразовать введенный текст в число')
