def bin(a):
    if a == 0:
        return "0"
    b = ""
    while a != 0:
        b = str(a % 2) + b
        a = a//2
    return b


n = int(input("Podaj liczbę dziesiętną"))
print(bin(n))