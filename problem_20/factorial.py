from functools import reduce
import operator

n = 100
print(sum([int(a) for a in str(reduce(operator.mul, range(1, n+1), 1))]))
