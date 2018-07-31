print('Введите строку')
string = input().lower()
print(string)
elems_list = []
numbers_list = []
number = ''
while 'cancel' not in string:
    for elem in string:
        elems_list.append(elem)
        if elem.isdigit():
            number=''.join([number, elem])
        elif number == '':
            continue
        else:
            numbers_list.append(int(number))
            number = ''
    if number != '':
        numbers_list.append(int(number))
    print(numbers_list)
    print(elems_list)
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