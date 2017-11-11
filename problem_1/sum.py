s = 0
for a in range(1000):
    if a % 3 == 0 or a % 5 == 0:
        s += a
print(s)
