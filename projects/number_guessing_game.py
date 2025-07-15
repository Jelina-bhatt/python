import random

def play_game(level):
    max_number = level * 10
    number = random.randint(1, max_number)
    attempts = 0

    print(f"\n🎯 Level {level}: Guess the number between 1 and {max_number}")

    while True:
        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("🚫 Please enter a valid number!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("⬇️ Too low!")
        elif guess > number:
            print("⬆️ Too high!")
        else:
            print(f"✅ Correct! You guessed it in {attempts} tries.")
            return True

def main():
    level = 1
    print("🎉 Welcome to the Number Guessing Game!")

    while True:
        success = play_game(level)
        if success:
            choice = input("🎮 Do you want to play the next level? (y/n): ").lower()
            if choice == 'y':
                level += 1
            else:
                print("👋 Thanks for playing!")
                break

main()
