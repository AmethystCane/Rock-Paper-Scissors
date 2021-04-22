from random import randint

# Moves for the player
moves = ["rock", "paper", "scissors"]

while True:
    computer = moves[randint(0, 2)]  # picking a random move from 1 to 3
    player = input("rock, paper or scissors? (or 'end the game'): ").lower()
    if player == "end the game":  # Conditions for ending game
        print("The game has ended. Thank you for playing ^-^")
        break  # stops the while True loop
    elif player == computer:  # Conditions for same moves
        print("Its a tie!")
    elif player == "rock":  # Conditions for rock
        if computer == "paper":
            print("You lose!", computer, "trumps", player)
        else:
            print("You win!", player, "trumps", computer)
    elif player == "paper":  # Conditions for paper
        if computer == "scissors":
            print("You lose!", computer, "trumps", player)
        else:
            print("You win!", player, "trumps", computer)
    elif player == "scissors":  # Conditions for scissors
        if computer == "rock":
            print("You lose!", computer, "trumps", player)
        else:
            print("You win!", player, "trumps", computer)
    else:  # Conditions for misspelled words
        print("Oops! Did you spell your move correctly?")
