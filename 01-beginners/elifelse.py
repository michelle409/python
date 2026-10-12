import random #library

def get_choice(): #a function is a set of code which only runs when its called.
    player_choice = input("enter a choice(rock, paper, scissors ): ")
    options = ["rock", "paper", "scissors"] #list 
    computer_choice = random.choice(options) #using a library function
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

"""def check_win(player,computer): #arguments
    print("you chose"+ player + ",computer chose " + computer) #concantenating stringss
    if player==computer:
        return"its a tie" 
"""
"""age = 35
 print("jim is {age} years old.") - fstrings"""

#USING FSTRINGS :
def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer : #else and elif statements.
        return "its a tie!"
    elif player == "rock" and computer ==  "scissors" :
        return "rock smashes scissors. You win!"
    elif player == "rock" and computer ==  "paper" :
        return "paper covers rock. You lose!"
  
check_win("rock", "paper")