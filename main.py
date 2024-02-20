import FunctionOne
import FunctionsTwo
import FunctionThree


#Zadanie 1

FunctionOne.przywitanie()

FunctionOne.przywitanie_imienne('Andrii','Zdrowka')

FunctionOne.liczbydokwadratu(5)

moja_lista = [1, 2, 3, 4, 5]
wynik_sumy = FunctionOne.suma_listy(moja_lista)
print("Suma liczb w liście:", wynik_sumy)

print(FunctionOne.generuj_liste_parzystych(10))

#Zadanie 2

FunctionsTwo.kalkulator_dodawania(5,40)

#Zadanie 3

from FunctionThree import funkcja_zmiennymi_funkcyjnymi_i_globalnymi, zmienna_globalna

if __name__ == "__main__":
    funkcja_zmiennymi_funkcyjnymi_i_globalnymi()
    print("Zmienna globalna poza funkcją:", zmienna_globalna)

#Zadanie 4

from FunctionFour import funkcja_do_przekazania, funkcja_ktora_przyjmuje_inna_funkcje

if __name__ == "__main__":
    print("Wywołanie funkcji funkcja_ktora_przyjmuje_inna_funkcje bezpośrednio w pliku main.py:")
    funkcja_ktora_przyjmuje_inna_funkcje(funkcja_do_przekazania, 1, 2, 3)

#Zadaine 5









