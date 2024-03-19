class Zadanie_Six:
    @staticmethod
    def safe_function(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Błąd: {e}")
                return None
        return wrapper

    @safe_function
    def dziel(self, a, b):
        return a / b

 # 5.0
 # Błąd: division by zero, None