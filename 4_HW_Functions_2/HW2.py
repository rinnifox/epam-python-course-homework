def newton_sqrt(x, accuracy=0.0, approx=1):
    newapprox = (approx + x / approx) / 2
    if abs(newapprox - approx) > accuracy:
        return newton_sqrt(x, approx=newapprox, accuracy=accuracy)
    else:
        return newapprox


print(newton_sqrt(5))
print(newton_sqrt(5, accuracy=0.001))
print(newton_sqrt(5, accuracy=0.01))
print(newton_sqrt(5, accuracy=0.1))
