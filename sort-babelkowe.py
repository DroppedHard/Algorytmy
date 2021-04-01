def babelkowe(tab):
    zamiany = 1
    while zamiany != 0:
        zamiany = 0
        for n in range(len(tab)-1):
            if tab[n]>tab[n+1]:
                tab[n], tab[n+1] = tab[n+1], tab[n]
                zamiany += 1
        print(tab)


tab=[1,6,3,8,9,3,6,35,22,6,3,6]
babelkowe(tab)
print(tab)