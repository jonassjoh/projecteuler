a = 0
b = 1
s = 0
while True:
    c = a + b

    if c > 4000000:
        break

    a = b
    b = c
    if c % 2 == 0:
        s += c

print(s)
