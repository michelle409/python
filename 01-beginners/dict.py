def get_choice(): #a function is a set of code which only runs when its called.
    player_choice = "rock"  #creating a variable called plater_choice. can use "" or ''. has to end and start wuith the same kind of quotes.
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

choicess = get_choice()
print(choicess) 


