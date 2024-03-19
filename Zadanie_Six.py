class Zadanie_Six:
    @staticmethod
    def is_palindrome(s):
        processed_string = ''.join(c.lower() for c in s if c.isalnum())
        return processed_string == processed_string[::-1]