def newton_sqrt(x, accuracy=0.0, percentage=100, approx=1):
    newapprox = (approx + x / approx) / 2
    if percentage == 100:
        if abs(newapprox - approx) > 0:
            return newton_sqrt(x, approx=newapprox, accuracy=accuracy, percentage=percentage)
    else:
        approximation = (x / (newapprox * newapprox)) * 100
        if approximation < percentage:
            return newton_sqrt(x, approx=newapprox, accuracy=accuracy, percentage=percentage)

    if accuracy == 0.0:
        return newapprox
    else:
        s = str(accuracy)
        r = abs(s.find('.') - len(s)) - 1
        return round(newapprox, ndigits=r)


print(newton_sqrt(5))
print(newton_sqrt(5, accuracy=0.001))
print(newton_sqrt(5, accuracy=0.01))
print(newton_sqrt(5, accuracy=0.1))


print(newton_sqrt(4/1000000))
print(newton_sqrt(4/1000000, accuracy=0.01))
print(newton_sqrt(4/1000000, accuracy=0.1))


print(newton_sqrt(10000, percentage=100))
print(newton_sqrt(10000, percentage=75))
print(newton_sqrt(10000, percentage=30))
