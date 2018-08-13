from math import sqrt
from functools import reduce


res1 = reduce(lambda a, b: a+b, map(lambda x: x if int(sqrt(x)) == float(sqrt(x)) else 0, range(10**6)))

res2 = reduce(lambda a, b: a+b, filter(lambda x: int(sqrt(x)) == float(sqrt(x)), range(10**6)))

res3 = reduce(lambda a, b: a+b, [x for x in range(10**6) if int(sqrt(x)) == float(sqrt(x))])
