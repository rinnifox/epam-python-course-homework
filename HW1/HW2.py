print ('Введите строку')
string = input().lower().split()
numbers = {}
while 'cancel' not in string:
    for elem in string:
        number = string.count(elem)
        numbers.update({elem:number})
    maxvalue = max(numbers.values())
    for key, value in numbers.items():
        if value == maxvalue:
            print ('{k} - {v}'.format(k=key, v=value))
    print ('Введите строку')
    string = input().lower().split()
else:
    print ('Bye')

