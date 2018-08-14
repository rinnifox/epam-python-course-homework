def newton_sqrt(x, accuracy=0.0, approx=1):
    newapprox = (approx + x / approx) / 2

    if abs(newapprox - approx) > 0:
        return newton_sqrt(x, approx=newapprox, accuracy=accuracy)

    else:
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