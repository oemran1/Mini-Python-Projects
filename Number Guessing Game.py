import random

print("🎲 Welcome to the Mystery Number Game! 🎲")
print("🔍 Can you guess the secret number? Let's find out! 🔎")

while True:
    top_of_range = input("🔢 Choose the maximum range for the mystery number: ")

    if top_of_range.isdigit() and int(top_of_range) > 0:
        top_of_range = int(top_of_range)
        break
    else:
        print("❌ Please enter a positive integer for the range.")

random_number = random.randint(0, top_of_range)
guesses = 0

print("\n🤔 Let's get started! Try to guess the mystery number.")

while True:
    guesses += 1
    user_guess = input("💭 Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_number:
            print("🎉 Congratulations! You guessed the mystery number!")
            break
        elif user_guess > random_number:
            print("⬆️ Too high! Try guessing a lower number.")
        else:
            print("⬇️ Too low! Try guessing a higher number.")
    else:
        print("❌ Please enter a valid number.")

print(f"🔍 You found the mystery number in {guesses} guesses! Well done!")

