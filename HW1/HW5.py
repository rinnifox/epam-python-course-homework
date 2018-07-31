def is_palindrome(x):
    reverse_x = str(x)[::-1]  # reversing the decimal number
    if str(x) == reverse_x:
        y = str(bin(x)[2::])  # converting to binary, removing '0b'
        reverse_y = y[::-1]   # reversing binary number
        if y == reverse_y:
            return x          # return the original number if both conditions are true
        else:
            return 0
    else:
        return 0


s = 0

for i in range(1, 1000000, 2):
    number = is_palindrome(i)
    s += number

print(s)

