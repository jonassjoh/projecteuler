number = ''
with open('number.in') as f:
    for line in f:
        number += line.strip()

def product(a):
    a_s = 1
    for p in a:
        p = int(p)
        a_s *= p
    return a_s

chunk = 13
s = 0
for i in range(len(number) - 1 - chunk):
    a = number[i:i+chunk]
    p = product(a)
    if p > s:
        s = p

print(s)
