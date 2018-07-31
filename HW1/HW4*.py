print('Введите строку')
string = input().split()

while 'cancel' not in string:

    next_even = 0

    for elem in string:
        if int(elem) % 2 == 0:
            next_even = int(elem) + 2
            if str(next_even) in string:
                continue
            else:
                print('Наименьшее положительное - ',next_even)
                break

    print('Введите строку')
    string = input().split()

else:
    print('Bye')