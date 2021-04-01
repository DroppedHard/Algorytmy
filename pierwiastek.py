import math


def pierw(n):
    x = n/2
    dokl = 0.000001
    while math.fabs(x-n/x) > dokl:
        print(x)
        x = float((x + n / x) / 2)
        if x * x == n:
            break
    return round(x, 6)


print("Podaj liczbę do spierwiastkowania: ")
a = float(input())
print(pierw(a))
