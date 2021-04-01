def nwd(n, k):
    a = n % k if n > k else k % n
    if a == 0:
        return n if n < k else k
    return nwd(a, k) if k < n else nwd(a, n)


n = int(input("Podaj 1 liczbę:"))
k = int(input("Podaj 2 liczbę:"))
print(nwd(n, k))