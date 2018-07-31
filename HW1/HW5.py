def is_palindrome(x):
    reverse_x = str(x)[::-1]
    if str(x) == reverse_x:
        y = str(bin(x)[2::])
        reverse_y = y[::-1]
        if y == reverse_y:
            return x
        else:
            return 0
    else:
        return 0


s = 0

for i in range(1, 1000000, 2):
    number = is_palindrome(i)
    s += number
    
print(s)

