import random
random.seed(1234)

# ASCII Art
ROCK = """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

PAPER = """     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)"""

SCISSORS = """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

# Mapping numbers to choices and ASCII
CHOICES = {
    1: ("rock", ROCK),
    2: ("paper", PAPER),
    3: ("scissors", SCISSORS)
}

# Initialize scores
scores = {
    "player": {"wins": 0, "losses": 0, "draws": 0},
    "bot": {"wins": 0, "losses": 0, "draws": 0}
}

# Rules: key beats value
RULES = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def print_separator():
    print("#" * 25)

def play_round(player_choice):
    bot_choice_num = random.randint(1, 3)
    bot_choice, bot_art = CHOICES[bot_choice_num]
    player_art = CHOICES[player_choice][1]
    player_name_choice = CHOICES[player_choice][0]

    print("\nRock! Paper! Scissors! Shoot!\n")
    print_separator()
    print(f"{player_name} chose {player_name_choice}.\n")
    print(player_art)
    print_separator()
    print(f"{bot_name} chose {bot_choice}.\n")
    print(bot_art)
    print_separator()
    
    if player_name_choice == bot_choice:
        print(f"Draw! Both players chose {player_name_choice}.")
        scores["player"]["draws"] += 1
        scores["bot"]["draws"] += 1
    elif RULES[player_name_choice] == bot_choice:
        print(f"{player_name_choice.capitalize()} beats {bot_choice}. {player_name} wins!")
        scores["player"]["wins"] += 1
        scores["bot"]["losses"] += 1
    else:
        print(f"{bot_choice.capitalize()} beats {player_name_choice}. {bot_name} wins!")
        scores["player"]["losses"] += 1
        scores["bot"]["wins"] += 1

# Main program
print("Program starting.")
print("Welcome to the rock-paper-scissors game!")

player_name = input("Insert player name: ")
bot_name = "RPS-3PO"

print(f"Welcome {player_name}!")
print(f"Your opponent is {bot_name}.")
print("Game starts...\n")

while True:
    print("Options:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    print("0 - Quit game")
    
    try:
        choice = int(input("Your choice: "))
        if choice == 0:
            break
        elif choice in (1, 2, 3):
            play_round(choice)
        else:
            print("Invalid choice. Please select 0, 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Enter a number.")

# Display final results
print("\nResults:")
print(f"{player_name} - wins ({scores['player']['wins']}), "
      f"losses ({scores['player']['losses']}), "
      f"draws ({scores['player']['draws']})")
print(f"{bot_name} - wins ({scores['bot']['wins']}), "
      f"losses ({scores['bot']['losses']}), "
      f"draws ({scores['bot']['draws']})")
print("\nProgram ending.")
