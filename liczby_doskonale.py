n = int(input("Podaj liczbę"))
suma = 0
iloczyn = 1
for i in range(1, (n//2)+1):
    print(n, i)
    if n % i == 0:
        suma += i
        iloczyn *= i
if suma == n:
    print("Liczba {} jest liczbą doskonałą 1 stopnia".format(n))
if iloczyn == n:
    print("Liczba {} jest liczbą doskonałą 2 stopnia".format(n))
if suma != n and iloczyn != n:
    print("Licba {} nie jest liczbą doskonałą".format(n))