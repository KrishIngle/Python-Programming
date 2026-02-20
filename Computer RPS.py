# Creating a RPS computer game
import random
player_score = 0
computer_score = 0
# Rules and Welcome
print("Welcome to the World of Computer RPS Game")
print("============= Rules ============")
print("1. Rock beats Scissors")
print("2. Paper beats Rock")
print("3. Scissors beats Paper")
print("4. Use 1 for Rock")
print("5. Use 2 for Scissors")
print("6. Use 3 for Paper")
print("7. Anything except 1, 2, 3 will result in breaking of the game:) ")
print("8. Number of Rounds is up to you")
Rounds = int(input("How many Rounds do you want to play: "))
# Main Game
for i in range (Rounds):
    computer = random.randint(1,3)
    player = int(input("Enter your choice: "))
    if player >= 1 and player <= 3 :
        print("Computer's choice: ",computer)
        if computer == 1 and player == 1:
            print("This Round is a TIE!")
            print("In this Round computer's total score is: ",computer_score)
            print("In this Round player's total score is: ",player_score)
        elif computer == 1 and player == 2:
            print("This Round is Won by Computer!")
            computer_score += 1
            print("In this Round computer's total score is: ",computer_score)
            print("In this Round player's total score is: ",player_score)
        elif computer == 1 and player == 3:
            print("This Round is Won by Player!")
            player_score += 1
            print("In this Round computer's total score is: ",computer_score)
            print("In this Round player's total score is: ",player_score)
        elif computer == 2 and player == 1:
            print("This Round is Won by Player!")
            player_score += 1
            print("In this Round computer's total score is: ",computer_score)
            print("In this Round player's total score is: ",player_score)
        elif computer == 2 and player == 2:
            print("This Round is a TIE!")
            print("In this Round computer's total score is: ",computer_score)
            print("In this Round player's total score is: ",player_score)
        elif computer == 2 and player == 3:
            print("This Round is Won by Computer!")
            computer_score += 1
            print("In this Round computer's total score is: ",computer_score)
            print("In this Round player's total score is: ",player_score)
        elif computer == 3 and player == 1:
            print("This Round is Won by Computer!")
            computer_score += 1
            print("In this Round computer's total score is: ",computer_score)
            print("In this Round player's total score is: ",player_score)
        elif computer == 3 and player == 2:
            print("This Round is Won by Player!")
            player_score += 1
            print("In this Round computer's total score is: ",computer_score)
            print("In this Round player's total score is: ",player_score)
        elif computer == 3 and player == 3:
            print("This Round is a TIE!")
            print("In this Round computer's total score is: ",computer_score)
            print("In this Round player's total score is: ",player_score)
    else:
        print("Due to your poor selection of choices you have broken the Game Rules")
        print("Hope you'll never prevail it in your life again")
        print("Better Luck Next Time! :)")
        print("BYE!")
        exit()

# Score and Calculation
print("Computer's total score is: ",computer_score)
print("Player's total score is: ",player_score)
if player_score > computer_score:
    print("!!!!! YOU WON THE GAME !!!!!")
elif player_score == computer_score:
    print("What a TIE Breaking Performance")
else:
    print("!!!!! COMPUTER WON THE GAME !!!!!")
