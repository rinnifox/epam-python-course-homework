from functools import reduce

# problem 9

pifagor = reduce(lambda a: a, [a*b*(1000-a-b) for a in range(3, 1000) for b in range(a+1, 1000-a)
                               if a**2 + b**2 == (1000-a-b)**2])

# problem 6

dif = reduce(lambda a, b: a+b, (i for i in range(1, 101)))**2 - \
      reduce(lambda a, b: a+b, (i*i for i in range(1, 101)))

# problem 48

last_ten = str(reduce(lambda a, b: a+b, (x**x for x in range(1, 1001))))[-10:]

# problem 40

champernowne = reduce(lambda x, y: x*y, list(map(int,((reduce(lambda a, b: a+b, (str(i) for i in range(25000))))[10**c]
                                                      for c in range(6)))))


print ('Problem #9 answer =', pifagor)
print ('Problem #6 answer =', dif)
print('Problem #48 answer =', last_ten)
print('Problem #40 answer =', champernowne)
