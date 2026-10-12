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

def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer : #refactoring and nested if 
        return "its a tie!"
    elif player == "rock" 
      if computer =="scissors"
        return "rock smashes scissors. You win!"
      else :
        return "paper covers rock. You lose!"
    elif player == "paper" 
      if computer =="rock"
        return "paper covers rock. You win!"
      else :
        return "scissors cuts paper. You lose
    elif player == "scissors" 
      if computer =="paper"
        return "scissors cuts paper. You win!"
      else :
        return "rock smashes scissors. You lose!"

choices = get_choices()
result + check_win(choices["player"], choices["computer"])

"""choices = {"player": "rock", "computer": "paper"}
p_choice = choices["player"]""" #getting the key value, here the key value of palyer is rock.



    
  
  
  
  
  
  
  
  
  