def ispalindrome(c):
    c = str(c)
    for d in range(int(len(c)/2)):
        if not (c[d] == c[len(c)-d-1]):
            return False
    return True

e = 0
for a in range(100, 1000):
    for b in range(100, 1000):

        c = a * b
        if ispalindrome(c):
            if c > e:
                e = c

print(e)
