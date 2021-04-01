def nwd(n, k):
    a = n % k if n > k else k % n
    if a == 0:
        return n if n < k else k
    return nwd(a, k) if k < n else nwd(a, n)


def nww(n, k):
    return n*k//nwd(n, k)


n = int(input("Podaj 1 liczbę:"))
k = int(input("Podaj 2 liczbę:"))
print(nww(n, k))