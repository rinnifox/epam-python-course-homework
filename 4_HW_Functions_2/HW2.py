def newton_sqrt(x, accuracy=0, approx=1):
    newapprox = (approx + x / approx) / 2

    if abs(newapprox - approx) > accuracy:
        return newton_sqrt(x, approx=newapprox)
    else:
        return newapprox
