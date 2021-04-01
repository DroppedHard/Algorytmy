def sortSlowo(wyraz):
    s = list(wyraz)
    zm = 1
    wynik = []
    for a in range(len(s)-1):
        if zm == 0:
            break
        zmian = 0
        for c in range(len(s)-1):
            if s[c] > s[c + 1]:
                s[c], s[c+1] = s[c+1], s[c]
                zm += 1
    return ''.join(s)



anag1 = input("Podaj pierwszy wyraz: ")
anag2 = input("Podaj drugi wyraz: ")
if len(anag1) != len(anag2):
    print("Nie są anagramami!")
else:
    wyr1 = sortSlowo(anag1)
    wyr2 = sortSlowo(anag2)
    if wyr1 == wyr2:
        print("No to są angramy!")
    else:
        print("Nie są anagramami!")
