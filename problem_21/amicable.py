def d(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s

s = 0
for i in range(1, 10000):
    a = d(i)
    b = d(a)
    if b == i and a != b:
        s += i

print(s)
