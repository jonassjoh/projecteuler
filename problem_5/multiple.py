def isSmallestMultiple(number, r):
    for i in range(1, r + 1):
        if not number % i == 0:
            return False
    return True


# 2 3 2 5 7 2 3 11 13 2 17 19

number = 232792559
while True:
    number += 1
    if isSmallestMultiple(number, 20):
        break

print(number)
print(2*3*2*5*7*2*3*11*13*2*17*19)
