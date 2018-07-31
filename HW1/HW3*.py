print('Введите  целые неотрицательные числа, разделенные любым не цифровым литералом')
string = input().lower()

numbers_list = []
number = ''

while 'cancel' not in string:
    if string[0].isdigit():
        number = ''.join([number, string[0]])

    for elem in range(1, len(string)):
        if string[elem].isdigit():
            if string[elem-1] == '-':
                number = ''.join(['-', string[elem]])
            else:
                number = ''.join([number, string[elem]])
        elif number == '':
            continue
        else:
            numbers_list.append(int(number))
            number = ''

    if number != '':
        numbers_list.append(int(number))

    s = 0

    for counter in numbers_list:
        s += counter

    print('Cумма всех чисел в строке = ', s)

    numbers_list = []
    number = ''
    print('Введите  целые неотрицательные числа, разделенные любым не цифровым литералом')
    string = input().lower()
else:
    print('Bye')