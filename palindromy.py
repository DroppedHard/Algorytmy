def czyPalindrom(tekst):
    tekst = tekst.lower().replace(" ", "")
    n = len(tekst)
    for c in range(n//2):
        print(tekst[c], tekst[-c-1])


txt = input("Podaj tekst:")
czyPalindrom(txt)