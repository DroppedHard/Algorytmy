print("Program szyfrujący tekst za pomocą Szyfru cezara")
print("Podaj tekst do zaszyfrowania: ")
word = input().upper()
print("Podaj klucz szyfrowania (ilość przesunięć): ")
p = int(input())
encrypted = ""
for c in word:
    if c != "\n":
        ch = chr(ord(c) + p)
        if ord(ch) > ord('Z'):
            ch = chr(ord(ch)-26)
        encrypted += ch
print("Twój tekst po szyfrowaniu cezara wygląda tak: " + encrypted)