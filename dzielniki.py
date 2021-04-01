n = int(input("Podaj liczbę:"))
print("Dzielniki to:\n1")
for i in range(2, n):
    if n%i==0:
        print(i)
print(n)