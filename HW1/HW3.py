print('Введите строку')
string = input().lower()

numbers_list = []                              # var for storage of the list of all the numbers found in the string
number = ''                                    # temp var for storage of one number in str format

while 'cancel' not in string:
    for elem in string:
        if elem.isdigit():
            number = ''.join([number, elem])   # creating the number from digits going one-by-one
        elif number == '':
            continue                           # when non-digit and number is empty from the previous step
        else:
            numbers_list.append(int(number))
            number = ''
    if number != '':                           # when number is not empty after the cycle has ended
        numbers_list.append(int(number))

    s = 0

    for counter in numbers_list:
        s += counter

    print(s)

    numbers_list = []
    number = ''
    print('Введите строку')
    string = input().lower()

else:
    print('Bye')
