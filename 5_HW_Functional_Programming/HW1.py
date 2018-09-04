from math import sqrt
from functools import reduce
import time

s = time.time()

res1 = reduce(lambda a, b: a+b, (map(lambda x: x**2, range(10**3))))

res2 = reduce(lambda a, b: a+b, filter(lambda x: int(sqrt(x)) == float(sqrt(x)), range(10**6)))

res3 = reduce(lambda a, b: a+b, ([x**2 for x in range(10**3)]))

print(res1)
print(res2)
print(res3)

end = time.time()

print('time =', end-s)
