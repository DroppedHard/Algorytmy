def dec(a):
    i = len(a) - 1
    dec = 0
    for c in a:
        dec += int(c) * pow(2, i)
        i -= 1
    return dec


n = input("Podaj liczbę binarną")
print(dec(n))
