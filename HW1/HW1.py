print ('Введите любые комбинации элементов через пробел')
string = input().split()

new_set = sorted(set(string), key=string.index)  # sorting the set for the same output order
print(' '.join(new_set))

