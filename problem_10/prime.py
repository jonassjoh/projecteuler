import math

def isprime(p):
    for i in range(2, int(math.sqrt(p) + 1)):
        if p % i == 0:
            return False
    return True

s = 0
for i in range(1, 2000000):
    if isprime(i):
        s += i
        print(i)
print(s)
