a = int(input("Podaj podstawę potęgi:"))
n = int(input("Podaj wykładnik potęgi"))

if a == 1 or n==0:
    print("1")
elif n!=0:
    wyklujemny=False if n>0 else True
    n = -n if n < 0 else n
    p=1
    for i in range(1, n+1):
        p *= a
    print(1/p) if wyklujemny else print(p)

# Pomijamy ułamki o wykładniku ułamkowym, bo tak.