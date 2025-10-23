import random

def game():
    computerTurn = ["snake", "water", "gun"]
    computerInput = random.choice(computerTurn)

    userInput = input("Your Turn")

    result = ""

    if(userInput == computerInput):
        result = "It's a tie"
    elif(userInput == "snake" and computerInput == "water"):
        result = "You won"
    elif(userInput == "water" and computerInput == "gun"):
        result = "You won"
    elif(userInput == "gun" and computerInput == "snake"):
        result = "You won"
    else:
        result = "Computer won"
    
    print(f"Your choice {userInput}")
    print(f"Computer's choice {computerInput}")
    print(result)

game()
game()
game()
game()
game()