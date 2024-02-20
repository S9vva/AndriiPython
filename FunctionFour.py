def funkcja_do_przekazania(a, b, c):
    print("Funkcja do przekazania została wywołana z argumentami:", a, b, c)

def funkcja_ktora_przyjmuje_inna_funkcje(funkcja, argument1, argument2, argument3):
    print("Funkcja przyjęła inną funkcję i wywoła ją z argumentami:")
    funkcja(argument1, argument2, argument3)

if __name__ == "__main__":
    funkcja_ktora_przyjmuje_inna_funkcje(funkcja_do_przekazania, 1, 2, 3)
