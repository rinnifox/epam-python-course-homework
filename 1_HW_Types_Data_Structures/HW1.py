print ('Введите любые комбинации элементов через пробел')
string = input().split()

new_set = sorted(set(string), key=string.index) # sorting for the same output
print(' '.join(new_set))