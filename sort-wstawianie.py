tab=[1,6,3,8,9,3,6,35,22,6,3,6]
print("Od tego zaczynamy: {}".format(tab))
for i in range(1, len(tab)):
    wybrany = tab[i]
    y=i-1
    while y >= 0 and wybrany < tab[y]:
        tab[y+1] = tab[y]
        y -= 1
        print(tab)
    print(tab, wybrany, y)
    tab[y+1] = wybrany

print(tab, "po przenoszeniu")