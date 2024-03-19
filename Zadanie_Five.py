class Zadanie_Five:
    @staticmethod
    def is_palindrome(s): return s.lower().replace(" ", "") == s.lower().replace(" ", "")[::-1]

#'A man a plan a canal Panama' is a palindrome. (True)

