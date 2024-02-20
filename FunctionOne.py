def przywitanie():
    print("Podro z mojej funkcji")

def przywitanie_imienne(imie, zyczenia):
    print ("Witaj " + imie + ". Zycze Tobie " + zyczenia)

def liczbydokwadratu(x):
    y = x
    print(x * y)

def suma_listy(lista):
    suma = 0
    for liczba in lista:
        suma += liczba
    return suma

def generuj_liste_parzystych(limit):
    lista_parzystych = []
    for i in range(2, limit + 1, 2):
        lista_parzystych.append(i)
    return lista_parzystych

