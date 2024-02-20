zmienna_globalna = 10

def funkcja_zmiennymi_funkcyjnymi_i_globalnymi():
    zmienna_lokalna = 20

    def wewnetrzna_funkcja():
        nonlocal zmienna_lokalna
        zmienna_lokalna += 5
        print("Zmienna lokalna wewnątrz wewnętrznej funkcji:", zmienna_lokalna)

    wewnetrzna_funkcja()
    print("Zmienna globalna wewnątrz funkcji:", zmienna_globalna)

if __name__ == "__main__":
    print("To jest plik FunctionThree.py.")
