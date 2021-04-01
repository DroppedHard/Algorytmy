import math
n = int(input("Podaj liczbę:"))
if n <2:
    print("Podana liczba nie jest liczbą pierwszą")
else:
    a = True
    for i in range(2, int(math.sqrt(n))):
        if n%i==0:
            a = False
    print("Podana liczba jest liczbą pierwszą") if a else print("Podana liczba nie jest liczbą pierwszą")
