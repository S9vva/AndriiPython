from itertools import product

class Zadanie_One:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def generate_combinations(self):
        # Generowanie i wydrukowanie wszystkich możliwych kombinacji
        for combination in product(self.list1, self.list2):
            print(combination)

#('A', 'C')
#('A', 'D')
#('B', 'C')
#('B', 'D')