import sys

def triplet(a, b, c):
    return round(a*a) + round(b*b) == round(c*c)

print(triplet(3,4,5))

for a in range(1, 1000):
    print('a: ', a)
    for b in reversed(range(1, 1000)):
        for c in range(a+1, b):
            if triplet(a, c, b):
                print(a,c,b)
                if a + b + c == 1000:
                    print(a*b*c)
                    sys.exit()
