print('Введите строку')
string = input().lower()
print(string)

numbers_list = []                                       # var for storage of the list of all the numbers found
number = ''                                             # temp var for storage of one number in str format

while 'cancel' not in string:
    if string[0].isdigit():                             # checking if the 0 element is digit as the cycle starts from 1
        number = ''.join([number, string[0]])

    for elem in range(1, len(string)):
        if string[elem].isdigit():                      # creating the number from digits going one-by-one
            if string[elem-1] == '-':
                number = ''.join(['-', string[elem]])   # if there is the '-' before the digit
            else:
                number = ''.join([number, string[elem]])
        elif number == '':
            continue                                    # when non-digit and number is empty from the previous step
        else:
            numbers_list.append(int(number))            # when number is not empty after the cycle has ended
            number = ''

    if number != '':
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