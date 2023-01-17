import random

#the project must be built so that the first one to win two times is the winner.
#if it keeps tied, keep playing until one of the two players wins two games
print("The first one that wins two rounds, is the winner")
user_won = 0
computer_won = 0
round = 1

#let´s create a tuple with the options
options = ("rock", "paper", "scissors")

#we will play until someone wins two times bro
while ((computer_won<2) and (user_won<2)):

    print("*"*10)
    print("ROUND", round)
    print("*"*10)
    round = round+1
    #human choice
    user_option = input("rock, paper or scissors? => ")
    user_option = user_option.lower()

    #computer choice
    #random.choice selects an element within a tuple or a list
    computer_option = random.choice(options)

    while user_option not in options:
        print("That is not an actual option, choose between rock, paper or scissors")
        user_option = input("rock, paper or scissors? => ")

    #print both choices
    print("The human chose - "+user_option+" -")
    print("The computer chose - "+computer_option+" -")

    #game code: -If- conditionals are used to set the logic of the game
    if user_option == computer_option:
        print("Tied")
    elif (user_option == "rock") and (computer_option == "paper"):
        print("HAHA, YOU LOST")
        computer_won = computer_won+1
    elif (user_option == "rock") and (computer_option == "scissors"):
        print("You won, GG")
        user_won = user_won+1
    elif (user_option == "paper") and (computer_option == "rock"):
        print("You won, GG")
        user_won = user_won+1
    elif (user_option == "paper") and (computer_option == "scissors"):
        print("HAHA, YOU LOST")
        computer_won = computer_won+1
    elif (user_option == "scissors") and (computer_option == "rock"):
        print("HAHA, YOU LOST")
        computer_won = computer_won+1
    elif (user_option == "scissors") and (computer_option == "paper"):
        print("You won, GG")
        user_won = user_won+1


if user_won ==2:
    print("You Finally won, CONGRATULATIONS c:")
else:
    print("You Finally lost, GG ez noob")


'''
#alternative computer choice
computerchoose = random.randint(0,2)
if computerchoose == 0:
    computer_option = "rock"
elif computerchoose == 1:
    computer_option = "paper"
elif computerchoose == 2:
    computer_option = "scissors"
'''