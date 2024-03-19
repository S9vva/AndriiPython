from itertools import combinations

class Zadanie_Two:
    def generate_combinations(self, elements):
        comb = list(combinations(elements, 2))
        return comb

#[('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
