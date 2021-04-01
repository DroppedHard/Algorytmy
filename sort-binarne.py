def wyszukaj(tab, el, l, r):
    print("Szukamy ", el, " w ", tab, l, r)
    sr = int((l + r) / 2)
    if l >= r:
        if el >= tab[l]:
            print("Pozyja elementu to ", (l+1))
            return l + 1
        else:
            print("Pozyja elementu to ", l)
            return l
    if tab[sr] == el:
        print("Pozyja elementu to ", (sr+1))
        return sr + 1
    if tab[sr] < el:
        return wyszukaj(tab, el, sr+1, r)
    else:
        return wyszukaj(tab, el, l, sr-1)


def sortuj_binarnie(tab, n):
    for i in range(1, n):
        el = tab[i]
        j = i - 1
        pos = wyszukaj(tab, el, 0, j)
        while j >= pos:
            tab[j+1] = tab[j]
            j -= 1
        if i != j+1:
            print('przenoszenie ', el, ' z pozycji ', i, ' na ', (j+1))
        else:
            print("Element ", el, " pozostaje na miejscu")
        tab[pos] = el
        print(tab)


# tabela=[1,6,3,8,9,3,6,35,22,6,3,6,3,6,4,6,342,7,234,7,3,6,47,435,6,34,7,42,6,5,6,17,456,34,7,3,57,0,45,7,45,7,435,6,34,7,345,6,34,6,0,6]
tabela=[1,6,3,8,9,3,6,35,22,6,3,6]
sortuj_binarnie(tabela, len(tabela))
print(tabela, 'po sortowaniu')