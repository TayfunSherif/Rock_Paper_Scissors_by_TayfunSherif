from art import rock, paper, scissors, logo
import random
print(logo)
players_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper or 3 for Scissors.\n"))
computer_choice = random.randint(1, 3)

print()
print("You chose:")
print()

if players_choice == 1:
    print(rock)
elif players_choice == 2:
    print(paper)
elif players_choice == 3:
    print(scissors)

print()
print("Computer chose:")
print()

if computer_choice == 1:
    print(rock)
elif computer_choice == 2:
    print(paper)
elif computer_choice == 3:
    print(scissors)

if players_choice == computer_choice:
    print("It's a draw")
elif players_choice == 1 and computer_choice == 2:
    print("You lose")
elif players_choice == 1 and computer_choice == 3:
    print("You win")
elif players_choice == 2 and computer_choice == 1:
    print("You win")
elif players_choice == 2 and computer_choice == 3:
    print("You lose")
elif players_choice == 3 and computer_choice == 1:
    print("You lose")
elif players_choice == 3 and computer_choice == 2:
    print("You win")
