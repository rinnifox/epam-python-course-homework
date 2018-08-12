def find_number(string):
    if int(string) / 10 < 1:
        return int(string) % 10
    else:
        return 10*find_number(string[:-1]) + int(string[-1])


while True:
    line = input('Введите текст: ')

    if line == 'cancel':
        print('Bye')
        break
    elif line.isdigit():
        number = find_number(line)
        if number % 2 == 0:
            res = number / 2
        else:
            res = number * 3 + 1

        print(round(res, ndigits=2))
    else:
        print('Не удалось преобразовать введенный текст в число')
