def newton_sqrt(x, accuracy=0.01, approx=1):

    newapprox = 0.5 * (approx + x / approx)

    if abs(newapprox - approx) > accuracy:
        print(newapprox)
        return newton_sqrt(x, approx=newapprox)
    else:
        return round(newapprox, ndigits=2)
