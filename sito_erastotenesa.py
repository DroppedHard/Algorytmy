import math
n = int(input("Podaj liczbę końcową:"))
tab = [True] * (n+1)
for i in range(2, int(math.ceil(math.sqrt(n)))):
    if tab[i]:
        for a in range(i*i, n+1, i):
            tab[a]=False
print("Liczby pierwsze z przedziału <2,"+str(n)+"> : ")
for i in range(2, n+1):
    if tab[i]:
        print(i, end="|")



