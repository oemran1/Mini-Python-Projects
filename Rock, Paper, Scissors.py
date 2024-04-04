import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You won!"
    else:
        return "You lost!"

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid input! Please type Rock, Paper, Scissors, or Q to quit.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    result = determine_winner(user_input, computer_pick)
    print(result)

    if result == "You won!":
        user_wins += 1
    elif result == "You lost!":
        computer_wins += 1

print(f"You won {user_wins} times and the computer won {computer_wins} times!")
print("Goodbye!")

        
    
