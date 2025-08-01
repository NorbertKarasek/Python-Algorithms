# Przechwytywanie argumentów w funkcji

def funkcja(*args, **kwargs):
    print(f"args {args}")      # tuple z wszystkimi argumentami pozycyjnymi
    print(f"kwargs {kwargs}")    # słownik z argumentami nazwanymi

# Przykładowe wywołanie funkcji
funkcja(1, 2, 3, a=4, b=5)

# Output:
# (1, 2, 3)
# {'a': 4, 'b': 5}