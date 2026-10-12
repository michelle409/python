import random

def get_choice():
    player_choice = input("enter a choice(rock, paper, scissors ): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "its a tie!"
    elif player == "rock" and computer == "scissors":
        return "rock smashes scissors. You win!"
    elif player == "rock" and computer == "paper":
        return "paper covers rock. You lose!"
    elif player == "paper" and computer == "rock":
        return "paper covers rock. You win!"
    elif player == "paper" and computer == "scissors":
        return "scissors cuts paper. You lose!"
    elif player == "scissors" and computer == "paper":
        return "scissors cuts paper. You win!"
    elif player == "scissors" and computer == "rock":
        return "rock smashes scissors. You lose!"

choices = get_choice()
result = check_win(choices["player"], choices["computer"])
print(result)