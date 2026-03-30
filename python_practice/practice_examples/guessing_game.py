import random

def play_game():
    print("\nChoose difficulty:")
    print("1. Easy (1-10)")
    print("2. Medium (1-50)")
    print("3. Hard (1-100)")

    level = input("Enter choice: ")

    if level == "1":
        max_num = 10
    elif level == "2":
        max_num = 50
    else:
        max_num = 100

    number = random.randint(1, max_num)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess number (1-{max_num}): "))
            attempts += 1

            if guess < number:
                print("Too low")
            elif guess > number:
                print("Too high")
            else:
                print(f"Correct! Attempts: {attempts}")
                break
        except:
            print("Invalid input")

while True:
    play_game()
    again = input("Play again? (yes/no): ")
    if again.lower() != "yes":
        break