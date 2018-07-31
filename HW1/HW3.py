print('Введите  целые неотрицательные числа, разделенные любым не цифровым литералом')
string = input().lower()

numbers_list = []
number = ''

while 'cancel' not in string:
    for elem in string:
        if elem.isdigit():
            number = ''.join([number, elem])
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
