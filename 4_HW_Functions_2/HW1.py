def find_number(string):
    symbol = ord(string[-1])
    digit = int(chr(symbol))

    if len(string) == 1:
        return digit
    else:
        return find_number(string[:-1])*10 + digit


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
