import Wojna

def main():
    print("Witamy w grze Wojna!")
    print("Zasady są proste: każdy z graczy otrzymuje po jednej karcie z talii, a następnie porównuje się wartości kart.")
    print("Gracz, który otrzyma kartę o wyższej wartości, zdobywa punkt.")
    print("Jeśli wartości kart są równe, to mamy wojnę!")
    print("Wojna polega na tym, że obaj gracze odkładają po jednej karcie na stos, a następnie porównują kolejne karty.")
    print("Gracz, który otrzyma kartę o wyższej wartości, zdobywa wszystkie karty ze stosu.")
    print("Gra kończy się, gdy talia kart jest pusta.")
    print("\nPowodzenia!\n")

    # Create a War object
    game = Wojna.Game()

    # Play the game
    game.play_game()

main()