import math

n = int(input("Podaj dodatnią liczbę:"))
print('{}='.format(n), end='')
a = 2
while n>=2:
    while n % a ==0:
        print("{}*".format(a), end="")
        n = n // a
    a += 1
print("1")