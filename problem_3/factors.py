def isprime(n):
    for i in range(2, int(n/2+1)):
        if n % i == 0:
            return False
    return True

number = 600851475143

i = 2
while True:
    if i > number + 1:
        break
    if isprime(i):
        if number % i == 0:
            print(i)
            number /= i
    i += 1
