print('Введите строку')
numbers_list = []
number = ''
string = input().lower()

while 'cancel' not in string:
    for elem in string:
        if elem.isdigit():
            number=''.join([number, elem])
        elif number == '':
            continue
        else:
            numbers_list.append(int(number))
            number = ''
    if number != '':
        numbers_list.append(int(number))

    sum=0

    for counter in numbers_list:
        sum+= counter

    numbers_list = []
    number = ''
    print(sum)

    print('Введите строку')
    string = input().lower()

else:
    print('Bye')
