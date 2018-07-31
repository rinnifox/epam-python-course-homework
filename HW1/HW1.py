print ('Введите строку')
string = input().split()
set = sorted(set(string), key=string.index)
print(' '.join(string))
print(' '.join(set))

