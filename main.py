from Zadanie_One import Zadanie_One
from Zadanie_Two import Zadanie_Two
from Zadanie_Three import Zadanie_Three
from Zadanie_Four import Zadanie_Four
from Zadanie_Five import Zadanie_Five
from Zadanie_Six import Zadanie_Six

#Zadanie 1
list1 = ['A', 'B']
list2 = ['C', 'D']

zadanie = Zadanie_One(list1, list2)
zadanie.generate_combinations()

#Zadanie 2
elements = ['A', 'B', 'C', 'D']

zadanie_two = Zadanie_Two()
combinations = zadanie_two.generate_combinations(elements)
print(combinations)

#Zadanie 3

zadanie_three = Zadanie_Three()
fib_gen = zadanie_three.fibonacci_generator()

for _ in range(10):
        print(next(fib_gen))

#Zadanie 4

liczby = [3, 4, 5, 11, 12, 13]
zadanie = Zadanie_Four(liczby)
kwadraty_powyzej_10 = zadanie.kwadraty_powyzej_10()
print(kwadraty_powyzej_10)

#Zadanie 5

zadanie_five = Zadanie_Five()
string = "A man a plan a canal Panama"
if zadanie_five.is_palindrome(string):
        print(f"'{string}' is a palindrome.")
else:
        print(f"'{string}' is not a palindrome.")

#Zadanie 6
zadanie_six = Zadanie_Six()
string = "A man, a plan, a canal, Panama!"
if zadanie_six.is_palindrome(string):
        print(f"'{string}' is a palindrome.")
else:
        print(f"'{string}' is not a palindrome.")

