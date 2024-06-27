# Hangman Game
import random
def hangman(word):
    wrong = 0
    stages = ["",
                "________        ",
                "|               ",
                "|        |      ",
                "|        0      ",
                "|       /|\     ",
                "|       / \     ",
                "|               "
                ]
    rletters = list(word.lower())
    board = ["_"] * len(word)
    win = False
    print("\nWelcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg).lower()
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            if len(char) > 1:
                print("Please enter a single letter")
                continue
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(f'The word is {"".join(board).upper()}')
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

list_of_words = ["cat", "dog", "elephant", "giraffe", "hippopotamus", "kangaroo", "lion", "monkey", "penguin", "rhinoceros", "tiger", "zebra"]

hangman(random.choice(list_of_words))