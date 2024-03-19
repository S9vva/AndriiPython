
class Zadanie_Four:
    def __init__(self, liczby):
        self.liczby = liczby

    def kwadraty_powyzej_10(self):
        return [x*x for x in self.liczby if x > 10]

# [121, 144, 169]