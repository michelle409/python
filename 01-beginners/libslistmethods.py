import random #library

def get_choice(): #a function is a set of code which only runs when its called.
    player_choice = input("enter a choice(rock, paper, scissors ): ")
    options = ["rock", "paper", "scissors"] #list 
    computer_choice = random.choice(options) #using a library function
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

choices = get_choice()
print(choices) 


 