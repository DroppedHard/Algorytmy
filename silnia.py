def silnia(n):
    if n==0:
        return 1
    else:
        return silnia(n-1)*n


n = int(input("Podaj liczbę:"))
wynik = 1
for i in range(1, n+1):
    wynik*=i
print(wynik)
print("Teraz rekurencja: ")
print(silnia(n))