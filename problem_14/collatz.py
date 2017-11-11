def next_collatz(n):
    return n / 2 if n % 2 == 0 else 3*n + 1

def collatz(n, res):
    if n == 1:
        return 1
    if n in res:
        return res[n]
    s = collatz(next_collatz(n), res) + 1
    res[n] = s
    return s

m = -1
m_i = -1
res = {}

for i in range(2, 1000001):
    c = collatz(i, res)
    if c > m:
        m = c
        m_i = i

print('i: ', m_i, '\nm: ', m)
