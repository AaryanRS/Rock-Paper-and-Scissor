import random

playoptions = ["Rock", "Paper", "Scissor"]

while True:
    computorChoice = random.choice(playoptions)
    playerChoice = input("Make a choice Rock, Paper, Scissor")

    if computorChoice == playerChoice :
        print("! Tie !")

    if playerChoice == "Rock" :
        if computorChoice == "Paper" :
            print (f"Computor Choice {computorChoice}")
            print (f"You lost, Paper wrape the rock")

        else:
            print (f"Computor Choice {computorChoice}")
            print ("You Win, Rock crushes the scissor")

    elif playerChoice == "Scissor" :
        if computorChoice == "Rock" :
            print (f"Computor Choice {computorChoice}")
            print (f"You lost, Rock crushes the Scissor")

        else:
            print (f"Computor Choice {computorChoice}")
            print ("You Win, Scissor cuts the Paper")

    elif playerChoice == "Paper" :
        if computorChoice == "Scissor" :
            print (f"Computor Choice {computorChoice}")
            print (f"You lost, Scissor cuts the paper")

        else:
            print (f"Computor Choice {computorChoice}")
            print (f"You Win, Paper wrape the Rock")
            