class Zadanie_Three:
    def fibonacci_generator(self):
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]