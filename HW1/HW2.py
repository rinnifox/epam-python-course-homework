print('Введите строку')
string = input().lower().split()

numbers = {}                             # var for dict {'word': num of occurencies}

while 'cancel' not in string:
    for elem in string:
        number = string.count(elem)      # counting the number of occurencies of the element
        numbers.update({elem: number})
    maxvalue = max(numbers.values())     # finding the max value in the dict

    for key, value in numbers.items():   # finding the keys corresponding to max value
        if value == maxvalue:
            print('{k} - {v}'.format(k=key, v=value))

    print('Введите строку')
    string = input().lower().split()
else:
    print('Bye')

