def fibonacci(n):
    if n<=0:
        return""
    elif n==1:
        return"0"
    elif n==2:
        return "0 1"
    elif n>2:
        wynik="0 1"
        a = 0
        b = 1
        for x in range(3, n+1):
            a, b = b, a+b
            wynik+=" {}".format(b)
        return wynik


print("Podaj liczbę wyrazów ciągu fibonacciego jaką chcesz zobaczyć:")
n = int(input())
print(fibonacci(n))