def minMax(tab):
    min = tab[0]
    max = tab[0]
    for i in tab:
        if i<min:
            min = i
        elif i>max:
            max = i
    odp = []
    odp.append(min)
    odp.append(max)
    return odp


def sortKub(tab, n):
    minmax = minMax(tab)
    min = minmax[0]
    max = minmax[1]
    kubelki = [0] * (max - min + 1)
    for i in range(n):
        kubelki[tab[i]-min]+=1
    print("Zliczono:")
    for i in range(max - min+1):
        print("B", (i+min), "=", kubelki[i], end=" | ")
    print()
    ostIndex = 0
    for i in range(max-min+1):
        j = ostIndex
        while j < kubelki[i] + ostIndex:
            tab[j] = i+min
            j+=1
        ostIndex = j


tabela =[1,6,3,8,9,3,6,35,22,6,3,6]
sortKub(tabela, len(tabela))
print(tabela)
